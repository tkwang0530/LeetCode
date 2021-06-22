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
Note:
1. convert to string, and compare it with reversed one: O(n) time | O(n) space
2. recreate a new number in reverse order: O(n) time | O(1) space
3. recreate a new number in reverse order (improve): O(n) time | O(1) space
"""




import unittest
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]

    def isPalindrome2(self, x: int) -> bool:
        if x < 0:
            return False
        temp = x
        reversedNum = 0
        while temp != 0:
            reversedNum = reversedNum * 10 + temp % 10
            temp = temp // 10
        return x == reversedNum

    def isPalindrome3(self, x: int) -> bool:
        if x < 0 or (x > 0 and x % 10 == 0):
            return False
        result = 0
        while x > result:
            result = result * 10 + x % 10
            x = x // 10
        return x == result or x == result // 10


# Unit Tests
funcs = [Solution().isPalindrome, Solution().isPalindrome2,
         Solution().isPalindrome3]


class TestPalindromeNumber(unittest.TestCase):
    def testPalindromeNumber1(self):
        for func in funcs:
            self.assertEqual(func(x=121), True)

    def testPalindromeNumber2(self):
        for func in funcs:
            self.assertEqual(func(x=-121), False)

    def testPalindromeNumber3(self):
        for func in funcs:
            self.assertEqual(func(x=10), False)


if __name__ == "__main__":
    unittest.main()
