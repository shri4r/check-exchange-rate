import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from lxml import etree

url = "http://www.tgju.org/"

ua = UserAgent()
header = {"user-agent": ua.chrome}

parser = etree.HTMLParser()  # Create an HTML parser object

main_page = requests.get(url, headers=header)
soup = BeautifulSoup(main_page.content, "lxml", parser=parser)

dollar: str = soup.find("tr", attrs={"data-market-row": "price_dollar_rl"}).td.string
pound: str = soup.find("tr", attrs={"data-market-row": "price_gbp"}).td.string
euro: str = soup.find("tr", attrs={"data-market-row": "price_eur"}).td.string


def remove_commas(num_with_commas: str) -> int:
    """
    This function takes a string, removes the commas, and then converts it to an integer.

    Parameters:
    - num_with_commas (str): The string containing the number with commas.

    Returns:
    - int: The integer value of the number without commas.

    Example:
    >>> remove_commas("610,000")
    610000
    """
    fixed_number = int(num_with_commas.replace(",", ""))
    return fixed_number


if __name__ == "__main__":
    print(remove_commas(dollar))
    print(remove_commas(pound))
    print(remove_commas(euro))
