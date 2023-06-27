import unittest
from flask import Flask
from flask_testing import TestCase
from app import app
from Happynumber import Solution
from unittest.mock import patch

class IntegrationTestCase(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_result_route(self):
        test_cases = [
            (19, True, b"The number 19 is a happy number"),
            (4, False, b"The number 4 is a sad number"),
            (7899999999999959999999996, True, b"The number 7899999999999959999999996 is a happy number"),
            (888888888, False, b"The number 888888888 is a sad number"),
            (10**100, None, b"Number is too large"),
            (-10, None, b"Number cannot be negative"),
            (3.14, None, b"Input must be an integer"),
        ]

        for number, expected_is_happy, expected_message in test_cases:
            with patch.object(Solution, 'isHappy', return_value=expected_is_happy):
                response = self.client.post('/result', data={'number': str(number)})
                self.assertEqual(response.status_code, 200)
                self.assertIn(expected_message, response.data)

if __name__ == '__main__':
    unittest.main()
