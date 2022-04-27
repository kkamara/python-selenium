import argparse
import os
import json

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

STORAGE_PATH = f'{os.getcwd()}/screenshots'

def screenshot(browser, name='example'):
    browser.save_screenshot(f'{STORAGE_PATH}/{name}.png')

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--bar', help='Do the bar option')
    parser.add_argument('--foo', help='Foo the program')
    return parser.parse_args()

def run():
    args = parse_args()
    print(args)
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    # chrome_options.add_argument('--user-agent='+userAgent)
    browser = webdriver.Remote(
        command_executor='http://localhost:4000/wd/hub',
        options=chrome_options
    )
    browser.get('https://www.amazon.co.uk/')
    screenshot(browser, 'debug')
    el = browser.find_element(By.XPATH, '//input[contains(@id,"twotabsearchtextbox")]')
    el.send_keys('Samsung phones'+Keys.ENTER)

    phoneNamesEl = browser.find_elements(By.XPATH, '//span[contains(@class, "a-size-base-plus a-color-base a-text-normal")]')
    priceWholeNumberEl = browser.find_elements(By.XPATH, '//span[contains(@class, "a-price-whole")]')
    priceDecimalNumberEl = browser.find_elements(By.XPATH, '//span[contains(@class, "a-price-fraction")]')
    
    phones = []
    priceWholeNumbers = []
    priceDecimalNumbers = []

    for phone in phoneNamesEl:
        phones.append(phone.text)

    print(50 * '*')

    for price in priceWholeNumberEl:
        priceWholeNumbers.append(price.text)

    for price in priceDecimalNumberEl:
        priceDecimalNumbers.append(price.text)

    finalList = json.dumps(list(map(combine, phones, priceWholeNumbers, priceDecimalNumbers)))
    print(finalList)

    browser.quit()
    print('success')

def combine (phone, wholeNumber, decimalNumber):
    return {'price': wholeNumber+'.'+decimalNumber, 'phone': phone}

if __name__ == '__main__':
    run()
