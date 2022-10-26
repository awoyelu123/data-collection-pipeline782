from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
import time

class Scraper():
    def __init__(self):
        self.link_list = []
        self.product_list =[]


    def geturl(self):
        '''Opens the waterstones webpage'''
        print("Opening url")
        self.driver = webdriver.Chrome("C:\\Users\\awoye\\Downloads\\chromedriver_win32 (2)\\chromedriver.exe")
        self.driver.get("https://www.waterstones.com/")
    
    def get_url_headless_mode(self):

        options= Options()
        options.add_argument('--headless')
        options.add_argument('window-size=1903x961')
        options.add_argument("--no-sandbox") 
        options.add_argument("--headless")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-setuid-sandbox") 
        options.add_argument('--disable-gpu')
        chrome_prefs = {}
        options.experimental_options["prefs"] = chrome_prefs
        chrome_prefs["profile.default_content_settings"] = {"images": 2}
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
        options.add_argument(f'user-agent={user_agent}')
        self.driver = webdriver.Chrome(chrome_options=options)
        self.driver.get("https://www.waterstones.com/")
        print ("Headless Chrome Initialized on Windows OS")





    def click_accept_cookies(self):
        '''Waits for accept cookies pop up and then clicks it when it becomes available'''
        time.sleep(10)
        button = self.driver.find_element(by = By.XPATH, value = '//*[@id="onetrust-accept-btn-handler"]')
        button.click()
        print("Cookie clicked successfully")


    def nav_to_crime_books(self):
        '''Navigates to book where the desired product are found'''
        time.sleep(7)
        book_tab = self.driver.find_element(by = By.XPATH, value = "//*[@id='masthead']/div[3]/div/div/div/nav/div[1]/ul[1]/li[5]/a")
        book_tab.click()
        time.sleep(5)
        crime_page = self.driver.find_element(by = By.XPATH, value = '//*[@id="masthead"]/div[3]/div/div/div/nav/div[1]/ul[2]/li[2]/div/div[1]/div[2]/div/div/span/a').click()
        time.sleep(5)
        self.driver.find_element(by = By.XPATH, value = '//*[@id="pagesmain"]/div/header[1]/a').click()


    def extend_webpage(self):
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")



    def scroll_up(self):       
        '''scrolls to top of page''' 
        self.driver.execute_script("window.scroll(0, 0);")
        time.sleep(5)
            

    def scroll_down(self):
        '''Scrolls to the bottom of the page'''
        time.sleep(5)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


    def create_list_of_product_links(self):
        '''Extracts the product links and appends them to a list'''
        time.sleep(5)
        container = self.driver.find_element(by = By.XPATH, value = '/html/body/div[1]/div[2]/div[3]/div[2]')
        link_container = container.find_elements(by = By.CLASS_NAME, value = 'title-wrap')

        for book in link_container:
            book_link = book.find_element(by = By.TAG_NAME, value = 'a').get_attribute('href')
            self.link_list.append(book_link)
        print(self.link_list)
        return self.link_list
            
    def create_dictionary_of_product_data(self):
        '''Extracts all relavent data and loads it into a dictionary'''
        for product in self.link_list:
            self.driver.get(product)
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
                self.product_list.append(product_details)
        print(self.product_list)
        return self.product_list

