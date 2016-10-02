from getgauge.python import step
from getgauge.python import DataStoreFactory, Messages
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from hamcrest import *
from step_impl.pages.admin.login_page import login
from step_impl.pages.admin.orders_page import navigate_to_orders_page_with_id
from Browser import BrowserFactory

@step('Login as Admin')
def login_as_admin():
    driver = BrowserFactory.getWebdriver()
    DataStoreFactory.spec_data_store().put('admin_driver', driver)

    login(driver)
    assert_that(driver.title, contains_string("Dashboard"))

@step('Check order exists for user <email>')
def check_order_exists(email):
    appClient = DataStoreFactory.spec_data_store().get(email + '_app_client')
    order_id = appClient.get_order_id()
    driver = DataStoreFactory.spec_data_store().get('admin_driver')
    navigate_to_orders_page_with_id(driver, order_id)

    order_block = WebDriverWait(driver, 10).until(lambda driver: driver.find_element(By.CLASS_NAME, 'order-view-account-information').text)
    assert_that(order_block, contains_string("Order & Account Information"))

@step('Verify order contains item with sku <sku>')
def check_order_contains_item_with_sku(sku):
    driver = DataStoreFactory.spec_data_store().get('admin_driver')
    sku_block = WebDriverWait(driver, 10).until(lambda driver: driver.find_element(By.CLASS_NAME, 'product-sku-block').text)
    assert_that(sku_block, contains_string(sku))


