"""
539. Minimum Time Difference
description: https://leetcode.com/problems/minimum-time-difference/description/
"""

"""
Note:
1. Sliding Window + bucket: O(1440*2) time | O(1440) space
"""

from typing import List
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timestamp = [0] * 1440
        for tp in timePoints:
            hourStr, minStr = tp.split(":")
            hours, mins = int(hourStr), int(minStr)
            timestamp[(hours*60+mins)%1440] += 1
            if timestamp[(hours*60+mins)%1440] == 2:
                return 0
        
        minDiff = float("inf")
        prev = -1
        for i in range(2 * 1440):
            j = i % 1440
            if not timestamp[j]:
                continue
            if prev == -1:
                prev = i
            else:
                minDiff = min(minDiff, i-prev)
                prev = i
        return minDiff

# Unit Tests
import unittest
funcs = [Solution().findMinDifference]

class TestFindMinDifference(unittest.TestCase):
    def testFindMinDifference1(self):
        for func in funcs:
            timePoints = ["23:59","00:00"]
            self.assertEqual(func(timePoints=timePoints), 1)

    def testFindMinDifference2(self):
        for func in funcs:
            timePoints = ["00:00","23:59","00:00"]
            self.assertEqual(func(timePoints=timePoints), 0)

    def testFindMinDifference3(self):
        for func in funcs:
            timePoints = ["00:00","04:00","22:00"]
            self.assertEqual(func(timePoints=timePoints), 120)

if __name__ == "__main__":
    unittest.main()