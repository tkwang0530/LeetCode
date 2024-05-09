
"""
3075. Maximize Happiness of Selected Children
description: https://leetcode.com/problems/maximize-happiness-of-selected-children/description/
"""

"""
Note:
1. minHeap + Sort: O((n+k)logk) time | O(k) space - where n is the number of children and k is the number of children selected
"""

from typing import List
import heapq
class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        # pick top k happiness value
        minHeap = []
        for value in happiness:
            if len(minHeap) < k:
                heapq.heappush(minHeap, value)
            else:
                heapq.heappushpop(minHeap, value)

        maxSum = 0
        picked = 0
        minHeap.sort()
        while minHeap:
            value = minHeap.pop()
            maxSum += max(value-picked, 0)
            picked += 1
        return maxSum

# Unit Tests
import unittest
funcs = [Solution().maximumHappinessSum]

class TestMaximumHappinessSum(unittest.TestCase):
    def testMaximumHappinessSum1(self):
        for maximumHappinessSum in funcs:
            happiness = [1,2,3]
            k = 2
            self.assertEqual(maximumHappinessSum(happiness=happiness, k=k), 4)

    def testMaximumHappinessSum2(self):
        for maximumHappinessSum in funcs:
            happiness = [1,1,1,1]
            k = 2
            self.assertEqual(maximumHappinessSum(happiness=happiness, k=k), 1)

    def testMaximumHappinessSum3(self):
        for maximumHappinessSum in funcs:
            happiness = [2,3,4,5]
            k = 1
            self.assertEqual(maximumHappinessSum(happiness=happiness, k=k), 5)

if __name__ == "__main__":
    unittest.main()