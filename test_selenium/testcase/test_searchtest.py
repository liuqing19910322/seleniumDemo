import pytest
from selenium import webdriver


class TestDefaultSuite():
    def setup_method(self,method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self,method):
        self.driver.quit()

    def test_search(self):
        self.driver.get('https://www.testerhome.com/')
        self.driver.set_window_size(1440, 877)
        self.driver.click()

