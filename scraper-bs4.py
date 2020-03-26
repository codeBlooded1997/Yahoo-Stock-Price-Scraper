from bs4 import BeautifulSoup
import requests
from twilio.rest import Client

URL = 'https://finance.yahoo.com/quote/FB?p=FB'
ideal_price = input('Ideal price : ')


def price_parser():
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    price = soup.findAll('div', {'class':'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
    return price

# Sending SMS
def send_message(message):
    account_sid = "AC81b4362f605c6398a48da412dcff6926"
    auth_token  = "84aa917ee50e1f59bf7c1d1264f7d1c3"
    client = Client(account_sid, auth_token)
    message = client.messages.create(
       to="+14387004763",
       from_="+16194326457",
       body="Price is : {}.".format(message)
    )

    print()
    print("A TEXT MASSAGE HAS BEEN SEND.")


while True:
    current_price = price_parser()
    print("The current price is : ", current_price)
    if current_price < ideal_price:
        send_message(current_price)
        break

print("Price is lower than the limit!")
