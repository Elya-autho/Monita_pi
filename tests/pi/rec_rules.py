from selenium import webdriver
import time
from locators.locatorsPiRecRul import PiRecRulesPage, PiRecRulesCreate
from base.db import get_code
from selenium.webdriver.common.by import By


def test_open_page_rec_rules(browser, url_rec_rules):


