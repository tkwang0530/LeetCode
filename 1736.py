"""
1736. Latest Time by Replacing Hidden Digits
description: https://leetcode.com/problems/latest-time-by-replacing-hidden-digits/description/
"""

"""
Note:
1. Brute-Force: O(1) time | O(1) space
"""

class Solution:
    def maximumTime(self, time: str) -> str:
        hourStr, minStr = time.split(":")
        if hourStr[0] == "?" and hourStr[1] != "?":
            if int(hourStr[1]) > 3:
                hourStr = "1" + hourStr[1]
            else:
                hourStr = "2" + hourStr[1]
        elif hourStr == "??":
            hourStr = "23"
        elif hourStr[0] != "?" and hourStr[1] == "?":
            if hourStr[0] == "1":
                hourStr = "19"
            elif hourStr[0] == "2":
                hourStr = "23"
            else:
                hourStr = "09"

        if minStr == "??":
            minStr = "59"
        elif minStr[0] == "?":
            minStr = "5" + minStr[1]
        elif minStr[1] == "?":
            minStr = minStr[0] + "9"

        return hourStr+":"+minStr

# Unit Tests
import unittest
funcs = [Solution().maximumTime]
class TestMaximumTime(unittest.TestCase):
    def testMaximumTime1(self):
        for func in funcs:
            time = "2?:?0"
            self.assertEqual(func(time=time), "23:50")

    def testMaximumTime2(self):
        for func in funcs:
            time = "0?:3?"
            self.assertEqual(func(time=time), "09:39")

    def testMaximumTime3(self):
        for func in funcs:
            time = "1?:22"
            self.assertEqual(func(time=time), "19:22")

if __name__ == "__main__":
    unittest.main()
