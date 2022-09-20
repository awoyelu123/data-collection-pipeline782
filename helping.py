from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import urllib
import time


driver = webdriver.Chrome("C:\\Users\\awoye\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.get("https://www.prodirectrugby.com//")

time.sleep(8)
button = driver.find_element(by = By.XPATH, value = '//*[@id="hide-cookie-message"]')
button.click()
