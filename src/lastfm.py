# Focus: pylast
import pylast
from dotenv import load_dotenv 
import os

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

    # Get the authenticated user and print the username
    user = network.get_authenticated_user()
    if user:
        print(f"Authenticated as: {user.get_name()}")
    else:
        print("Failed to authenticate user.")

    # Return the network object
    return network

# initializes the Last.fm network with user authentication (taking in params)
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
    # Print out the username
    if user:
        print(f"Authenticated as: {user.get_name()}")
    else:
        print("Failed to authenticate user.")
    # Return network
    return network

# Run the setup function
setup_lastfm()


