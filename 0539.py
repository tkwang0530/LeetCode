"""
539. Minimum Time Difference
Given a list of 24-hour clock time points in "HH:MM" format, return the minimum minutes difference between any two time-points in the list.

Example1:
Input: timePoints = ["23:59","00:00"]
Output: 1

Example2:
Input: timePoints = ["00:00","23:59","00:00"]
Output: 0

Constraints:
2 <= timePoints.length <= 2 * 10^4
timePoints[i] is in the format "HH:MM".
"""

"""
Note:
1. Sliding Window + bucket: O(1440*2) time | O(1440) space
"""

from typing import List
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = [0] * 1440
        for timePoint in timePoints:
            hourStr, minuteStr = timePoint.split(":")
            hour, minute = int(hourStr), int(minuteStr)
            mins = 60*hour + minute
            if minutes[mins]:
                return 0
            minutes[mins] += 1
    
        n = len(minutes)
        
        # find the first unzero position and assign it to start
        start = 0
        while start < n and minutes[start] == 0:
            start += 1
        
        minDiff = float("inf")
        for i in range(start+1, 2*n):
            end = i % n
            if minutes[end] == 0:
                continue
            
            minDiff = min(
                minDiff,
                abs(end-start),
                abs(abs(end-start)-1440)
            )
            start = end
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