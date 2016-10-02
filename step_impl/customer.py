import time
from getgauge.python import step
from getgauge.python import DataStoreFactory, Messages
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from hamcrest import *
from step_impl.pages.signup_page import signup_as
from step_impl.api.MobileApp import MobileAppClient
from Browser import BrowserFactory

@step('Create customer account for <first_name> <last_name> with <email>')
def create_new_customer(firstname, lastname, email):
    driver = BrowserFactory.getWebdriver()
    DataStoreFactory.spec_data_store().put(email + '_driver', driver)

    signup_as(driver, firstname, lastname, email, password="passw0rd")

    msg = WebDriverWait(driver, 10).until(lambda driver: driver.find_element(By.CLASS_NAME, 'messages').text)
    assert_that(msg, any_of(contains_string("Thank you for registering"), contains_string("There is already an account with this email address")))

@step('Login from app as user <email>')
def get_token_for_user(email):
    appClient = MobileAppClient(email=email)
    DataStoreFactory.spec_data_store().put(email + '_app_client', appClient)
    appClient.request_token(password='passw0rd')

@step('Create a cart from app as user <email>')
def create_cart(email):
    appClient = DataStoreFactory.spec_data_store().get(email + '_app_client')
    appClient.create_cart()

@step('Add item with sku <sku> to cart from app as user <email>')
def add_cart_items(sku, email):
    appClient = DataStoreFactory.spec_data_store().get(email + '_app_client')
    appClient.add_item_to_cart(sku)

@step('Process and submit order for cart from app as user <email> with firstname=<firstname> lastname=<lastname> street=<street> city=<city> region=<region> postcode=<postcode> country=<country> telephone=<telephone>')
def process_cart(email, firstname, lastname, street, city, region, postcode, country, telephone):
    appClient = DataStoreFactory.spec_data_store().get(email + '_app_client')
    appClient.set_shipping_info(email, firstname, lastname, street, city, region, postcode, country, telephone)
    appClient.submit_cart_payment_info(email, firstname, lastname, street, city, region, postcode, country, telephone)

@step('User <email> closes browser')
def close(email):
    driver = DataStoreFactory.spec_data_store().get(email + '_driver')
    driver.quit()