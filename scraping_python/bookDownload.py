import requests

#make request to the link with 
res = requests.get("https://automatetheboringstuff.com/files/rj.txt")
print(res.status_code)
#write the text to the text document
playText = open('RomeoAndJuliet.txt', 'wb')
#iterate the whole text and write on the text file
for text in res.iter_content(1000000):
    playText.write(text)
#afteropen the file, we need to close it
playText.close()
