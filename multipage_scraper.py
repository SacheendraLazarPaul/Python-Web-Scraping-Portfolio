import requests
from bs4 import BeautifulSoup

base_url = "https://news.ycombinator.com/news?p="

for page in range(1,4):

    url = base_url + str(page)

    response = requests.get(url)
    soup = BeautifulSoup(response.text,"html.parser")

    titles = soup.select(".titleline")

    for t in titles:
        print(t.text)