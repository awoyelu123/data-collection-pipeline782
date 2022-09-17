import json
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import urllib
import time
import uuid


driver= webdriver.Chrome(executable_path="C:\\Users\\awoye\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.get("https://www.waterstones.com")
