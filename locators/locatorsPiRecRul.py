from selenium.webdriver.common.by import By


class PiRecRules:
    INPUT_NAME_PRODUCT = (By.CLASS_NAME, 'rr-filter-input rr-filter-name')
    INPUT_ID_PRODUCT = (By.CLASS_NAME, 'rr-filter-input rr-filter-code')
    SELECT_STRATEGY = (By.CLASS_NAME,'rr-filter-span rr-filter-strategy')
