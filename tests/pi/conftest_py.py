import pytest
from selenium import webdriver
from faker import Faker
from selenium.webdriver.support.wait import WebDriverWait
from base.urls import pi_rec_rules
fake = Faker('ru')




@pytest.fixture
def browser(base_url):

    driver = webdriver.Chrome()
    driver.get(base_url)
    yield driver

    driver.quit()

@pytest.fixture
def url_rec_rules():
    return 'https://test.kb-monita.ru/#rec_rules'

