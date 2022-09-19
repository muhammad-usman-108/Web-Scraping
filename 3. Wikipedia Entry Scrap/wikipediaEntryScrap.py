"""
@author: muhammad-usman-108
"""

"""
Task: Wikipedia table scrap
Our next goal is going to be to scrap all the data from the yahoo finance for a list of 505 companies that are part of the S&P 500 index.
API end point: https://en.wikipedia.org/wiki/List_of_S%26P_500_companies
"""

import requests
from bs4 import BeautifulSoup

wikiUrl = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
endSymbol = "ZTS"

tickerSymbols = []
response = requests.get(wikiUrl)
pageText = response.text

soup = BeautifulSoup(pageText, features="html.parser")

tbody = soup.find_all("tbody")

print(tbody[0].contents[4].contents[1].text)

for i in range(len(tbody[0].contents)):
    if i<2:
        continue
    if i%2 != 0:
        continue

    symbols = tbody[0].contents[i].contents[1].text
    tickerSymbols.append(symbols.strip("\n"))
    if symbols == endSymbol:
        break

print(tickerSymbols)

