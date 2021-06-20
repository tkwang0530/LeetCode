"""
9. Palindrome Number
Given an integer x, return true if x is palindrome integer.
An integer is a palindrome when it reads the same backward as forward.
Examples:
    Given 121, the answer is true.
    Given -121, the answer is false.
    Given 10, the answer is false.
"""

"""
Solution1: convert to string, and compare it with reversed one
O(n) time | O(n) space
"""
# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         return str(x) == str(x)[::-1]

"""
Solution2: If we don't want to convert the number to string, then recreate a new number in reverse order.
O(n) time | O(1) space
"""
# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         if x < 0:
#             return False
#         temp = x
#         reversedNum = 0
#         while temp != 0:
#             reversedNum = reversedNum * 10 + temp % 10
#             temp = temp // 10
#         return x == reversedNum
"""
Solution3: recreate a new number in reverse order, and modify x in the same time.
O(n) time | O(1) space
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x > 0 and x % 10 == 0):
            return False
        result = 0
        while x > result:
            result = result * 10 + x % 10
            x = x // 10
        return x == result or x == result // 10


# Unit Tests
import unittest


class TestPalindromeNumber(unittest.TestCase):
    def testPalindromeNumber1(self):
        func = Solution().isPalindrome
        self.assertEqual(func(x=121), True)

    def testPalindromeNumber2(self):
        func = Solution().isPalindrome
        self.assertEqual(func(x=-121), False)

    def testPalindromeNumber3(self):
        func = Solution().isPalindrome
        self.assertEqual(func(x=10), False)


if __name__ == "__main__":
    unittest.main()