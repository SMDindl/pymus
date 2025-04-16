# Focus: pylast
import pylast
from dotenv import load_dotenv
import os

import calendar
import datetime as dt
import user_cache 

accessed_dates_dict = {} # Store dates by year-month (e.g. 2023-10)

# Initializes the Last.fm network with user authentication
def setup_lastfm():
    # Load environment variables from .env file
    load_dotenv()

    # Collect variables from environment
    api_key = os.getenv("API_KEY")
    api_secret = os.getenv("API_SECRET")
    username = os.getenv("US")
    password_hash = pylast.md5(os.getenv("PW"))

    # Initialize the Last.fm network with user authentication
    network = pylast.LastFMNetwork(
        api_key=api_key,
        api_secret=api_secret,
        username=username,
        password_hash=password_hash
    )

    # Explicitly delete sensitive data from memory
    del api_key, api_secret, username, password_hash

    # Return network object
    return network
# End of setup_lastfm function

# Initializes the Last.fm network with user authentication (taking in params)
def setup_lastfm_params(username, password):
    # Load environment variables from .env file
    load_dotenv()
    
    # Initialize the Last.fm network with user authentication
    network = pylast.LastFMNetwork(
        api_key = os.getenv("API_KEY"),
        api_secret= os.getenv("API_SECRET"),
        username = username,
        password_hash=pylast.md5(password),
    )

    # Explicitly delete sensitive data from memory
    del username, password

    # Get the authenticated user
    user = network.get_authenticated_user()

    # Return network object
    return network
# End of setup_lastfm function

def print_lastfm_user(network):
    # Get the authenticated user
    user = network.get_authenticated_user()

    # Print out the username
    if user:
        print(f"Authenticated as: {user.get_name()}")
        return user
    else:
        print("Failed to authenticate user.")
        return None
# End of print_lastfm_user function

# Main function to run the script
def main():
    # Setup Last.fm network
    network = setup_lastfm()

    # Print out the authenticated user
    user = print_lastfm_user(network)

    # Check if user is authenticated
    if user is None:
        return
    
    # Use user_cache to ultize user data
    cache = user_cache.UserCache(network)

    # Print out the username and the number of months and years since the user registered
    cache.print_data()

    jan_2022_data = user_cache.MonthlyData(year=2022, month=1, network=network)

    jan_2022_data.cache_data()

    jan_2022_data.print_cached_data()



    # Get list of each month and year since the user registered
    # dates = cache.get_months_since_registered_dict()

    # # # Print out the keys and their corresponding data
    # # print("Dates since registration:")
    # # for date, data in dates.items():
    # #     print("[ " + str(date) + " ], [ " + str(data) + " ]")

    # # Get weekly album charts
    # print("Weekly Album Charts:")
    # for album in user.get_weekly_album_charts():
    #     print(f"Album: {album.get_name()} by {album.get_artist().get_name()}")
    #     print(f"Playcount: {album.get_playcount()}")
    #     print(f"URL: {album.get_url()}")

    # # Get weekly track charts
    # chart_dates = user.get_weekly_chart_dates()
    # with open("log.txt", "w") as file:
    #     for start, end in chart_dates:
    #         file.write(start + "\n")
    #         file.write(end + "\n")


    # top_artists = user.get_weekly_artist_charts(from_date=start, to_date=end)
    # for artist in top_artists:
    #     print(f"Artist: {artist.item.name}, Playcount: {artist.weight}")
    

    




    



# End of main function

# Run the main function
if __name__ == "__main__":
    main()
# End of execution


