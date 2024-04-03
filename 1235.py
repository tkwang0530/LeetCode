"""
1235. Maximum Profit in Job Scheduling
description: https://leetcode.com/problems/maximum-profit-in-job-scheduling/description/
"""

"""
Note:
1. dfs+memo: O(nlogn) time | O(n) space - where n is the length of array startTime
ref: https://www.youtube.com/watch?v=JLoWc3v0SiE
"""

from typing import List
import bisect, functools
import unittest
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit))

        @functools.lru_cache(None)
        def dfs(i):
            if i == len(jobs):
                return 0

            # don't include
            maxProfit = dfs(i+1)

            # include
            j = bisect.bisect(jobs, (jobs[i][1], -1, -1))
            maxProfit = max(maxProfit, jobs[i][-1] + dfs(j))
            return maxProfit

        return dfs(0)

# Unit Tests
funcs = [Solution().jobScheduling]


class TestJobScheduling(unittest.TestCase):
    def testJobScheduling1(self):
        for func in funcs:
            startTime = [1,2,3,3]
            endTime = [3,4,5,6]
            profit = [50,10,40,70]
            self.assertEqual(func(startTime=startTime, endTime=endTime, profit=profit), 120)

    def testJobScheduling2(self):
        for func in funcs:
            startTime = [1,2,3,4,6]
            endTime = [3,5,10,6,9]
            profit = [20,20,100,70,60]
            self.assertEqual(func(startTime=startTime, endTime=endTime, profit=profit), 150)

if __name__ == "__main__":
    unittest.main()
