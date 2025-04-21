# Classes for caching lastfm user data
# Focus: User cache to handle and limit api calls

# Create a list of each month and year since the user registered
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import calendar
import time

TOP_LIMIT = 10 # Limit for top artists, albums, tracks, and genres

class UserCache:
    def __init__(self, network):
        self.network = network
        self.user = network.get_authenticated_user()
        self.username = self.user.get_name()
        self.months_regiestered = 0
        self.years_registered = 0
        self.unixtime_registered = self.user.get_unixtime_registered()
        self.months_since_registered_dict = self.create_months_since_registered_dict();
        # Cached data
        self.monthly_data_cache= {}  # key = time, item = data (or None if data has not yet been cached)
        self.yearly_data_cache = {}
        self.alltime_data_cache = None
        

    def get_username(self):
        return self.username
    
    def get_unixtime_registered(self):
        return self.unixtime_registered

    def create_months_since_registered_dict(self):
        # Get the registration date
        registration_date = datetime.fromtimestamp(self.unixtime_registered)

        # Get the current date
        current_date = datetime.now()

        # Create a dictionary of each month and year since the user registered
        months = 0
        months_years = {}
        while registration_date <= current_date:
            months_years[registration_date.strftime("%Y-%m")] = None # Key set to year-month, Item initially set to None
            registration_date += relativedelta(months=1)
            months += 1
        
        # Save the number of months and years since the user registered
        self.months_registered = months
        self.years_registered = months // 12 # treated as int, don't need decimal places for year

        return months_years
    
    def get_months_since_registered_list(self):
        # Return the list of months and years since the user registered
        return list(self.months_since_registered_dict.keys())
    
    def get_months_since_registered_dict(self):
        # Return the dictionary of months and years since the user registered
        return self.months_since_registered_dict
    
    def get_monthly_data(self, year, month):
        # Get the monthly data for the given year and month
        date = f"{year}-{month}"
        if date in self.monthly_data_cache:
            print("Data already cached")
            return self.monthly_data_cache[f"{year}-{month}"]
        else:
            data = MonthlyData(year, month, self.network)
            data.cache_data
            self.monthly_data_cache.update({date : data})
            print("Data newly cached")
            return data
        
    def get_yearly_data(self, year):
        # Get the yearly data for the given year
        if year in self.yearly_data_cache:
            return self.yearly_data_cache[year]
        else:
            print(f"Yearly data for {year} not found.")
            return None
        
    def get_alltime_data(self):
        # Get the alltime data
        if self.alltime_data_cache:
            return self.alltime_data_cache
        else:
            print("Alltime data not found.")
            return None
    
    def print_data(self):
        # Print out the username and the number of months and years since the user registered
        print(f"Username: {self.username} \n")
        print(f"Months since registration: {self.months_registered} \n")
        print(f"Years since registration: {self.years_registered} \n")
        print(f"Unix time registered: {self.unixtime_registered} \n")
        print(f"Months since registration dictionary: {self.months_since_registered_dict} \n")
        print(f"Months filled: {self.monthly_data_cache} \n")

class Data:
    def __init__(self):
        pass


# Montly Data Object
class MonthlyData:
    def __init__(self, year, month, network):
        self.network = network
        self.fufilled = False
        self.year = year
        self.month = month

        # Find start and end dates for the month
        self.start_date = datetime(year, month, 1)
        _, last_day = calendar.monthrange(year, month)
        self.end_date = datetime(year, month, last_day, 23, 59, 59)

        # Cachable data
        self.total_scrobbles = 0
        self.top_artists = []
        self.top_albums = []
        self.top_tracks = []
        self.top_genres = []

    def cache_data(self):
        # Cache all data for the month
        print(f"Month {self.year}-{self.month} data caching......")
        self.cache_total_scrobbles()
        # print(f"Total scrobbles for {self.year}-{self.month}: {self.total_scrobbles}")
        time.sleep(0.1)  # buffer
        self.cache_top_artists()
        # print(f"Top artists for {self.year}-{self.month}: {self.top_artists}")
        time.sleep(0.1)  # buffer
        self.cache_top_albums()
        # print(f"Top albums for {self.year}-{self.month}: {self.top_albums}")
        time.sleep(0.1)  # buffer
        self.cache_top_tracks()
        # print(f"Top tracks for {self.year}-{self.month}: {self.top_tracks}")
        time.sleep(0.1)  # buffer        # print(f"Month {self.year}-{self.month} data caching......")

        self.cache_top_genres()
        # print(f"Top genres for {self.year}-{self.month}: {self.top_genres}")
        self.fufill()
        # Mark the data as fulfilled
        print(f"Month {self.year}-{self.month} data cached.")
        # Add the month to the all time data

    def cache_total_scrobbles(self):
        # Fetch and cache the total scrobbles for the month
        weekly_tracks = self.network.get_authenticated_user().get_weekly_track_charts(
            from_date=int(self.start_date.timestamp()), to_date=int(self.end_date.timestamp())
        )
        self.total_scrobbles = sum(track.weight for track in weekly_tracks)

    def cache_top_artists(self):
        # Fetch and cache the top artists for the month
        weekly_artists = self.network.get_authenticated_user().get_weekly_artist_charts(
            from_date=int(self.start_date.timestamp()), to_date=int(self.end_date.timestamp())
        )
        self.top_artists = [
            {"artist": artist.item.name, "playcount": artist.weight}
            for artist in weekly_artists[:TOP_LIMIT]  # Limit to TOP_LIMIT
        ]

    def cache_top_albums(self):
        # Fetch and cache the top albums for the month
        weekly_albums = self.network.get_authenticated_user().get_weekly_album_charts(
            from_date=int(self.start_date.timestamp()), to_date=int(self.end_date.timestamp())
        )
        self.top_albums = [
            {"album": album.item.title, "artist": album.item.artist.name, "playcount": album.weight}
            for album in weekly_albums[:TOP_LIMIT]  # Limit to TOP_LIMIT
        ]

    def cache_top_tracks(self):
        # Fetch and cache the top tracks for the month
        weekly_tracks = self.network.get_authenticated_user().get_weekly_track_charts(
            from_date=int(self.start_date.timestamp()), to_date=int(self.end_date.timestamp())
        )
        self.top_tracks = [
            {"track": track.item.title, "artist": track.item.artist.name, "playcount": track.weight}
            for track in weekly_tracks[:TOP_LIMIT]  # Limit to TOP_LIMIT
        ]
    
    def cache_top_genres(self):
            # Fetch and cache the top genres for the month
            genre_counts = {}
            for artist in self.top_artists[:TOP_LIMIT * 2]:  # Take double the top limit
                artist_obj = self.network.get_artist(artist["artist"])
                tags = artist_obj.get_top_tags()
                for tag in tags:
                    genre = tag.item.name.lower().replace("-", " ").strip()  # Normalize genre names
                    weight = int(tag.weight) if tag.weight.isdigit() else 0  # Convert weight to int
                    genre_counts[genre] = genre_counts.get(genre, 0) + weight

            # Sort genres by weight (popularity) and limit to TOP_LIMIT
            sorted_genres = sorted(genre_counts.items(), key=lambda x: x[1], reverse=True)[:TOP_LIMIT]
            self.top_genres = [{"genre": genre, "weight": weight} for genre, weight in sorted_genres]
    
    def print_cached_data(self):
        # Print out the cached data for the month
        print(f"Total plays for {self.year}-{self.month}: {self.total_scrobbles}")
        print(f"Top artists for {self.year}-{self.month}: {self.top_artists}")
        print(f"Top albums for {self.year}-{self.month}: {self.top_albums}")
        print(f"Top tracks for {self.year}-{self.month}: {self.top_tracks}")
        print(f"Top genres for {self.year}-{self.month}: {self.top_genres}")

    def fufill(self):
        # Mark the data as fulfilled
        self.fufilled = True

    def fufilled(self):
        return self.fufilled

    # Getters
    def get_month(self):
        return self.month
    
    def get_year(self):
        return self.year
    

# Yearly data object
class YearlyData:
    def __init__(self, year):
        self.year = year
        self.months = {}
    
    def add_month(self, month, data):
        self.months[month] = data
    
    def get_months(self):
        return self.months
    
    def get_year(self):
        return self.year
    
class AllTimeData:
    def __init__(self):
        self.months = {}
    
    def add_month(self, month, data):
        self.months[month] = data
    
    def get_months(self):
        return self.months
    
class TimeData:
    def __init__(self):
        pass
        
    
class Metadata:
    def __init__(self, network):
        self.track = track
        self.album = album
        self.artist = artist

