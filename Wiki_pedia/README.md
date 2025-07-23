# Wikipedia Programming Languages Scraper

This project uses **Python**, **Requests**, and **BeautifulSoup** to scrape a list of programming languages from Wikipedia and save them into a CSV file.

## Features

- Scrapes all programming languages listed on [Wikipedia's List of Programming Languages](https://en.wikipedia.org/wiki/List_of_programming_languages)
- Cleans and writes each language as a separate row into a CSV file
- Outputs a UTF-8 encoded CSV for better compatibility

## Files

- `scraper.py` → the Python script (your code)
- `languagess.csv` → the output file containing the scraped languages
- `README.md` → this file

## How to Run

1. Make sure you have Python 3 installed.
2. Install required libraries:
   ```bash
   pip install requests beautifulsoup4
   ```
