"""
@author: muhammad-usman-108
"""

"""
Task: Extract all data in the table from yahoo finance
API end point: https://finance.yahoo.com/quote/AAPL?p=AAPL
"""

import requests
from bs4 import BeautifulSoup

url = "https://finance.yahoo.com/quote/AAPL?p=AAPL"
finalName = "1y Target Est"

response = requests.get(url)
text = response.text

soup = BeautifulSoup(text, features="html.parser")

trs = soup.find_all("tr")

nameVal = {}
for i in range(0, len(trs)):
    name = trs[i].contents[0].text
    value = trs[i].contents[1].text
    nameVal[name] = value

    if name == finalName:
        break

print(nameVal)
