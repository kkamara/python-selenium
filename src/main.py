import argparse
import os

from selenium import webdriver

STORAGE_PATH = f'{os.getcwd()}/storage'

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--bar', help='Do the bar option')
    parser.add_argument('--foo', help='Foo the program')
    return parser.parse_args()

def run():
    args = parse_args()
    print(args)
    browser = webdriver.Firefox()
    browser.get('http://seleniumhq.org/')
    browser.save_screenshot(f'{STORAGE_PATH}/test.jpg')
    browser.quit
    print('success')

if __name__ == '__main__':
    run()
