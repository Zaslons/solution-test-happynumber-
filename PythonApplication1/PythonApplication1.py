
import unittest

class Solution:
    def isHappy(self, n: int) -> bool:
        """
        Determines whether a number is a happy number or not.

        Args:
            n (int): The number to check.

        Returns:
            bool: True if the number is a happy number, False otherwise.
        """
        slow, fast = n, self.sumSquareDigits(n)

        while slow != fast:
            fast = self.sumSquareDigits(fast)
            fast = self.sumSquareDigits(fast)
            slow = self.sumSquareDigits(slow)

        return True if fast == 1 else False

    def sumSquareDigits(self, n):
        """
        Calculates the sum of the squares of the digits of a number.

        Args:
            n (int): The number to calculate the sum of squares.

        Returns:
            int: The sum of the squares of the digits.
        """
        output = 0
        while n:
            output += (n % 10) ** 2
            n = n // 10
        return output


class TestHappyNumber(unittest.TestCase):
    """
    Unit tests for the Solution class to check the isHappy() and sumSquareDigits() methods.
    """

    def setUp(self):
        """
        Test case setup.
        """
        self.solution = Solution()

    def test_isHappy_with_happy_number(self):
        """
        Test isHappy() method with a happy number.
        """
        result = self.solution.isHappy(19)
        self.assertTrue(result)

    def test_isHappy_with_unhappy_number(self):
        """
        Test isHappy() method with an unhappy number.
        """
        result = self.solution.isHappy(4)
        self.assertFalse(result)

    def test_isHappy_with_zero(self):
        """
        Test isHappy() method with zero.
        """
        result = self.solution.isHappy(0)
        self.assertFalse(result)

    def test_isHappy_with_large_happy_number(self):
        """
        Test isHappy() method with a large happy number.
        """
        result = self.solution.isHappy(986543210)
        self.assertTrue(result)

    def test_isHappy_with_large_unhappy_number(self):
        """
        Test isHappy() method with a large unhappy number.
        """
        result = self.solution.isHappy(999999999)
        self.assertFalse(result)

    def test_sumSquareDigits(self):
        """
        Test sumSquareDigits() method.
        """
        result = self.solution.sumSquareDigits(123)
        self.assertEqual(result, 14)

        result = self.solution.sumSquareDigits(7)
        self.assertEqual(result, 49)

        result = self.solution.sumSquareDigits(0)
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()
