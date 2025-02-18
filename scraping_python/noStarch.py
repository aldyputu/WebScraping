#program to get information from weather forecast website
#using beautifulsoup we will parse the html

from bs4 import BeautifulSoup
import requests

#set up connection for the link resource first
link = requests.get("https://nostarch.com")
link.raise_for_status()
#lets parse the html here
noStarchSoup = BeautifulSoup(link.text, "html.parser")
#write the whole hmtl for testing
#print(noStarchSoup) 
# print(type(noStarchSoup))

# print(noStarchSoup.select('div'))
# print(noStarchSoup.select('#author'))
print(noStarchSoup.select('.notice'))





