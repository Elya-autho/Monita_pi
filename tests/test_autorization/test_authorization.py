from selenium import webdriver
import time
from locators.locatorsAuthPage import Login_page_locators
from base.db import get_code
from selenium.webdriver.common.by import By


#Вводим данные для авторизации

def test_authorizations(browser, base_url, user_phone):

    input_phone = browser.find_element(*Login_page_locators.INPUT_PHONE).send_keys(user_phone)
    time.sleep(2)
    send_next =  browser.find_element(*Login_page_locators.SEND_BUTTON_NEXT).click()
    time.sleep(2)
    input_code = browser.find_element(*Login_page_locators.INPUT_SMS_CODE).send_keys(get_code(10318))
    time.sleep(2)
    send_next_after_code = browser.find_element(*Login_page_locators.SEND_BUTTON_NEXT_SMS_CODE).click()
    time.sleep(12)
    browser.quit()

