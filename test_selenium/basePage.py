import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class TestMethod():
# common
  base_url="https://testerhome.com/"

# test_test01
  click01_loc = (By.CSS_SELECTOR,'.nav > li:nth-child(4) > a')
  click02_loc = (By.CSS_SELECTOR,'[data-name="霍格沃兹测试学院"]')
  click03_loc = (By.CSS_SELECTOR,'.topic:nth-child(1) .title a')
  click04_loc = (By.CSS_SELECTOR,'.title media-heading')
# test_test02
  click05_loc = (By.CSS_SELECTOR,'.topic-21805 .title > a')
  click06_loc = (By.CSS_SELECTOR,'[data-toggle="dropdown"]')
  click07_loc = (By.CSS_SELECTOR,'.toc-item:nth-child(4) > .toc-item-link')

  def setup_method(self):
    self.driver = webdriver.Chrome()
    self.driver.implicitly_wait(10)
    self.driver.maximize_window()

  def teardown_method(self):
    time.sleep(5)
    self.driver.quit()

  def wait(self,element):
    WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(element))

  def Find_element(self,*element):
    self.driver.find_element(*element).click()

  def GetUrl(self,url):
    self.driver.get(url)
