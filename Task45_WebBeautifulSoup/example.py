from bs4 import BeautifulSoup

with open("website.html") as file:
    contents = file.read()

# Sort the contents as html (it could be also for a xml file)
soup = BeautifulSoup(contents, "html_parser")

all_anchor_tags = soup.find_all(name="a")

for tag in all_anchor_tags:
    print(tag.getText())
    print(tag.get("href"))

heading = soup.find(name="h1", id="name")

