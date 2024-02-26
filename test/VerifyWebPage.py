from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.delete_all_cookies()
time.sleep(5)

class QaPlayground:
    # URL
    URL = 'https://qaplayground.dev/'

    # Initializer
    def __init__(self, browser):
        self.browser = browser

    # Print Header
    def print_header(self):
        print("Header is present")

    # Interaction Methods
    def load(self):
        self.print_header()
        self.browser.get(self.URL)

# Example usage:
qa_playground = QaPlayground(driver)
qa_playground.load()
