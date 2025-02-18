import requests
from bs4 import BeautifulSoup
import sys
import webbrowser

#searchpypi.py - Opens several search results.
print('Searching...')
res = requests.get('https://google.com/search?q=' 'https://pypi.org/search/?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()  

#retrieve top search from the link
soup =  BeautifulSoup(res.text, 'html.parser')
#open browser
linkElems = soup.select('.package-snippet')
numOpen = min(5, len(linkElems))

for i in range(numOpen):
    urlToOpen = 'https://pypi.org' + linkElems[i].get('href')
    print('Opening', urlToOpen)
    webbrowser.open(urlToOpen)

