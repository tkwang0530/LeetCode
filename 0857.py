"""
857. Minimum Cost to Hire K Workers
There are n workers. You are given two integer arrays quality and wage where quality[i] is the quality of the i-th worker and wage[i] is the minimum wage expectation for the i-th worker.

We want to hire exactly k workers to form a paid group. To hire a group of k workers, we must pay them according to the following rules:
1. Every worker in the paid group should be paid in the ratio of their quality compared to other workers in the paid group.

2. Every worker in the paid group must be paid at least their minimum wage expectation.

Given the integer k, return the least amount of money needed to form a paid group satisfying the above conditions. Answers within 10^-5 of the actual answer will be accepted.

Example1:
Input: quality = [10,20,5], wage = [70,50,30], k = 2
Output: 105.00000
Explanation: We pay 70 to 0th worker and 35 to 2nd worker.

Example2:
Input: quality = [3,1,10,10,1], wage = [4,8,2,2,7], k = 3
Output: 30.66667
Explanation: We pay 4 to 0th worker, 13.33333 to 2nd and 3rd workers separately.

Constraints:
n == quality.length == wage.length
1 <= k <= n <= 10^4
1 <= quality[i], wage[i] <= 10^4
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

    def mincostToHireWorkers2(self, quality: List[int], wage: List[int], k: int) -> float:
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
funcs = [Solution().mincostToHireWorkers, Solution().mincostToHireWorkers2]
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
