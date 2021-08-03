"""
378. Kth Smallest Element in a Sorted Matrix
Given an n x n matrix where each of the rows and columns are sorted in ascending order, return the kth smallest element in the matrix

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example1:
Input: matrix = [
    [1,5,9],
    [10,11,13],
    [12,13,15]
], k = 8
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13

Example2:
Input: matrix = [[-5]], k = 1
Output: -5

Constraints:
n == matrix.length
n == matrix[i].length
1 <= n <= 300
-10^9 <= matrix[i][j] <= 10^9
All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
1 <= k <= n^2
"""

"""
Note:
1. Binary Search: O(nlogn * log(max-min)) time | O(1) space
"""

from bisect import bisect_right
from typing import List
import unittest

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        left, right = matrix[0][0], matrix[-1][-1]
        while left < right:
            mid = left + (right - left) // 2
            count = 0
            for row in matrix:
                count += bisect_right(row, mid)
            if count >= k:
                right = mid
            else:
                left = mid + 1
        return left



# Unit Tests
funcs = [Solution().kthSmallest]

class TestKthSmallest(unittest.TestCase):
    def testKthSmallest1(self):
        for func in funcs:
            matrix = [[1,5,9],[10,11,13],[12,13,15]]
            k = 8
            self.assertEqual(
                func(matrix=matrix, k=k), 13)
    
    def testKthSmallest2(self):
        for func in funcs:
            matrix = [[-5]]
            k = 1
            self.assertEqual(
                func(matrix=matrix, k=k), -5)

if __name__ == "__main__":
    unittest.main()
