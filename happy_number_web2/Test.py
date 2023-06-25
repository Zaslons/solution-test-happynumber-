import warnings
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest

warnings.filterwarnings("ignore", category=ResourceWarning)

class PythonOrgSearch(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.close()

    def test_home_page_with_happy_number(self):
        driver = self.driver
        driver.get("http://localhost:5000")
        num_input = driver.find_element(By.NAME, "number")
        num_input.clear()
        num_input.send_keys("7")
        num_input.send_keys(Keys.RETURN)
        time.sleep(2)  # adding delay
        assert "The number 7 is a happy number." in driver.page_source

    def test_result_page_with_unhappy_number(self):
        driver = self.driver
        driver.get("http://localhost:5000")
        num_input = driver.find_element(By.NAME, "number")
        num_input.clear()
        num_input.send_keys("4")
        num_input.send_keys(Keys.RETURN)
        time.sleep(2)  # adding delay
        assert "The number 4 is a sad number." in driver.page_source

    def test_result_page_with_large_happy_number(self):
        driver = self.driver
        driver.get("http://localhost:5000")
        num_input = driver.find_element(By.NAME, "number")
        num_input.clear()
        num_input.send_keys("7899999999999959999999996")
        num_input.send_keys(Keys.RETURN)
        time.sleep(2)  # adding delay
        assert "The number 7899999999999959999999996 is a happy number." in driver.page_source

    
    
    def test_result_page_with_large_unhappy_number(self):
        driver = self.driver
        driver.get("http://localhost:5000")
        num_input = driver.find_element(By.NAME, "number")
        num_input.clear()
        num_input.send_keys("12005034444292997294")
        num_input.send_keys(Keys.RETURN)
        time.sleep(2)  # adding delay
        assert "The number 12005034444292997294 is a sad number." in driver.page_source

    def test_input_with_negative_integer(self):
        driver = self.driver
        driver.get("http://localhost:5000")
        num_input = driver.find_element(By.NAME, "number")
        num_input.clear()
        num_input.send_keys("-1")
        num_input.send_keys(Keys.RETURN)
        time.sleep(2)  # adding delay
        assert "Number cannot be negative." in driver.page_source

    def test_input_with_very_large_number(self):
        driver = self.driver
        driver.get("http://localhost:5000")
        num_input = driver.find_element(By.NAME, "number")
        num_input.clear()
        num_input.send_keys("1" * 101)  # input a number with 101 digits
        num_input.send_keys(Keys.RETURN)
        time.sleep(2)  # adding delay
        assert "Number is too large." in driver.page_source


if __name__ == "__main__":
    unittest.main()
