import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="chromedriver")

    def test_search(self):
        driver = self.driver
        driver.get("http://www.nike.org")
        self.assertIn("Nike", driver.title)
        elem = driver.find_element_by_id("VisualSearchInput")
        elem.send_keys("Air Force 1")
        elem.send_keys(Keys.RETURN)
        self.assertIn("Nike", driver.title)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()