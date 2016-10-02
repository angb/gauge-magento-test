import os
from selenium.webdriver.common.by import By
from getgauge.python import Messages
from step_impl.pages.Tasks import enter_text_into, click_on

## Screen:
_usernameBox = (By.ID, 'username')
_passwordBox = (By.ID, 'login')
_submitButton = (By.CLASS_NAME, 'action-login')

## Steps:
def login(driver, username="admin", password="admin123"):
    _navigate_to_login_page(driver)
    enter_text_into(driver, username, _usernameBox)
    enter_text_into(driver, password, _passwordBox)
    click_on(driver, _submitButton)

## Actions:
def _navigate_to_login_page(driver):
    # Messages.write_message("Getting URL: {0}".format(self.URL))
    MAGENTO_URL = '{}/admin/'.format(os.getenv('MAGENTO_URL'))
    Messages.write_message('Navigation URL: {}'.format(MAGENTO_URL))
    driver.get(MAGENTO_URL)
