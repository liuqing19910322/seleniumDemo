import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestDefaultSuite():
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.vars = {}

    def teardown_method(self):
        pass
        # self.driver.quit()

    def test_searchtest(self):
        self.driver.get("https://testerhome.com/")
        self.driver.find_element(By.CSS_SELECTOR, '#main-nav-menu > ul > li:nth-child(4) > a').click()
        self.driver.find_element(By.CSS_SELECTOR, '#hot_teams > div.panel-body > div > div:nth-child(1) > div > div.media-body > div.media-heading > a').click()
        self.driver.find_element(By.CSS_SELECTOR, '#main > div > div.col-md-8 > div > div.panel-body > div.topic.media.topic-21848 > div.infos.media-body > div.title.media-heading > a').click()
