"""
2895. Minimum Processing Time
description: https://leetcode.com/problems/minimum-processing-time/description/
"""

"""
Note:
1. Greedy: O(nlogn) time | O(sort) space - where n is the length of array tasks
"""

from typing import List
class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse=True)

        i = 0
        j = 0
        minimumTime = 0
        while i < len(processorTime):
            minimumTime = max(minimumTime, processorTime[i]+max(tasks[j:j+4]))
            i += 1
            j = 4 * i
        return minimumTime

# Unit Tests
import unittest
funcs = [Solution().minProcessingTime]

class TestMinProcessingTime(unittest.TestCase):
    def testMinProcessingTime1(self):
        for func in funcs:
            processorTime = [8,10]
            tasks = [2,2,3,1,8,7,4,5]
            self.assertEqual(func(processorTime=processorTime, tasks=tasks), 16)

    def testMinProcessingTime2(self):
        for func in funcs:
            processorTime = [10,20]
            tasks = [2,3,1,2,5,8,4,3]
            self.assertEqual(func(processorTime=processorTime, tasks=tasks), 23)

if __name__ == "__main__":
    unittest.main()