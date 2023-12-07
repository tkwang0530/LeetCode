"""
72. Edit Distance
Given two strings word1 and word2, return the minimum number of operations required to convert word1 and word2.

You have the following three operations permitted on a word:
- Insert a character
- Delete a character
- Replace a character

Example1:
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Example2:
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')

Constraints:
0 <= word1.length, word2.length <= 500
word1 and word2 consist of lowercase English letters.
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
