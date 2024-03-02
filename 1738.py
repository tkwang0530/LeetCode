"""
1738. Find Kth Largest XOR Coordinate Value
description: https://leetcode.com/problems/find-kth-largest-xor-coordinate-value/description/
"""

"""
Note:
1. dp + minHeap: O(mnlog(k)) time | O(mn+k) space - where m is the length of matrix and n is the length of matrix[0]
"""

import heapq
from typing import List
class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        dp = [[0] * cols for _ in range(rows)]
        minHeap = []

        dp[0][0] = matrix[0][0]
        for row in range(1, rows):
            dp[row][0] = dp[row-1][0] ^ matrix[row][0]

        for col in range(1, cols):
            dp[0][col] = dp[0][col-1] ^ matrix[0][col]

        for row in range(1, rows):
            for col in range(1, cols):
                dp[row][col] = dp[row-1][col]^dp[row][col-1]^matrix[row][col]^dp[row-1][col-1]
        

        for row in range(rows):
            for col in range(cols):
                heapq.heappush(minHeap, dp[row][col])
                if len(minHeap) > k:
                    heapq.heappop(minHeap)

        return minHeap[0]

# Unit Tests
import unittest
funcs = [Solution().kthLargestValue]
class TestKthLargestValue(unittest.TestCase):
    def testKthLargestValue1(self):
        for func in funcs:
            matrix = [[5,2],[1,6]]
            k = 1
            self.assertEqual(func(matrix=matrix, k=k), 7)

    def testKthLargestValue2(self):
        for func in funcs:
            matrix = [[5,2],[1,6]]
            k = 2
            self.assertEqual(func(matrix=matrix, k=k), 5)

    def testKthLargestValue3(self):
        for func in funcs:
            matrix = [[5,2],[1,6]]
            k = 3
            self.assertEqual(func(matrix=matrix, k=k), 4)

if __name__ == "__main__":
    unittest.main()
