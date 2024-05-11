"""
2960. Count Tested Devices After Test Operations
description: https://leetcode.com/problems/count-tested-devices-after-test-operations/description/
"""

"""
Note:
1. One Pass: O(n) time | O(1) space - where n is the length of array batteryPercentages
"""

from typing import List
class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        testCount = 0
        for percentage in batteryPercentages:
            if percentage-testCount > 0:
                testCount += 1
        return testCount

# Unit Tests
import unittest
funcs = [Solution().countTestedDevices]

class TestCountTestedDevices(unittest.TestCase):
    def testCountTestedDevices1(self):
        for func in funcs:
            batteryPercentages = [1,1,2,1,3]
            self.assertEqual(func(batteryPercentages), 3)

    def testCountTestedDevices2(self):
        for func in funcs:
            batteryPercentages = [0,1,2]
            self.assertEqual(func(batteryPercentages), 2)

if __name__ == "__main__":
    unittest.main()