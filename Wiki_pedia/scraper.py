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

response = requests.get(url="https://en.wikipedia.org/wiki/List_of_programming_languages", headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

languages = soup.find_all("div", class_="div-col")

with open("languagess.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Language"]) 

    for language in languages:
        language_single = language.ul.get_text().split("\n")  
        for lang in language_single:
            if lang.strip():  
                writer.writerow([lang.strip()])

