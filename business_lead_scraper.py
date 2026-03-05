import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://news.ycombinator.com"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

titles = []
links = []

for item in soup.select(".titleline a"):
    titles.append(item.text)
    links.append(item["href"])

data = {
    "Business/Article": titles,
    "Website": links
}

df = pd.DataFrame(data)

df.to_excel("business_leads.xlsx", index=False)

print("Leads saved to business_leads.xlsx")