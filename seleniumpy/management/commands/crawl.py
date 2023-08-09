from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

import os
import json
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Command(BaseCommand):
    help = 'help text'

    def handle(self, *args, **options):
        try:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--disable-extensions')
            chrome_options.add_argument('--disable-gpu')
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--disable-blink-features=AutomationControlled')
            userAgent = 'Mozilla/5.0 (BB10; Touch) AppleWebKit/537.1+ (KHTML, like Gecko) Version/10.0.0.1337 Mobile Safari/537.1+'
            chrome_options.add_argument('--user-agent='+userAgent)
            # Uncomment next line to remove GUI.
            if settings.SELENIUM_HEADLESS == True:
                chrome_options.add_argument('--headless')
            browser = webdriver.Chrome(options=chrome_options)
            
            browser.get('https://www.kelvinkamara.com')

            self.screenshot(browser, 'debug')

            if 'Thisisnotinpagesource.' in browser.page_source:
                raise RuntimeError('We were detected.')            
            time.sleep(1)

            browser.find_element(By.XPATH, "//a[@id='contact-me-link']").click()
            
            el = browser.find_element(By.XPATH, "//input[@id='name']")
            el.send_keys('gdpr'+Keys.ENTER)
            
            time.sleep(60)

            browser.quit()
            self.stdout.write(self.style.SUCCESS('Success'))
        except Exception as e:
            try:
                browser.quit()
            except:
                pass
            raise CommandError(str(e))

    def screenshot(self, browser, name='example'):
        browser.save_screenshot(f'./screenshots/{name}.png')
