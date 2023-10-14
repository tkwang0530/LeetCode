"""
2896. Apply Operations to Make Two Strings Equal
description: https://leetcode.com/problems/apply-operations-to-make-two-strings-equal/description/
"""

"""
Note:
1. dfs+memo: O(n) time | O(n) space - where n is the length of string s1
2. dfs+memo: O(n^2) time | O(n^2) space - where n is the length of string s1
"""

import functools
class Solution:
    def minOperations(self, s1: str, s2: str, x: int) -> int:
        indice = []
        for i, (c1, c2) in enumerate(zip(s1, s2)):
            if c1 != c2:
                indice.append(i)
        
        n = len(indice)
        if n % 2 > 0:
            return -1
        
        @functools.lru_cache(None)
        def dfs(i):
            if i == 0:
                return x / 2
            elif i < 0:
                return 0
            
            return min(dfs(i-1) + x/2, dfs(i-2) + indice[i] - indice[i-1])

        return int(dfs(n-1))

class Solution2:
    def minOperations(self, s1: str, s2: str, x: int) -> int:
        indice = []
        for i, (c1, c2) in enumerate(zip(s1, s2)):
            if c1 != c2:
                indice.append(i)
        
        n = len(indice)
        if n % 2 > 0:
            return -1
        @functools.lru_cache(None)
        def dfs(i, j):
            if i >= j:
                return 0
            
            index1, index2, index3, index4 = indice[i], indice[i+1], indice[j-1], indice[j]
            cost = min(
                min(index4-index1, x) + dfs(i+1, j-1),
                min(index2-index1, x) + dfs(i+2, j),
                min(index4-index3, x) + dfs(i, j-2)
            )
            return cost

        return dfs(0, n-1)

# Unit Tests
import unittest
funcs = [Solution().minOperations, Solution2().minOperations]

class TestMinOperations(unittest.TestCase):
    def testMinOperations1(self):
        for minOperations in funcs:
            s1 = "1100011000"
            s2 = "0101001010"
            x = 2
            self.assertEqual(minOperations(s1=s1, s2=s2, x=x), 4)

    def testMinOperations2(self):
        for minOperations in funcs:
            s1 = "10110"
            s2 = "00011"
            x = 4
            self.assertEqual(minOperations(s1=s1, s2=s2, x=x), -1)

if __name__ == "__main__":
    unittest.main()