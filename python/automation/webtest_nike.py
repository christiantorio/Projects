import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class WebSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="chromedriver")

    def test_search(self):
        print("Testing search feature...")
        driver = self.driver
        driver.get("http://www.nike.org")
        self.assertIn("Nike", driver.title)
        elem = driver.find_element_by_id("VisualSearchInput")
        elem.send_keys("Air Force 1")
        elem.send_keys(Keys.RETURN)
        driver.back()
    
    def test_element(self):
        print("Testing how to find elements")
        driver = self.driver
        driver.get("http://www.nike.org")
        signin = driver.find_element_by_class_name("hf_title_sigin_membership")
        self.assertIn("Sign In", driver.signin)
        
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()