from bs4 import BeautifulSoup
import requests

link = requests.get("https://www.bmkg.go.id/cuaca/prakiraan-cuaca/32")
link.raise_for_status()

soup = BeautifulSoup(link.text, 'html.parser')
# print(soup.prettify)

print(soup.select('<th scope="col" class="bg-[#F8FAFC] sticky left-0 px-3 lg:px-5 py-[19px] text-left text-sm leading-[22px] md:text-base md:leading-[25px] font-bold text-gray-primary rounded-l-lg"> Kab. / Kota </th>'))
