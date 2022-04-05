import argparse
import os

from selenium import webdriver

STORAGE_PATH = f'{os.getcwd()}/storage'

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
    browser = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',
        options=chrome_options
    )
    browser.get('http://seleniumhq.org/')
    screenshot(browser, 'test')
    browser.implicitly_wait(5)
    browser.quit
    print('success')

if __name__ == '__main__':
    run()
