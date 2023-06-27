import unittest
from parameterized import parameterized
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from app import app
from Happynumber import Solution

class MockSolution(Solution):
    def isHappy(self, n: int) -> bool:
        return True

class E2ETestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://localhost:5000/')

    def tearDown(self):
        self.driver.quit()

    @parameterized.expand([
        ('19', 'The number 19 is a happy number.'),
        ('4', 'The number 4 is a sad number.'),
        ('7899999999999959999999996', 'The number 7899999999999959999999996 is a happy number.'),
        ('888888888', 'The number 888888888 is a sad number.'),
        ('10' * 100, 'Number is too large.'),
        ('-5', 'Number cannot be negative.'),
        ('3.14', 'Input must be an integer.'),
        ('abc', 'Input must be an integer.'),
    ])
    def test_number_check(self, number, expected_result):
        app.solution = MockSolution()

        number_input = self.driver.find_element(By.ID, 'number')
        number_input.send_keys(number)
        number_input.send_keys(Keys.RETURN)

        result_message = self.driver.find_element(By.TAG_NAME, 'p').text
        self.assertEqual(result_message, expected_result)

if __name__ == '__main__':
    unittest.main()
