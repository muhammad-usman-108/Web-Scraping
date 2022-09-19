"""
@author: muhammad-usman-108
"""

"""
Task: Extract the previous close value from yahoo finance
API end point: https://finance.yahoo.com/quote/AAPL?p=AAPL
"""

import requests
from bs4 import BeautifulSoup

url = "https://finance.yahoo.com/quote/AAPL?p=AAPL"

response = requests.get(url)
text = response.text

soup = BeautifulSoup(text, features="html.parser")

#trs = soup.find_all("tr", class_="")
trs = soup.find_all("tr")

#print(trs[0].find("td", attrs={"data-test":"PREV_CLOSE-value"}))

for td in trs[0].contents:
    print(td.text)
