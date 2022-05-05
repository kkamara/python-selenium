from django.core.management.base import BaseCommand, CommandError

import os
import json

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Command(BaseCommand):
    help = 'help text'

    def handle(self, *args, **options):
        try:
            chrome_options = webdriver.ChromeOptions()
            # chrome_options.add_argument('--disable-extensions')
            chrome_options.add_argument('--disable-gpu')
            # chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--disable-blink-features=AutomationControlled')
            # chrome_options.add_argument('--user-agent='+userAgent)
            browser = webdriver.Remote(
                command_executor='http://localhost:4444',
                options=chrome_options,
            )
            browser.set_page_load_timeout(10)
            browser.implicitly_wait(10)
            browser.get('https://www.amazon.co.uk/')

            self.screenshot(browser, 'debug')

            if 'Type the characters you see in this image:' in browser.page_source:
                raise RuntimeError('We were detected.')

            el = browser.find_element(By.XPATH, '//input[contains(@id,"twotabsearchtextbox")]')
            el.send_keys('Samsung phones'+Keys.ENTER)

            if 'An error occurred while we tried to process your request:' in browser.page_source:
                raise RuntimeError('We were detected.')

            self.screenshot(browser, 'debug2')

            phoneNamesEl = browser.find_elements(By.XPATH, '//span[contains(@class, "a-size-base-plus a-color-base a-text-normal")]')
            priceWholeNumberEl = browser.find_elements(By.XPATH, '//span[contains(@class, "a-price-whole")]')
            priceDecimalNumberEl = browser.find_elements(By.XPATH, '//span[contains(@class, "a-price-fraction")]')
                        
            phones = []
            priceWholeNumbers = []
            priceDecimalNumbers = []

            for phone in phoneNamesEl:
                phones.append(phone.text)

            self.stdout.write(self.style.NOTICE(50 * '*'))

            for price in priceWholeNumberEl:
                priceWholeNumbers.append(price.text)

            for price in priceDecimalNumberEl:
                priceDecimalNumbers.append(price.text)

            finalList = json.dumps(list(map(self.combine, phones, priceWholeNumbers, priceDecimalNumbers)))
            self.stdout.write(self.style.NOTICE(finalList))

            browser.quit()
            self.stdout.write(self.style.SUCCESS('Success'))
        except Exception as e:
            browser.quit()
            raise CommandError(str(e))

    def screenshot(self, browser, name='example'):
        browser.save_screenshot(os.path.abspath(os.path.join(__file__, f'../../../../screenshots/{name}.png')))

    def combine (self, phone, wholeNumber, decimalNumber):
        return {'price': wholeNumber+'.'+decimalNumber, 'phone': phone}