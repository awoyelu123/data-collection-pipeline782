import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
import time
from Scraperdir.scraper import Scraper

class TestScraper(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:\\Users\\awoye\\Downloads\\chromedriver_win32 (2)\\chromedriver.exe")
        
    def test_try_to_find_cookies(self):
        self.driver.get("https://www.waterstones.com")
        element_1 = self.driver.find_element(by = By.XPATH, value = '//*[@id="onetrust-accept-btn-handler"]')
        
    def test_LinkList(self):

        self.link_list = []


        self.driver.get("https://www.waterstones.com/category/crime-thrillers-mystery/page/1")
        time.sleep(8)
        button = self.driver.find_element(by = By.XPATH, value = '//*[@id="onetrust-accept-btn-handler"]')
        button.click()
        container = self.driver.find_element(by = By.XPATH, value = '/html/body/div[1]/div[2]/div[3]/div[2]')
        link_container = container.find_elements(by = By.CLASS_NAME, value = 'title-wrap')

        for book in link_container:
            book_link = book.find_element(by = By.TAG_NAME, value = 'a').get_attribute('href')
            self.link_list.append(book_link)
        print(str(type(self.link_list)))
        self.assertEqual(str(type(self.link_list)),"<class 'list'>")

    def test_geturl(self):
        driver = driver = webdriver.Chrome("C:\\Users\\awoye\\Downloads\\chromedriver_win32 (2)\\chromedriver.exe")
        driver.get("https://www.waterstones.com")
        self.assertEqual(driver.title,'Buy books, stationery and gifts, online and in store | Waterstones')

    def test_create_dictionary_of_product_data(self):
        self.get_url_headless_mode()
        self.click_accept_cookies()
        self.nav_to_crime_books()
        self.create_list_of_product_links()

        # TODO 2 test that shows that product details dictionary is a dictionary
        
        #TODO 3 Make sure that pages type is an integer

        #TODO 4 Make sure that price is an integer

        #TODO Expect that product img link gives back a picture ending in jpg/png
if __name__ == '__main__':
    unittest.main()