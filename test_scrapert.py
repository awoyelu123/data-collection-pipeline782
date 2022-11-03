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

class TestScraper(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("C:\\Users\\awoye\\Downloads\\chromedriver_win32 (2)\\chromedriver.exe")
        
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
        self.driver.get("https://www.waterstones.com")
        self.assertEqual(self.driver.title,'Buy books, stationery and gifts, online and in store | Waterstones')

    def test_try_to_find_cookies(self):
        self.driver.get("https://www.waterstones.com")
        element_1 = self.driver.find_element(by = By.XPATH, value = '//*[@id="onetrust-accept-btn-handler"]').tag_name
        self.assertEqual(element_1,'button')
    
    def test_dictionary(self):
        self.driver.get("https://www.waterstones.com/book/the-bullet-that-missed/richard-osman/2928377088439")

        try:
            pages = int(self.driver.find_element(by = By.XPATH, value = '/html/body/div[1]/div[2]/div[2]/section[1]/div[2]/div[2]/div/div/div/div[2]/span[2]/span').text)
        except Exception:
            pages = None
        try:
            price = float(self.driver.find_element(by = By.XPATH, value = '/html/body/div[1]/div[2]/div[2]/section[1]/div[2]/div[2]/div/div/div/div[1]/div/b[2]').text[1:])
        except Exception:
            try: 
                price = float(self.driver.find_element(by = By.XPATH, value = '/html/body/div[1]/div[2]/div[2]/section[1]/div[2]/div[2]/div/div/div/div[1]/div/b').text[1:])
            except Exception:
                        price = None
        finally:
            product_details ={
            'isbn': self.driver.find_element(by = By.XPATH, value = '/html/body/div[1]/div[2]/div[2]/section[2]/div[2]/div[1]/div[1]/p/i[2]/span').text,
            'book_title':self.driver.find_element(by = By.CLASS_NAME, value = 'book-title').text,
            'author':self.driver.find_element(by = By.XPATH, value = '/html/body/div[1]/div[2]/div[2]/section[1]/div[2]/div[1]/span/a/b/span').text,
            'price': price,
            'pages': pages,
            'product_img_link':self.driver.find_element(by = By.XPATH, value = '//*[@id="scope_book_image"]').get_attribute('src')
        }

        # TODO 2 test that shows that product details dictionary is a dictionary
        
        #TODO 3 Make sure that pages type is an integer

        #TODO 4 Make sure that price is an integer

        #TODO 5 with pytest raises ____Error .Expect an error when click accept cookies does not wait

        #TODO Expect that product img link gives back a picture ending in jpg/png

if __name__ == '__main__':
    unittest.main()