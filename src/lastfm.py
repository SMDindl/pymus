# Focus: pylast
import pylast
import os

# Load environment variables from .env file
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

# User credentials for Last.fm from .env file
USERNAME = os.getenv("US") 
PASSWORD_HASH = pylast.md5(os.getenv("PW")) 

# Initialize the Last.fm network with user authentication
network = pylast.LastFMNetwork(
    api_key=API_KEY,
    api_secret=API_SECRET,
    username=USERNAME,
    password_hash=PASSWORD_HASH,
)

# Get the authenticated user
user = network.get_authenticated_user()

# Print out the username
if user:
    print(f"Authenticated as: {user.get_name()}")
else:
    print("Failed to authenticate user.")
