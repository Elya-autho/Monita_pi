import pytest
from selenium import webdriver
from faker import Faker
from selenium.webdriver.support.wait import WebDriverWait
from base.urls import pi_rec_rules
fake = Faker('ru')


@pytest.fixture
def url_rec_rules():
    return 'https://test.kb-monita.ru/#rec_rules'

