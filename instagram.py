# Import the necessary libraries
import os
import requests
from instaloader import Instaloader, Profile

# Define the Instagram username
username = "usedsoil"

def get_latest_post_timestamp(username):
    # Create an instance of Instaloader
    loader = Instaloader()

    # Load the profile of the Instagram account
    profile = Profile.from_username(loader.context, username)

    # Get the latest post (don't think there is a better way to do this)
    for post in profile.get_posts():
        latest_post = post
        break

    # Get the timestamp of the latest post
    timestamp = latest_post.date_utc.timestamp()

    return int(timestamp)


def Download_all_photos(username):
    # Create an instance of Instaloader
    loader = Instaloader()

    # Load the profile of the Instagram account
    profile = Profile.from_username(loader.context, username)

    # Create a directory to save the downloaded photos
    os.makedirs(username, exist_ok=True)

    # Iterate over the posts of the profile
    for post in profile.get_posts():
        # Iterate over the photos in the post
        for index, photo in enumerate(post.get_sidecar_nodes()):
            # Get the URL of the photo
            url = photo.display_url

            # Download the photo
            response = requests.get(url)
            if response.status_code == 200:
                # Save the photo to the directory
                with open(f"{username}/{post.date_utc.strftime('%Y-%m-%d_%H-%M-%S')}_{index}.jpg", "wb") as f:
                    f.write(response.content)
                print(f"Downloaded photo: {post.date_utc.strftime('%Y-%m-%d_%H-%M-%S')}_{index}.jpg")

    print("All photos downloaded successfully!")


if __name__ == "__main__":
    # Get the latest post timestamp
    timestamp = get_latest_post_timestamp(username)
    print(f"Latest post timestamp: {timestamp}")

    # Download all the photos
    #Download_all_photos(username)
