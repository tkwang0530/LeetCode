"""
402. Remove K Digits
Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

Example1:
Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.

Example2:
Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.

Example3:
Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.

Constraints:
1 <= k <= num.length <= 10^5
num consists of only digits
num does not have any leading zeros except for the zero itself.
"""

"""
Note:
1. Monotonic Stack: O(n) time | O(n) space - where n is the length of string num
"""

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for digit in num:
            while stack and int(stack[-1]) > int(digit) and k > 0:
                stack.pop()
                k -= 1
            stack.append(digit)

        result = ""
        for i, digit in enumerate(stack):
            if digit != "0":
                result = "".join(stack[i:len(stack) - k])
                break
        
        return "0" if result == "" else result

# Unit Tests
import unittest
funcs = [Solution().removeKdigits]
class TestRemoveKdigits(unittest.TestCase):
    def testRemoveKdigits1(self):
        for func in funcs:
            num = "1432219"
            k = 3
            self.assertEqual(func(num=num, k=k), "1219")

    def testRemoveKdigits2(self):
        for func in funcs:
            num = "10200"
            k = 1
            self.assertEqual(func(num=num, k=k), "200")

    def testRemoveKdigits3(self):
        for func in funcs:
            num = "10"
            k = 2
            self.assertEqual(func(num=num, k=k), "0")

    def testRemoveKdigits4(self):
        for func in funcs:
            num = "112"
            k = 1
            self.assertEqual(func(num=num, k=k), "11")

    def testRemoveKdigits5(self):
        for func in funcs:
            num = "9"
            k = 1
            self.assertEqual(func(num=num, k=k), "0")

    def testRemoveKdigits6(self):
        for func in funcs:
            num = "10001"
            k = 4
            self.assertEqual(func(num=num, k=k), "0")

if __name__ == "__main__":
    unittest.main()
