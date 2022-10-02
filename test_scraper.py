import unittest
from water_scraper_mile_4 import WaterScraper


    

class TestLinkList(unittest.TestCase): 

    
    def testLinkList(self):
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        import time
        self.link_list = []

        driver = webdriver.Chrome("C:\\Users\\awoye\\Downloads\\chromedriver_win32\\chromedriver.exe")
        driver.get("https://www.waterstones.com/category/crime-thrillers-mystery/page/1")
        time.sleep(8)
        button = driver.find_element(by = By.XPATH, value = '//*[@id="onetrust-accept-btn-handler"]')
        button.click()
        container = driver.find_element(by = By.XPATH, value = '/html/body/div[1]/div[1]/div[3]/div[2]')
        link_container = container.find_elements(by = By.CLASS_NAME, value = 'title-wrap')
        for book in link_container:
            book_link = book.find_element(by = By.TAG_NAME, value = 'a').get_attribute('href')
            self.link_list.append(book_link)
            print(self.link_list)
            print(type(self.link_list))
            
        self.assertEqual(self.link_list[0],'https://www.waterstones.com/book/the-bullet-that-missed/richard-osman/2928377088439')
        self.assertEqual(str(type(self.link_list)),"<class 'list'>")
    

    def testDictList(self):
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        import time

        self.link_list = []
        self.product_list = []

        driver = webdriver.Chrome("C:\\Users\\awoye\\Downloads\\chromedriver_win32\\chromedriver.exe")
        driver.get("https://www.waterstones.com/category/crime-thrillers-mystery/page/1")
        time.sleep(8)
        button = driver.find_element(by = By.XPATH, value = '//*[@id="onetrust-accept-btn-handler"]')
        button.click()
        container = driver.find_element(by = By.XPATH, value = '/html/body/div[1]/div[1]/div[3]/div[2]')
        link_container = container.find_elements(by = By.CLASS_NAME, value = 'title-wrap')
        for book in link_container:
            book_link = book.find_element(by = By.TAG_NAME, value = 'a').get_attribute('href')
            self.link_list.append(book_link)

        for product in self.link_list[:1]:
            driver.get(product)
        
            product_details ={
            'isbn': driver.find_element(by = By.XPATH, value = '/html/body/div[1]/div[1]/div[2]/section[2]/div[2]/div[1]/div[1]/p/i[2]/span').text,
            'book_title':driver.find_element(by = By.CLASS_NAME, value = 'book-title').text,
            'author':driver.find_element(by = By.XPATH, value = '/html/body/div[1]/div[1]/div[2]/section[1]/div[2]/div[1]/span/a/b/span').text,
            'price': float(driver.find_element(by = By.XPATH, value = '/html/body/div[1]/div[1]/div[2]/section[1]/div[2]/div[2]/div/div/div/div[1]/div/b[2]').text[1:]),
            'pages': int(driver.find_element(by = By.XPATH, value = '/html/body/div[1]/div[1]/div[2]/section[1]/div[2]/div[2]/div/div/div/div[2]/span[2]/span').text),
            'product_img_link':driver.find_element(by = By.XPATH, value = '//*[@id="scope_book_image"]').get_attribute('src')
            }
            self.product_list.append(product_details)

        self.assertEqual(self.product_list[0]['isbn'],'2928377088439')
        
    def testDirectoryExists(self):
        import os
        self.assertTrue(os.path.exists("C:\\Users\\awoye\\OneDrive\\Documents\\GitHub\\data-collection-pipeline782//raw_data"))



 
 
 #def test2():
    #def test2():
        #pass
#class TestCreateLinksOfProductLinks(unittest.TestCase):
#make sure first link matches 




if __name__ == '__main__':
    unittest.main()
