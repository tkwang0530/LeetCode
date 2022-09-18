"""
504. Base 7
Given an integer num, return a string of its base 7 representation.

Example1:
Input: num = 100
Output: "202"

Example2:
Input: num = -7
Output: "-10"

Constraints:
-10^7 <= num <= 10^7
"""

"""
Note:
1. Brute Force: O(1) time | O(1) space
"""




import unittest
class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        base7 = [] if num >= 0 else ["-"]
        num = abs(num)
        power = 9
        hasLeading = False
        while power >= 0:
            quotient = num//(7**power)
            if quotient == 0 and hasLeading:
                base7.append("0")
            elif quotient != 0:
                base7.append(str(quotient))
                hasLeading = True
            num %= (7**power)
            power -= 1
        return "".join(base7)


# Unit Tests
funcs = [Solution().convertToBase7]


class TestConvertToBase7(unittest.TestCase):
    def testConvertToBase7_1(self):
        for func in funcs:
            num = 100
            self.assertEqual(func(num=num), "202")

    def testConvertToBase7_2(self):
        for func in funcs:
            num = -7
            self.assertEqual(func(num=num), "-10")


if __name__ == "__main__":
    unittest.main()
