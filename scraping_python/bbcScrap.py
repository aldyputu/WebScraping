import requests
from bs4 import BeautifulSoup

URL = "https://www.bbc.com/news"
headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"}

resp = requests.get(URL, headers=headers)
print(resp.status_code)
# print(resp.text)

soup = BeautifulSoup(resp.text, "html.parser")

newsBBC =  []
headline =  soup.find_all("h2", class_= "sc-8ea7699c-3 dhclWg")
category = soup.find_all("span", class_="sc-6fba5bd4-2 bHkTZK")
 

for  news in newsBBC:
    print(news)

