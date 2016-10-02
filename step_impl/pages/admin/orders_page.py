import os
from getgauge.python import Messages

## Actions:
def navigate_to_orders_page(driver):
    # Messages.write_message("Getting URL: {0}".format(self.URL))
    MAGENTO_URL = '{}/admin/sales/order'.format(os.getenv('MAGENTO_URL'))
    Messages.write_message('Navigation URL: {}'.format(MAGENTO_URL))
    driver.get(MAGENTO_URL)

def navigate_to_orders_page_with_id(driver, id):
    # Messages.write_message("Getting URL: {0}".format(self.URL))
    MAGENTO_URL = '{}/admin/sales/order/view/order_id/{}/'.format(os.getenv('MAGENTO_URL'), id)
    Messages.write_message('Navigation URL: {}'.format(MAGENTO_URL))
    driver.get(MAGENTO_URL)
