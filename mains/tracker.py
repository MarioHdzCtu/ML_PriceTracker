import requests
from bs4 import BeautifulSoup as bs
from dotenv import load_dotenv
import os
from mains.exceptions import StoreNotRegistered


load_dotenv(".env")

class Item():
    """
    Each of the items to track, uses link and store of the item to track the price and other information
    """
    def __init__(self, link: str, store: str):
        """Main method of Items class. Gets the raw html, name and price of the given link

        Args:
            link (str): _description_ 
            store (str): _description_
        """
        self.link = link
        self.store = store
        self.get_raw(self.link)
        self.get_name()
        self.get_price()
    
    def get_raw(self, link):
        """
        Gets the raw html document of the given page and converts to a BeautifulSoup (bs) object
        """
        self.raw = requests.request('GET', link).text
        self.soup = bs(self.raw,'html.parser')

    def get_name(self):
        """
        Gets the name of the given item
        """
        
        if self.store == 'ML':
            self.name = self.soup.find_all(os.getenv('ML_title_element'),{os.getenv('ML_identifier'):os.getenv('ML_title_tag')})[int(os.getenv('ML_title_iteration'))].text
        else:
            raise StoreNotRegistered(self.store)

    def get_price(self):
        """
        Gets the price of the given Item
        """
        if self.store == 'ML':
            self.price = int(self.soup.find_all(os.getenv('ML_price_element'),{os.getenv('ML_identifier'):os.getenv('ML_price_tag')})[int(os.getenv('ML_price_iteration'))].text.replace(',',''))


