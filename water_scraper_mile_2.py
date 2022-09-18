import json
from mimetypes import init
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import urllib
import time
import uuid


class WaterScraper():
    def __init__(self):
        self.link_list = []
        self.product_list =[]

    def geturl(self):
        self.driver = webdriver.Chrome("C:\\Users\\awoye\\Downloads\\chromedriver_win32\\chromedriver.exe")
        self.driver.get("https://www.waterstones.com/")
        

    def click_accept_cookies(self):
        time.sleep(8)
        button = self.driver.find_element(by = By.XPATH, value = '//*[@id="onetrust-accept-btn-handler"]')
        button.click()

    def nav_to_crime_books(self):
        time.sleep(7)
        book_tab = self.driver.find_element(by = By.XPATH, value = "//*[@id='masthead']/div[3]/div/div/div/nav/div[1]/ul[1]/li[5]/a")
        book_tab.click()
        time.sleep(5)
        crime_page = self.driver.find_element(by = By.XPATH, value = '//*[@id="masthead"]/div[3]/div/div/div/nav/div[1]/ul[2]/li[2]/div/div[1]/div[2]/div/div/span/a').click()
        time.sleep(5)
        crime_books_page= self.driver.find_element(by = By.XPATH, value = '//*[@id="pagesmain"]/div/header[1]/a').click()

    def scroll_up(self):        
        self.driver.execute_script("window.scroll(0, 0);")
        time.sleep(5)
            
    def scroll_down(self):
        time.sleep(5)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def extract_product_links(self):
        time.sleep(5)
        container = self.driver.find_element(by = By.XPATH, value = '/html/body/div[1]/div[1]/div[3]/div[2]')
        link_container = container.find_elements(by = By.CLASS_NAME, value = 'title-wrap')

        for book in link_container:
            book_link = book.find_element(by = By.TAG_NAME, value = 'a').get_attribute('href')
            self.link_list.append(book_link)
            
            
        print(self.link_list)

    def extract_and_load_dict(self):
            for product in self.link_list[:3]:
                self.driver.get(product)
                book_title = self.driver.find_element(by = By.CLASS_NAME, value = 'book-title').text
                author = self.driver.find_element(by = By.XPATH, value = '/html/body/div[1]/div[1]/div[2]/section[1]/div[2]/div[1]/span/a/b/span').text
                price = float(self.driver.find_element(by = By.XPATH, value = '/html/body/div[1]/div[1]/div[2]/section[1]/div[2]/div[2]/div/div/div/div[1]/div/b[2]').text[1:])
                pages = int(self.driver.find_element(by = By.XPATH, value = '/html/body/div[1]/div[1]/div[2]/section[1]/div[2]/div[2]/div/div/div/div[2]/span[2]/span').text )
                ISBN = self.driver.find_element(by = By.XPATH, value = '/html/body/div[1]/div[1]/div[2]/section[2]/div[2]/div[1]/div[1]/p/i[2]/span').text 
                product_img_link = self.driver.find_element(by = By.XPATH, value = '//*[@id="scope_book_image"]').get_attribute('src')
            
                product_details ={
                'UUID': uuid.uuid4(),
                'ISBN': ISBN,
                'book_title':book_title,
                'author':author,
                'price': price,
                'pages': pages,
                'product_img_link':product_img_link
                }
                self.product_list.append(product_details)
            print(self.product_list)



runscraper = WaterScraper()

if __name__ == '__main__':
    runscraper.geturl()
    runscraper.click_accept_cookies()
    runscraper.nav_to_crime_books()
    runscraper.scroll_down()
    runscraper.scroll_up()
    runscraper.extract_product_links()
    runscraper.extract_and_load_dict()