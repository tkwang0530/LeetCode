"""
826. Most Profit Assigning Work
description: https://leetcode.com/problems/most-profit-assigning-work/description/
"""

"""
Note:
1. Greedy + Sort: O(nlogn+n+m) time | O(n) space - where n is length of array difficulty and m is length of array worker
ref: https://www.youtube.com/watch?v=hh1hF2hS3C4
"""

from typing import List
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        n = len(difficulty)
        jobs = []
        for i in range(n):
            jobs.append((difficulty[i], profit[i]))

        jobs.sort()
        worker.sort()

        totalProfit = 0
        i = 0
        best = 0
        for level in worker:
            while i < n and level >= jobs[i][0]:
                best = max(best, jobs[i][1])
                i += 1
            totalProfit += best
        return totalProfit

# Unit Tests
import unittest
funcs = [Solution().maxProfitAssignment]
class TestMaxProfitAssignment(unittest.TestCase):
    def testMaxProfitAssignment1(self):
        for func in funcs:
            difficulty = [2,4,6,8,10]
            profit = [10,20,30,40,50]
            worker = [4,5,6,7]
            self.assertEqual(func(difficulty, profit, worker), 100)


    def testMaxProfitAssignment2(self):
        for func in funcs:
            difficulty = [85,47,57]
            profit = [24,66,99]
            worker = [40,25,25]
            self.assertEqual(func(difficulty, profit, worker), 0)


if __name__ == "__main__":
    unittest.main()
