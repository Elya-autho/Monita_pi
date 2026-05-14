import time
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators.locatorsAuthPage import Login_page_locators
from base.db import get_code

# 1. ФИКСТУРА АВТОРИЗАЦИИ (выполняется один раз перед тестами)
@pytest.fixture(scope="function")
def authorized_browser(browser, base_url, user_phone):
    # Открываем базовую страницу (если требуется)
    browser.get(base_url)

    # Ввод телефона
    browser.find_element(*Login_page_locators.INPUT_PHONE).send_keys(user_phone)

    # Клик "Далее"
    browser.find_element(*Login_page_locators.SEND_BUTTON_NEXT).click()

    # Ожидаем появления поля ввода СМС-кода (вместо time.sleep)
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(Login_page_locators.INPUT_SMS_CODE)
    )

    # Ввод СМС-кода
    browser.find_element(*Login_page_locators.INPUT_SMS_CODE).send_keys(get_code(10318))

    # Клик "Далее" после ввода кода
    browser.find_element(*Login_page_locators.SEND_BUTTON_NEXT_SMS_CODE).click()

    # Ждем завершения анимации входа и появления главного элемента интерфейса (например, меню или профиля)
    # Замените 'YOUR_DASHBOARD_ELEMENT_LOCATOR' на локатор элемента, который виден только авторизованному юзеру
    WebDriverWait(browser, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "YOUR_DASHBOARD_ELEMENT_LOCATOR"))
    )

    return browser
