import requests
from bs4 import BeautifulSoup
import csv

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Connection": "keep-alive",
}

with open("hackernews_posts.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Title", "Link", "Points", "Author"]) 

    for page in range(1, 31):  
        url = f"https://news.ycombinator.com/news?p={page}"
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        posts = soup.find_all("span", class_="titleline")
        sublines = soup.find_all("span", class_="subline")

        for post, subline in zip(posts, sublines):
            title = post.a.get_text(strip=True)
            link = post.a["href"]

            points_tag = subline.find("span", class_="score")
            points = points_tag.get_text(strip=True) if points_tag else "0 points"

            author_tag = subline.find("a", href=lambda x: x and x.startswith("user?id="))
            author = author_tag.get_text(strip=True) if author_tag else "unknown"

            writer.writerow([title, link, points, author])

print("Saved data to hackernews_posts.csv")
