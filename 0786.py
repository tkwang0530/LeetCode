
"""
786. K-th Smallest Prime Fraction
description: https://leetcode.com/problems/k-th-smallest-prime-fraction/description/
"""

"""
Note:
1. maxHeap: O(n^2*log(k)) time | O(k) space - where n is the length of array arr
"""

import heapq
from typing import List
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

# Unit Tests
import unittest
funcs = [Solution().kthSmallestPrimeFraction]

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