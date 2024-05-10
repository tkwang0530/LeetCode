
"""
786. K-th Smallest Prime Fraction
description: https://leetcode.com/problems/k-th-smallest-prime-fraction/description/
"""

"""
Note:
1. maxHeap: O(n^2*log(k)) time | O(k) space - where n is the length of array arr
2. Binary Search: O(n*log(max-min)) time | O(1) space - where n is the length of array arr
ref: https://www.youtube.com/watch?v=ZzfXmZgJ0cw
"""

import heapq
from typing import List, Tuple
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        maxHeap = []
        n = len(arr)
        for i in range(n-1):
            for j in range(i+1, n):
                if len(maxHeap) < k:
                    heapq.heappush(maxHeap, (-(arr[i]/arr[j]), arr[i], arr[j]))
                else:
                    heapq.heappushpop(maxHeap, (-(arr[i]/arr[j]), arr[i], arr[j]))
        return list(maxHeap[0][1:])

class Solution2:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        left, right = 0, 1

        def condition(m) -> Tuple[int, int, int]: # return (total, numerator, denominator)
            maxFraction = [0, 0, 0] # [fraction, numerator, denominator]
            total = 0
            j = 1
            for i in range(n-1):
                while j < n and arr[i] > m * arr[j]:
                    j += 1
                total += (n-j)
                if n == j: break
                fraction = arr[i] / arr[j]
                if fraction > maxFraction[0]:
                    maxFraction = [fraction, arr[i], arr[j]]
            return total, maxFraction[1], maxFraction[2]

        while left < right:
            m = left + (right - left) / 2
            total, numerator, denominator = condition(m)
            if total == k:
                return [numerator, denominator]
            elif total < k:
                left = m
            else:
                right = m
        return []

# Unit Tests
import unittest
funcs = [Solution().kthSmallestPrimeFraction, Solution2().kthSmallestPrimeFraction]

class TestKthSmallestPrimeFraction(unittest.TestCase):
    def testKthSmallestPrimeFraction1(self):
        for kthSmallestPrimeFraction in funcs:
            arr = [1,2,3,5]
            k = 3
            self.assertEqual(kthSmallestPrimeFraction(arr=arr, k=k), [2,5])

    def testKthSmallestPrimeFraction2(self):
        for kthSmallestPrimeFraction in funcs:
            arr = [1,7]
            k = 1
            self.assertEqual(kthSmallestPrimeFraction(arr=arr, k=k), [1,7])


if __name__ == "__main__":
    unittest.main()