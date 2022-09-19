# Web-Scraping
Web scraping in python: Practicing Udemy course

## Setup:
1. Download python : https://www.python.org/downloads/
2. Run the downloaded .exe file.

## Prerequisite Library:
1. requests: `pip install requests`
2. beautiful soup: `pip install beautifulsoup4`
3. selenium: `pip install selenium`
4. 

## External tools:
1. Chrome Web Driver: https://chromedriver.chromium.org/downloads


### Tasks:
1. Extract the previous close value from yahoo finance using `requests`.
API end point: `https://finance.yahoo.com/quote/AAPL?p=AAPL`

2. Extract the previous close value from yahoo finance using `beautiful soup 4`
API end point: `https://finance.yahoo.com/quote/AAPL?p=AAPL`

3. Extract all data in the table from Yahoo Finance
Now that you've see how we went about extracting the first value, see if you can extract all of the values contained within that table, starting at "Previous Close" and ending at "1y Target Est".

4. Wikipedia table scrap
Our next goal is going to be to scrap all the data from the yahoo finance for a list of 505 companies that are part of the S&P 500 index.
API end point: `https://en.wikipedia.org/wiki/List_of_S%26P_500_companies`
