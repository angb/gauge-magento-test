import os

def enter_text_into(driver, text, selector):
    driver.find_element(*selector).clear()
    driver.find_element(*selector).send_keys(text)

def click_on(driver, selector):
    driver.find_element(*selector).click()