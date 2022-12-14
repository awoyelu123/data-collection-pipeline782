import boto3
from botocore.client import Config
import json
import os
import pandas as pd
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from sqlalchemy import create_engine
from sqlalchemy import inspect
import time
import urllib.request
import chromedriver_autoinstaller


class WaterScraper():
    def __init__(self):
        self.link_list = []
        self.product_list =[]
        

    def geturl(self):
        '''Opens the waterstones webpage'''
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


    def nav_to_crime_books(self):
        '''Navigates to book where the desired product are found'''
        time.sleep(7)
        book_tab = self.driver.find_element(by = By.XPATH, value = "//*[@id='masthead']/div[3]/div/div/div/nav/div[1]/ul[1]/li[5]/a")
        book_tab.click()
        time.sleep(5)
        crime_page = self.driver.find_element(by = By.XPATH, value = '//*[@id="masthead"]/div[3]/div/div/div/nav/div[1]/ul[2]/li[2]/div/div[1]/div[2]/div/div/span/a').click()
        time.sleep(5)
        crime_books_page= self.driver.find_element(by = By.XPATH, value = '//*[@id="pagesmain"]/div/header[1]/a').click()


    def extend_webpage(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
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
    

    def extract_img_and_dwnld(self):
        '''Obtains image link and downloads image locally'''
        for product in self.link_list[:1]:
            self.driver.get(product)
            id = self.driver.find_element(by = By.XPATH, value = '/html/body/div[1]/div[2]/div[2]/section[2]/div[2]/div[1]/div[1]/p/i[2]/span').text
            img_link = self.driver.find_element(by = By.XPATH, value = '//*[@id="scope_book_image"]').get_attribute('src')
            filename = id + '.jpg'
            image_url = img_link
        urllib.request.urlretrieve(image_url,filename)
                

    def create_directory(self):
        '''Creates directory'''
        if not os.path.exists("C:\\Users\\awoye\\OneDrive\\Documents\\GitHub\\data-collection-pipeline782\\'raw_data'"):
            os.mkdir("\\'raw_data'")
        


    def load_data_to_json(self):
        '''Saves dictionary of product text data as a json file'''   
        os.chdir("\\'raw_data'")
        with open("\\'raw_data\\data.json'",'w') as f:
            json.dump(self.product_list,f) 


    def upload_raw_data(self):
        '''
        Uploads raw data to S3
        '''
        ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
        ACCESS_SECRET_KEY =os.environ['ACCESS_SECRET_KEY']
        BUCKET_NAME = 'waterstones-data'

        print("Loading data")

        data=open('data.json','rb')

        s3 = boto3.resource(
            's3',
            aws_access_key_id = ACCESS_KEY_ID,
            aws_secret_access_key = ACCESS_SECRET_KEY,
            config = Config(signature_version = 's3v4'))
        s3.Bucket(BUCKET_NAME).put_object(Key = 'data.json', Body = data)
        print("Data sent to S3!")
    

    def make_pandas_dataframe(self):
        '''Turns my data into a pandas dataframe'''
        self.df = pd.DataFrame(self.product_list)
    

    def load_to_sql(self):
        '''
        Loads dataframe into PostgresSQl
        '''
        print("Connecting to database")
        DATABASE_TYPE = 'postgresql'
        DBAPI = 'psycopg2'
        HOST = 'database-1.czkh6nyqipgc.eu-west-2.rds.amazonaws.com'
        USER = 'postgres'
        PASSWORD = 'password'
        DATABASE = 'postgres'
        PORT = 5432
        engine = create_engine(f"{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}")
        engine.connect()
        try:
            old_info = pd.read_sql_table('waterstones_data',con = engine)
            merged_data = pd.concat([old_info, self.df])
            new_data = merged_data.drop_duplicates(keep=False)
            new_data.to_sql('waterstones_data',engine,if_exists ='append', index = False)
        except Exception:
            self.df.to_sql('waterstones_data',engine,if_exists ='append', index = False)
        finally:
            old_info = pd.read_sql_table('waterstones_data',con = engine)
            merged_data = pd.concat([old_info, self.df])
            new_data = merged_data.drop_duplicates(keep=False)
            new_data.to_sql('waterstones_data',engine,if_exists ='append', index = False)
        print("Data Successfully loaded to PostgreSQL")

runscraper = WaterScraper()

if __name__ == '__main__':
    runscraper.get_url_headless_mode()
    runscraper.click_accept_cookies()
    runscraper.nav_to_crime_books()
    runscraper.extend_webpage()
    runscraper.create_list_of_product_links()
    runscraper.create_dictionary_of_product_data()
    runscraper.load_data_to_json()
    runscraper.upload_raw_data()

    

