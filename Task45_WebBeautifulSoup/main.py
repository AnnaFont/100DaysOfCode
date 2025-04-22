# Before scrapping a website go to the website plus /robot.txt
# It will tell what you can and what you cannot do when scrapping it.
# Normally is limited to do not overload the website

from bs4 import BeautifulSoup
import requests

# To know how to scrap a website it is needed to inspect the website
response = requests.get(
    'https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/')

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
print(soup.title)

all_anchor_tags = soup.find_all(name="h3", class_="title")
title_text = []

for title_tag in all_anchor_tags:
    text = title_tag.getText()
    title_text.append(text)

title_text = title_text[::-1]

with open("movies.txt", mode="w") as file:
    for title in title_text:
        file.write(f"{title}\n")

