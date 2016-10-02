import os
from selenium.webdriver.common.by import By
from getgauge.python import Messages
from step_impl.pages.Tasks import enter_text_into, click_on

## Screen:
_firstnameBox = (By.NAME, 'firstname')
_lastnameBox = (By.NAME, 'lastname')
_emailBox = (By.NAME, 'email')
_passwordBox = (By.NAME, 'password')
_passwordConfirmBox = (By.NAME, 'password_confirmation')
_submitButton = (By.CLASS_NAME, 'submit')

## Steps:
def signup_as(driver, firstname, lastname, email, password):
    _navigate_to_signup_page(driver)
    enter_text_into(driver, firstname, _firstnameBox)
    enter_text_into(driver, lastname, _lastnameBox)
    enter_text_into(driver, email, _emailBox)
    enter_text_into(driver, password, _passwordBox)
    enter_text_into(driver, password, _passwordConfirmBox)
    click_on(driver, _submitButton)

## Actions:
def _navigate_to_signup_page(driver):
    # Messages.write_message("Getting URL: {0}".format(self.URL))
    MAGENTO_URL = '{}/customer/account/create/'.format(os.getenv('MAGENTO_URL'))
    Messages.write_message('Navigation URL: {}'.format(MAGENTO_URL))
    driver.get(MAGENTO_URL)
