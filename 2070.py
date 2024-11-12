"""
2070. Most Beautiful Item for Each Query
description: https://leetcode.com/problems/most-beautiful-item-for-each-query/description/ 
"""

"""
Note:
1. Greedy: O((n+q)log(n+q)) time | O(n+q) space
"""

from typing import List
class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        seqs = [(price, beauty, -1) for price, beauty in items]
        for i, q in enumerate(queries):
            seqs.append((q, -1, i))

        seqs.sort(key=lambda x: (x[0], -x[1]))
        runningMaxBeauty = 0
        output = [0] * len(queries)
        for _, beauty, queryIdx in seqs:
            if beauty != -1:
                runningMaxBeauty = max(runningMaxBeauty, beauty)
            else:
                output[queryIdx] = runningMaxBeauty
        return output

import unittest
funcs = [Solution().maximumBeauty]

class TestMaximumBeauty(unittest.TestCase):
    def testMaximumBeauty1(self):
        for func in funcs:
            items = [[1,2],[3,2],[2,4],[5,6],[3,5]]
            queries = [1,2,3,4,5,6]
            self.assertEqual(func(items=items, queries=queries), [2,4,5,5,6,6])

    def testMaximumBeauty2(self):
        for func in funcs:
            items = [[1,2],[1,2],[1,3],[1,4]]
            queries = [1]
            self.assertEqual(func(items=items, queries=queries), [4]) 

    def testMaximumBeauty3(self):
        for func in funcs:
            items = [[10,1000]]
            queries = [5]
            self.assertEqual(func(items=items, queries=queries), [0]) 

if __name__ == "__main__":
    unittest.main()
