"""
2443. Sum of Number and Its Reverse
Given a non-negative integer num, return true if num can be expressed as the sum of any non-negative integer and its reverse, or false otherwise.

Example1:
Input: num = 443
Output: true
Explanation: 172 + 271 = 443 so we return true.

Example2:
Input: num = 63
Output: false
Explanation: 63 cannot be expressed as the sum of a non-negative integer and its reverse so we return false.

Example3:
Input: num = 181
Output: true
Explanation: 140 + 041 = 181 so we return true. Note that when a number is reversed, there may be leading zeros.

Constraints:
0 <= num <= 10^5
"""

"""
Note:
1. Brute-Force: O(n) time | O(1) space
"""




import unittest
class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        if num == 0:
            return True

        def reverse(n):
            return int(str(n)[::-1])

        current = num
        while current > num//2-1:
            if current + reverse(current) == num:
                return True
            current -= 1
        return False


# Unit Tests
funcs = [Solution().sumOfNumberAndReverse]


class TestSumOfNumberAndReverse(unittest.TestCase):
    def testSumOfNumberAndReverse1(self):
        for func in funcs:
            num = 443
            self.assertEqual(func(num=num), True)

    def testSumOfNumberAndReverse2(self):
        for func in funcs:
            num = 63
            self.assertEqual(func(num=num), False)

    def testSumOfNumberAndReverse3(self):
        for func in funcs:
            num = 181
            self.assertEqual(func(num=num), True)


if __name__ == "__main__":
    unittest.main()
