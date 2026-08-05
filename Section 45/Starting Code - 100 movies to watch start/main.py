import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
response.raise_for_status()

response.encoding = "utf-8"
content = response.text

soup = BeautifulSoup(content, "html.parser")

movies = soup.select(".article-title-description__text > .title")
movies = [movie.text for movie in movies]
movies.reverse()

with open("movies.txt", "w", encoding="utf-8") as file:
    for movie in movies:
        file.write(f"{movie}\n")
