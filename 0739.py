"""
739. Daily Temperatures
description: https://leetcode.com/problems/daily-temperatures/description/
"""

""" 
1. Monotonic Decreasing Stack: O(n) time | O(n) space - where n is len(temperatures)
"""
from typing import List
class Solution(object):
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for i, temperature in enumerate(temperatures):
            while stack and stack[-1][0] < temperature:
                _, j = stack.pop()
                result[j] = i-j
            stack.append((temperature, i))
        return result


# Unit Tests
import unittest
funcs = [Solution().dailyTemperatures]
class TestDailyTemperatures(unittest.TestCase):
    def testDailyTemperatures1(self):
        for func in funcs:
            temperatures = [73,74,75,71,69,72,76,73]
            self.assertEqual(func(temperatures=temperatures), [1,1,4,2,1,1,0,0])

    def testDailyTemperatures2(self):
        for func in funcs:
            temperatures = [30,40,50,60]
            self.assertEqual(func(temperatures=temperatures), [1,1,1,0])

    def testDailyTemperatures3(self):
        for func in funcs:
            temperatures = [30,60,90]
            self.assertEqual(func(temperatures=temperatures), [1,1,0])

if __name__ == "__main__":
    unittest.main()
