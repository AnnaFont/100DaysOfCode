from bs4 import BeautifulSoup
import requests
import spotipy

travel_time = input("What year you would like to travel to in YYY-MM-DD format?")

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

URL = "https://www.billboard.com/charts/hot-100/" + travel_time + "/"

CLIENT_ID = "b251b192b1a64cd6b4d4eba5dbdf7739"

SECRET_KEY = "9754ba62420548f58e0cbc70f17bd41d"

print(f"Travelling to {URL}")

# To know how to scrap a website it is needed to inspect the website
response = requests.get(URL, headers=header)

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
print(soup.title.getText())

# Extract all the music from selected date
all_anchor_tags = soup.select("li ul li h3")
title_text = [tag.getText().strip() for tag in all_anchor_tags]
print(title_text)

# Spotify Authentication
sp = spotipy.Spotify(
        auth_manager=spotipy.SpotifyOAuth(
            scope="playlist-modify-private",
            redirect_uri="http://127.0.0.1:8000/callback",
            client_id=CLIENT_ID,
            client_secret=SECRET_KEY,
            show_dialog=True,
            cache_path="token.txt"
        )
)
user_id = sp.current_user()["id"]
print(user_id)


# Searching Spotify for songs by title
song_uris = []
year = travel_time.split("-")[0]
for song in title_text:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{travel_time} Billboard 100", public=False)
print(playlist)

# Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)