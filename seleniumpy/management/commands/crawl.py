from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

import os
import json
import time
import logging

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Command(BaseCommand):
    help = 'help text'

    def handle(self, *args, **options):
        '''
        The Selenium Python Documentation:
            https://www.selenium.dev/documentation/
        '''
        try:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--disable-extensions')
            chrome_options.add_argument('--disable-gpu')
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--disable-blink-features=AutomationControlled')
            userAgent = 'Mozilla/5.0 (BB10; Touch) AppleWebKit/537.1+ (KHTML, like Gecko) Version/10.0.0.1337 Mobile Safari/537.1+'
            chrome_options.add_argument('--user-agent='+userAgent)
            # Use SELENIUM_HEADLESS in .env to remove GUI.
            if settings.SELENIUM_HEADLESS == True or settings.APP_ENV == 'testing':
                chrome_options.add_argument('--headless')
            if settings.APP_ENV == 'testing':
                chrome_options.add_argument('--disable-dev-shm-usage')
            browser = webdriver.Chrome(options=chrome_options)
            
            browser.get('https://www.kelvinkamara.com')

            self.screenshot(browser, name='debug')

            if 'Thisisnotinpagesource.' in browser.page_source:
                raise RuntimeError('We were detected.')            
            time.sleep(1)

            browser.find_element(
                By.XPATH, "//a[@id='contact-me-link']").click()

            el = browser.find_element(
                By.XPATH, "//a[@href='tel:+447956694595'][2]")
            self.screenshot(browser, el=el, name='number')
            el.click()
            
            time.sleep(1)

            browser.quit()
            self.stdout.write(self.style.SUCCESS('Success'))
        except Exception as e:
            try:
                browser.quit()
            except:
                pass
            raise CommandError(str(e))

    def screenshot(self, browser, el=None, name='example'):
        browser.save_screenshot(f'./screenshots/{name}.png')
        if el:
            test = browser.execute_script('return arguments[0].innerText', el)
            logging.info(test)
