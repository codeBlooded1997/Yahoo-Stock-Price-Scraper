from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, time
from random import randint
import datetime
import pandas as pd



# Path to chrome driver.
# Edit before running.
path_to_chromedriver = 'PATH TO CHROME DRIVER'
# Opening driver.
driver = webdriver.Chrome(executable_path=path_to_chromedriver)
# Simulating human browsing.
sleep(randint(8, 10))
# grabbing
URL = "https://finance.yahoo.com/"
print("Grabbing website")
# Grabbing url.
driver.get(URL)
# Maximizing window.
driver.maximize_window()
# Getting input from user.
company_name = input('COMPANY NAME : ')
duration = int(input("DURATION OF DATA EXTRACTION (seconds): "))
sleep(randint(8, 10))
# inserting input data into search bar

search_bar = driver.find_element_by_xpath('//*[@id="header-search-form"]/input')
search_bar.send_keys(company_name)
# Simulating human browsing.
sleep(randint(3, 5))
# Sending keys
search_bar.send_keys(Keys.RETURN)


def price_parser():
    """
    This function scrapes price and 
    return the price as a text.
    """
    price_xp = '//*[@id="quote-header-info"]/div[3]/div[1]/div/span[1]'
    price = driver.find_element_by_xpath(price_xp)
    return price.text

def name_parser():
    """
    This function scrapes name and
    retus the price as a text.
    """
    name_xp = '//*[@id="quote-header-info"]/div[2]/div[1]/div[1]/h1'
    name = driver.find_element_by_xpath(name_xp)
    return name.text

def currency_parser():
    """
    This function scrapes currency and
    returs the currency as a text.
    """
    currency_xp = '//*[@id="quote-header-info"]/div[2]/div[1]/div[2]/span'
    obj = driver.find_element_by_xpath(currency_xp)
    # currency = obj.text.split('. ')[-1]
    currency = obj.text
    return currency

def growth_factor_parser():
    """
    This function scrapes coefficient and
    returs the coefficient as a text.
    """
    coefficient_xp = '//*[@id="quote-header-info"]/div[3]/div[1]/div/span[2]'
    coefficient = driver.find_element_by_xpath(coefficient_xp)
    return coefficient.text


price_list = []
name_list = []
time_list = []
currency_list = []
growth_factors = []
timeout = time() + 60 * (duration / 60)  # seconds

print("SCRAPING DATA...")
# scraping 5 times...
while True:
    test = 0
    if test == 5 or time() > timeout:
        break
    else:
        price_list.append(price_parser())
        name_list.append(name_parser())
        time_list.append(datetime.datetime.now())
        currency_list.append(currency_parser())
        growth_factors.append(growth_factor_parser())

    test = test - 1

print("Done!")
# Creating dataframe.
result = pd.DataFrame(
    {
        "NAME": name_list,
        "PRICE": price_list,
        "GROWTH FACTOR": growth_factors,
        "CURRENCY": currency_list,
        "TIME": time_list,

    })
print(result)
