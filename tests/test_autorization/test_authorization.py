import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from conftest import browser,base_url,authorized_browser, user_phone
#Вводим данные для авторизации

def test_user_authorizations(authorized_browser,browser,user_phone):
   driver =authorized_browser
   # 1. ОТКРЫТИЕ СТРАНИЦЫ ПОСЛЕ АВТОРИЗАЦИИ
   target_url = "https://kb-monita.ru"
   driver.get(target_url)

