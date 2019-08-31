# Author : Shahriar Hashemi

import lxml
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

url = "http://www.tgju.org/"

ua = UserAgent()
header = {"user-agent": ua.chrome}

main_page = requests.get(url, headers = header)
soup = BeautifulSoup(main_page.content, "lxml")

dollar = soup.find("tr", attrs={"data-market-row":"price_dollar_rl"}).td.string
pound  = soup.find("tr", attrs={"data-market-row":"price_gbp"}).td.string
euro   = soup.find("tr", attrs={"data-market-row":"price_eur"}).td.string

"""
This Function removes all the commas in the string 
and then converts the string to an integer.
example : 11,200 -> 11200
"""
def remove_commas(num_with_commas):
    fixed_number = num_with_commas.replace(",", "")
    return fixed_number 

dollar  = remove_commas(dollar)
pound   = remove_commas(pound)
euro    = remove_commas(euro)

print(dollar)
print(pound)
print(euro)