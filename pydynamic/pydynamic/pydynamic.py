import requests
from bs4 import BeautifulSoup
import pandas as pd
from io import StringIO

class pyDynamic(object):

    def __init__(self):
        self._url_luminus = "https://my.luminusbusiness.be/market-info/nl/dynamic-prices/"
        
    def getLuminusDayPrices(self):
        response = requests.get(self._url_luminus)
        html_content = response.content
        soup = BeautifulSoup(html_content, "html.parser")
        table = soup.find("table")
        if table:
            df = pd.read_html(StringIO(str(table)))[0]
        else:
            return None
        
        return df