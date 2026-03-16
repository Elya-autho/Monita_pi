from selenium.webdriver.common.by import By


class PiRecRulesPage:
    INPUT_NAME_PRODUCT = (By.CLASS_NAME, 'rr-filter-input rr-filter-name')
    INPUT_ID_PRODUCT = (By.CLASS_NAME, 'rr-filter-input rr-filter-code')
    SELECT_STRATEGY = (By.CLASS_NAME,'rr-filter-span rr-filter-strategy')
    SELECT_MANAGER_RESPONSIBLE = (By.CLASS_NAME,'rr-filter-span rr-filter-manager')
    SELECT_MANAGER_CATEGORY = (By.CLASS_NAME, 'rr-filter-span rr-filter-category-manager')
    SELECT_CATEGORY_PRODUCT = (By.CLASS_NAME, 'rr-filter-span rr-filter-category')
    SELECT_CATEGORY_STATUS = (By.CLASS_NAME, 'rr-filter-span rr-filter-status')
    SELECT_AUTOMATIZATION =(By.CLASS_NAME, 'rr-filter-span rr-filter-automatization')
    CLICK_BUTTON_SHOW = (By.CLASS_NAME, 'button button--lightGreen rr-filter-show')
    CLICK_BUTTON_CLEAR = (By.CLASS_NAME, 'button button--blue rr-filter-clean')




class PiRecRulesCreate:
    CLICK_ADD_STRATEGY = (By.CLASS_NAME, 'button button--blue rr-strategy-add')



