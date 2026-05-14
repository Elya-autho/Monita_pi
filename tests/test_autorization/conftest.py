import pytest
from selenium import webdriver
from faker import Faker
from selenium.webdriver.support.wait import WebDriverWait

fake = Faker('ru')


PHONE = 9085728301

@pytest.fixture
def browser(base_url):

    driver = webdriver.Chrome()
    driver.get(base_url)
    yield driver

    driver.quit()

@pytest.fixture
def base_url():
    return "https://test.kb-monita.ru/"

@pytest.fixture
def user_phone():
    return PHONE