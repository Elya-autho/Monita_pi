from selenium import webdriver
import time
from selenium.webdriver.common.by import By

URL = "https://test.kb-monita.ru/"

browser = webdriver.Chrome()
browser.get(URL)
time.sleep(2)

