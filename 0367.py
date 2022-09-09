"""
367. Valid Perfect Square
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Follow up: Do not use any built-in library function such as sqrt.

Example1:
Input: num = 16
Output: true

Example2:
Input: num = 14
Output: false

Constraints:
1 <= num <= 2^31 - 1
"""

"""
Note:
1. Math: O(1) time | O(1) space
2. Binary Search: O(logn) time | O(1) space
"""




import unittest
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        candidateSquareRoot = int(num ** 0.5)
        return candidateSquareRoot ** 2 == num

    def isPerfectSquare2(self, num: int) -> bool:
        left, right = 0, num+1
        while left < right:
            mid = left + (right - left) // 2

            if mid ** 2 == num:
                return True
            elif mid ** 2 < num:
                left = mid+1
            else:
                right = mid
        return left**2 == num


# Unit Tests
funcs = [Solution().isPerfectSquare, Solution().isPerfectSquare2]


class TestIsPerfectSquare(unittest.TestCase):
    def testIsPerfectSquare1(self):
        for func in funcs:
            num = 16
            self.assertEqual(func(num=num), True)

    def testIsPerfectSquare2(self):
        for func in funcs:
            num = 14
            self.assertEqual(func(num=num), False)


if __name__ == "__main__":
    unittest.main()
