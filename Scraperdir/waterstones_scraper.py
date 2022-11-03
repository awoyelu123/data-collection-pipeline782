from Scraperdir.transformer import Transformer
from .scraper import Scraper
from .loader import Loader
from .transformer import Transformer
import pandas as pd


class WaterstonesScraper(Scraper,Loader,Transformer):
    def __init__(self):
        Scraper.__init__(self)
        Loader.__init__(self)
        Transformer.__init__(self)

    def run_scraper(self):
        self.get_url_headless_mode()
        self.click_accept_cookies()
        self.nav_to_crime_books()
        self.create_list_of_product_links()
        self.create_dictionary_of_product_data()
        self.save_all_product_info_json_locally()
        self.save_all_images_locally()



        
    
if __name__ == '__main__':
    waterstones_scraper = WaterstonesScraper()
    waterstones_scraper.run_scraper