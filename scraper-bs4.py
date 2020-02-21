from bs4 import BeautifulSoup
import requests

URL = 'https://finance.yahoo.com/quote/FB?p=FB'

def price_parser():
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    price = soup.findAll('div', {'class':'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
    return price
while True:
    print("The current price is : ", price_parser())
