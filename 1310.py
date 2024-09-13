"""
1310. XOR Queries of a Subarray
description: https://leetcode.com/problems/xor-queries-of-a-subarray/description/
"""

"""
Note:
1. PrefixXOR: O(n+q) time | O(n) space - where n is the length of array arr and q is the length of queries
"""

import unittest
from typing import List
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        preXOR = [0] * (n+1)
        for i in range(1, n+1):
            preXOR[i] = preXOR[i-1] ^ arr[i-1]

        def rangeXOR(i, j):
            return preXOR[j+1] ^ preXOR[i]

        output = [0] * len(queries)
        for i, (left, right) in enumerate(queries):
            output[i] = rangeXOR(left, right)

        return output

# Unit Tests
funcs = [Solution().xorQueries]


class TestXorQueries(unittest.TestCase):
    def testXorQueries1(self):
        for func in funcs:
            arr = [1,3,4,8]
            queries = [[0,1],[1,2],[0,3],[3,3]]
            self.assertEqual(func(arr, queries), [2,7,14,8])

    def testXorQueries2(self):
        for func in funcs:
            arr = [4,8,2,10]
            queries = [[2,3],[1,3],[0,0],[0,3]]
            self.assertEqual(func(arr, queries), [8,0,4,4])



if __name__ == "__main__":
    unittest.main()
