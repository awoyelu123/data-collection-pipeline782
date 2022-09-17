import json
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
        
    def open_waterstones(self):
        url = "https://www.waterstones.com"
        self.driver= webdriver.Chrome(executable_path="C:\\Users\\awoye\\Downloads\\chromedriver_win32\\chromedriver.exe")
        self.driver.get("https://www.waterstones.com")

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
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def extract_product_links(self):
        container = self.driver.find_element(by = By.XPATH, value = '/html/body/div[1]/div[1]/div[3]/div[2]')
        container = container.find_elements(by = By.CLASS_NAME, value = 'title-wrap')


        for book in container:
            book_link = book.find_element(by = By.TAG_NAME, value = 'a').get_attribute('href')
            self.link_list.append(book_link)
            
            
        print(self.link_list)



