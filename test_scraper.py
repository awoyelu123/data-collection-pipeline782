import unittest
from water_scraper_mile_4 import WaterScraper

#class TestCreateDictionaryOfProductData(unittest.TestCase): 

    

class TestLinkList(unittest.TestCase): 


    def test1(self):
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
 #def test2():
    #def test2():
        #pass
#class TestCreateLinksOfProductLinks(unittest.TestCase):
#make sure first link matches 


unittest.main()

if __name__ == '__main__':
    unittest.main()
