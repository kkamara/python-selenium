import logging
import random
import time

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "help text"

    def handle(self, *args, **options):
        """
        The Selenium Python Documentation:
            https://www.selenium.dev/documentation/
        """
        browser = None
        try:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--disable-extensions")
            chrome_options.add_argument("--disable-gpu")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-blink-features=AutomationControlled")
            user_agent = self.get_random_user_agent()
            logger.info(f"Using User Agent : {user_agent}")
            chrome_options.add_argument(f"--user-agent={user_agent}")
            # Use SELENIUM_HEADLESS in .env to remove GUI.
            if settings.SELENIUM_HEADLESS or "testing" == settings.APP_ENV:
                chrome_options.add_argument("--headless")
            if "testing" == settings.APP_ENV:
                chrome_options.add_argument("--disable-dev-shm-usage")
                browser = webdriver.Chrome(options=chrome_options)
            else:
                browser = webdriver.Remote(
                    command_executor="http://127.0.0.1:4444/wd/hub",
                    options=chrome_options,
                )

            browser.get("https://www.kelvinkamara.com")

            self.screenshot(browser, name="debug")

            if "Thisisnotinpagesource." in browser.page_source:
                raise RuntimeError("We were detected.")
            time.sleep(1)

            browser.find_element(By.XPATH, "//a[@id='contact-me-link']").click()

            time.sleep(2)

            browser.quit()
            self.stdout.write(self.style.SUCCESS("Success"))
        except (RuntimeError, TimeoutError, TypeError, ValueError, WebDriverException) as e:
            if browser is not None:
                try:
                    browser.quit()
                except WebDriverException:
                    logger.exception("Failed to close the browser during cleanup")
            raise CommandError(str(e))

    def screenshot(self, browser, el=None, name="example"):
        browser.save_screenshot(f"./screenshots/{name}.png")
        if el:
            el_text = browser.execute_script("return arguments[0].innerText", el)
            logger.info(el_text)

    def get_random_user_agent(self):
        user_agents = [
            "Mozilla/5.0 (BB10; Touch) AppleWebKit/537.1+ (KHTML, like Gecko) Version/10.0.0.1337 Mobile Safari/537.1+",
            "Mozilla/5.0 (PlayBook; U; RIM Tablet OS 2.1.0; en-US) AppleWebKit/536.2+ (KHTML, like Gecko) Version/7.2.1.0 Safari/536.2+",
            "Mozilla/5.0 (BlackBerry; U; BlackBerry 9900; en-US) AppleWebKit/534.11+ (KHTML, like Gecko) Version/7.0.0.187 Mobile Safari/534.11+",
        ]
        key = random.randint(0, 2)
        return user_agents[key]
