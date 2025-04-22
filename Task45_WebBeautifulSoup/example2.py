# Before scrapping a website go to the website plus /robot.txt
# It will tell what you can and what you cannot do when scrapping it.
# Normally is limited to do not overload the website

from bs4 import BeautifulSoup
import requests

# To know how to scrap a website it is needed to inspect the website
response = requests.get("https://news.ycombinator.com/news")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
print(soup.title)

articles = soup.find_all(name="a", class_="storylink")
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

#article_upvote = [score.getText() for score in soup.find(name="span", class_="score").getText()]

print(article_texts)
print(article_links)
#print(article_upvote)
