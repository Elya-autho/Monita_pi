from selenium import webdriver
import time
import pytest
from locators.locatorsPiRecRul import PiRecRulesPage, PiRecRulesCreate
from base.db import get_code
from selenium.webdriver.common.by import By
from  conftest import  browser, authorized_browser, base_url, user_phone
from conftest_py import url_rec_rules



def test_open_page_rec_rules(browser, authorized_browser,user_phone, url_rec_rules):
    browser.get(url_rec_rules)
    time.sleep(5)
    assert "#rec_rules" in browser.current_url
