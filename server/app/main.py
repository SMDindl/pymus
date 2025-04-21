# Focus: User choice of API (Last.fm or Spotify)
import os

# Prompt the user to choose between Last.fm and Spotify.
def get_api_choice():
    
    print("Choose an API:")
    print("1. Last.fm")
    print("2. Spotify")
    choice = input("Enter 1 or 2: ")
    if choice == "1":
        return "lastfm"
    elif choice == "2":
        return "spotify"
    else:
        print("Invalid choice. Defaulting to Last.fm.")
        return "lastfm"
    
# Main func to run the script
def main():
    print(get_api_choice())

main()
