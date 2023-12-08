"""
72. Edit Distance
description: https://leetcode.com/problems/edit-distance/description/
"""

"""
Note:
1. dfs (bottom-up) + memo: O(mn) time | O(mn) space - where m is the length of word1 and n is the length of word2
"""

import functools
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        L1 = len(word1)
        L2 = len(word2)
        @functools.lru_cache(None)
        def dfs(i: int, j: int) -> int:
            if i == L1 and j == L2:
                # finish the changes
                return 0
            if i == L1 and j < L2:
                # cost to insert the left part
                return L2 - j
            if j == L2 and i < L1:
                # cost to remove the left part
                return L1 - i
            
            char1, char2 = word1[i], word2[j]
            if char1 == char2:
                return dfs(i+1, j+1)

            # op1: insert
            insertOps = 1 + dfs(i, j+1)

            # op2: delete
            deleteOps = 1 + dfs(i+1, j)

            # op3: replace
            replaceOps = 1 + dfs(i+1, j+1)

            return min(insertOps, deleteOps, replaceOps)
        return dfs(0, 0)


# Unit Tests
import unittest
funcs = [Solution().minDistance]
class TestMinDistance(unittest.TestCase):
    def testMinDistance1(self):
        for func in funcs:
            word1 = "horse"
            word2 = "ros"
            self.assertEqual(func(word1=word1, word2=word2), 3)

    def testMinDistance2(self):
        for func in funcs:
            word1 = "intention"
            word2 = "execution"
            self.assertEqual(func(word1=word1, word2=word2), 5)

if __name__ == "__main__":
    unittest.main()
