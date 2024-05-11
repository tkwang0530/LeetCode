"""
857. Minimum Cost to Hire K Workers
description: https://leetcode.com/problems/minimum-cost-to-hire-k-workers/description/
"""

"""
Note:
1. maxHeap: O(nlogn + nlogk) time | O(n+k) space
2. SortedList (bst): O(nlogn + nlogk) | O(n+k) space
"""

from sortedcontainers import SortedList
import heapq
from typing import List
class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        wageQuality = [(w, q) for w, q in zip(wage, quality)]
        wageQuality.sort(key = lambda x: x[0]/x[1])

        minTotalWage = float("inf")
        currentSum = 0
        maxHeap = []
        for wage, quality in wageQuality:
            ratio = wage/quality

            if len(maxHeap) < k:
                heapq.heappush(maxHeap, -quality)
                currentSum += quality
                if len(maxHeap) == k:
                    minTotalWage = min(minTotalWage, currentSum * ratio)
            else:
                currentSum += heapq.heappushpop(maxHeap, -quality) + quality
                minTotalWage = min(minTotalWage, currentSum * ratio)
        return minTotalWage

class Solution2:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        wageQuality = [(w, q) for w, q in zip(wage, quality)]
        wageQuality.sort(key = lambda x: x[0]/x[1])

        sortedList = SortedList()
        currentSum = 0
        for i in range(k):
            wage, quality = wageQuality[i]
            sortedList.add(quality)
            currentSum += quality

        minTotalWage = (wageQuality[k-1][0] / wageQuality[k-1][1]) * currentSum
        for i in range(k, len(wageQuality)):
            wage, quality = wageQuality[i]
            ratio = wage / quality

            currentSum += quality
            sortedList.add(quality)

            currentSum -= sortedList[-1]
            sortedList.remove(sortedList[-1])

            minTotalWage = min(minTotalWage, ratio * currentSum)

        return minTotalWage


# Unit Tests
import unittest
funcs = [Solution().mincostToHireWorkers, Solution2().mincostToHireWorkers]
class TestMincostToHireWorkers(unittest.TestCase):
    def testMincostToHireWorkers1(self):
        for func in funcs:
            quality = [10,20,5]
            wage = [70,50,30]
            k = 2
            self.assertTrue(abs(func(quality=quality, wage=wage, k=k) - 105.00000) < 10e-5)

    def testMincostToHireWorkers2(self):
        for func in funcs:
            quality = [3,1,10,10,1]
            wage = [4,8,2,2,7]
            k = 3
            self.assertTrue(abs(func(quality=quality, wage=wage, k=k) - 30.66667) < 10e-5)

if __name__ == "__main__":
    unittest.main()
