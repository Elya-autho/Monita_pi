from selenium import webdriver
import time
from locators.locatorsAuthPage import Login_page_locators
from base.db import get_code
from selenium.webdriver.common.by import By

URL = "https://test.kb-monita.ru/"
PHONE = 9085728301

#Открываем страницу
# browser = webdriver.Chrome()
# browser.get(URL)
# time.sleep(5)
#
# browser.quit()

#Вводим данные для авторизации

browser = webdriver.Chrome()
browser.get(URL)
time.sleep(5)
input_phone = browser.find_element(*Login_page_locators.INPUT_PHONE).send_keys(PHONE)
time.sleep(2)
send_next =  browser.find_element(*Login_page_locators.SEND_BUTTON_NEXT).click()
time.sleep(2)
input_code = browser.find_element(*Login_page_locators.INPUT_SMS_CODE).send_keys(get_code(10318))
time.sleep(12)
send_next_after_code = browser.find_element(*Login_page_locators.SEND_BUTTON_NEXT_SMS_CODE).click()
time.sleep(12)
browser.quit()


