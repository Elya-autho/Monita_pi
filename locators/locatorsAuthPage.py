from selenium.webdriver.common.by import By

class Login_page_locators:
    INPUT_PHONE = (By.XPATH, '//*[@class="login-phone-number"]')
    SEND_BUTTON_NEXT = (By.XPATH, '//*[@class="login-phone-next"]')
    INPUT_SMS_CODE = (By.XPATH, '//*[@id="app"]/div/input')
    SEND_BUTTON_NEXT_SMS_CODE = (By.XPATH, '//*[@class="login-sms-code"]')

    CLICK_LINK_SMS_CODE = (By.XPATH, '//*[@class ="login-sms-code-again-a"]')