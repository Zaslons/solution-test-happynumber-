import unittest
from parameterized import parameterized
from Happynumber import Solution

class SolutionTestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    @parameterized.expand([
        (123, 14),  # Test positive number
        (5, 25),    # Test single-digit number
        (0, 0),     # Test zero
    ])
    def test_sumSquareDigits(self, number, expected):
        result = self.solution.sumSquareDigits(number)
        self.assertEqual(result, expected)

    @parameterized.expand([
        (19, True),        # Test happy number
        (4, False),        # Test sad number
        (999999999, False) # Test large number
    ])
    def test_isHappy(self, number, expected):
        result = self.solution.isHappy(number)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
