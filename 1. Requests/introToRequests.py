"""
@author: muhammad-usman-108
"""

"""
Task: Extract the previous close value from yahoo finance
API end point: https://finance.yahoo.com/quote/AAPL?p=AAPL
"""

import requests

url = "https://finance.yahoo.com/quote/AAPL?p=AAPL"

response = requests.get(url)
print(response.status_code)

t = response.text
ind = t.index("Previous Close")
redText = t[ind:].split("</span>")[1].split("</td>")
val = redText[1].split("\">")[1]
print("The previous value is : ", val)
