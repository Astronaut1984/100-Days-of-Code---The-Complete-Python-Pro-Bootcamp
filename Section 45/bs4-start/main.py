from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
webpage = response.text
soup = BeautifulSoup(webpage, "html.parser")

titles = soup.select(".titleline > a")
scores = soup.select(".subtext .subline .score")

links = [title.get("href") for title in titles]
titles = [title.text for title in titles]
scores = [int(score.get_text().split()[0]) for score in scores]

idx = scores.index(max(scores))
print("Winner:")
print(f"{titles[idx]} | {links[idx]}\n{scores[idx]}")
