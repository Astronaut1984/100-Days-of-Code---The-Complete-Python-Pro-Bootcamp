from bs4 import BeautifulSoup
import requests
import os
from ytmusicapi import YTMusic

web_headers = {
    # Type your user agent here
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:153.0) Gecko/20100101 Firefox/153.0"
}

if not "browser.json" in os.listdir("./"):
    print("browser.json not found")
    print("You need to authenticate with YouTube Music first.")
    print("Run one of these commands in your terminal from this project folder:\n")
    print("  Mac:     pbpaste | ytmusicapi browser")
    print("  Windows: ytmusicapi browser\n")
    print("Copy the request headers from Firefox first.")
    print("This will create browser.json.")
    exit()

year = input(
    "Which year do you want to travel to? Type the data in this format YYYY-MM-DD: "
)

response = requests.get(
    url=f"https://appbrewery.github.io/bakeboard-hot-100/{year}",
    headers=web_headers,
)
if response.status_code == 404:
    print("Year not found :(")
    exit
response.raise_for_status()

response.encoding = "utf-8"

content = response.text

soup = BeautifulSoup(content, "html.parser")

titles = [title.text for title in soup.select(".chart-entry__title")]
artists = [artist.text for artist in soup.select(".chart-entry__artist")]

try:
    yt = YTMusic("browser.json")
except Exception as e:
    print(f"Invalid browser.json content: {e}")
    exit()
playlist_title = f"{year} Billboard 100"

playlists = [playlist.get("title") for playlist in yt.get_library_playlists()]
if playlist_title in playlists:
    print("playlist already created...")
    exit
else:
    playlist_id = yt.create_playlist(
        title=playlist_title,
        description="A playlist made as a part of 100 days of code's Section 46, really cool",
    )
    print("playlist created")

for i, title, artist in zip(range(len(titles)), titles, artists):
    try:
        search_results = yt.search(f"{title} {artist}", filter="songs")
        song = search_results[0]
        print(f"{i+1}.{song['title']}")
        yt.add_playlist_items(playlist_id, [song["videoId"]])
    except IndexError:
        print(f"No results for: {title} — skipping.")
        continue
    except KeyError as e:
        print(f"Missing field {e} in result for: {title} — skipping.")
        continue
    except Exception as e:
        print(f"Error adding {title}: {e} — skipping.")
        continue
