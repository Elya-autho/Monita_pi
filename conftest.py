import time
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators.locatorsAuthPage import Login_page_locators
from base.db import get_code




@pytest.fixture
def browser(base_url):
    driver = webdriver.Chrome()
    driver.get(base_url)
    yield driver

    driver.quit()

@pytest.fixture
def base_url():
    return "https://test.kb-monita.ru/"


PHONE = 9085728301
@pytest.fixture
def user_phone():

    return PHONE

# 1. ФИКСТУРА АВТОРИЗАЦИИ (выполняется один раз перед тестами)
@pytest.fixture(scope="function")
def authorized_browser(browser, base_url, user_phone):
    # Открываем базовую страницу (если требуется)
    browser.get(base_url)
    time.sleep(2)
    # Ввод телефона
    browser.find_element(*Login_page_locators.INPUT_PHONE).send_keys(PHONE)
    time.sleep(2)
    # Клик "Далее"
    browser.find_element(*Login_page_locators.SEND_BUTTON_NEXT).click()
    time.sleep(2)
    # Ожидаем появления поля ввода СМС-кода (вместо time.sleep)
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(Login_page_locators.INPUT_SMS_CODE)
    )
    time.sleep(2)
    # Ввод СМС-кода
    browser.find_element(*Login_page_locators.INPUT_SMS_CODE).send_keys(get_code(10318))
    time.sleep(2)
    # Клик "Далее" после ввода кода
    browser.find_element(*Login_page_locators.SEND_BUTTON_NEXT_SMS_CODE).click()
    time.sleep(2)
    # Ждем завершения анимации входа и появления главного элемента интерфейса (например, меню или профиля)
    # Замените 'YOUR_DASHBOARD_ELEMENT_LOCATOR' на локатор элемента, который виден только авторизованному юзеру
   #

    return browser
