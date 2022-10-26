from .scraper import Scraper
from .loader import Loader
import pandas as pd
import os
import math

class WaterstonesScraper(Scraper,Loader):
    def __init__(self):
        Scraper.__init__(self)
        Loader.__init__(self)

    def run_scraper(self):
        self.get_url_headless_mode()
        self.click_accept_cookies()
        self.nav_to_crime_books()
        self.create_list_of_product_links()
        self.create_dictionary_of_product_data()
        self.create_directory()
        self.load_data_to_json()



        
    
if __name__ == '__main__':
    waterstones_scraper = WaterstonesScraper()
    waterstones_scraper.run_scraper