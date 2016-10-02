from selenium import webdriver

class BrowserFactory(object):
    def getWebdriver():
        driver = webdriver.Chrome(service_args=['--ignore-ssl-errors=true'])
        driver.set_window_size(1124, 850)
        driver.implicitly_wait(30)  # seconds
        return driver

    def quit(driver):
        driver.quit()
