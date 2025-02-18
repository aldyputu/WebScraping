import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Web_scraping"
headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"}

resp = requests.get(url, headers=headers)
print(resp.status_code)
# print(resp.text)

soup = BeautifulSoup(resp.text, 'html.parser')

titleText = open('titleWiki.txt', 'w')

titleText.write(soup.title.string)

titleText.close()





