"""
739. Daily Temperatures
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the i-th day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

Example1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example2:
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example3:
Input: temperatures = [30,60,90]
Output: [1,1,0]

Constraints:
1 <= temperatures.length <= 10^5
30 <= temperatures[i] <= 100
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
