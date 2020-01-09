def test_test01(self):
  self.GetUrl(self.base_url)
  self.Find_element(*self.click01_loc)
  self.wait(self.click02_loc)
  self.Find_element(*self.click02_loc)
  self.Find_element(*self.click03_loc)