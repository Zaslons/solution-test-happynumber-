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




