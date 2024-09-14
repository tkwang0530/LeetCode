"""
97. Interleaving String
description: https://leetcode.com/problems/interleaving-string/description/
"""

"""
Note:
1. dfs+memo: O(mn) time | O(mn) space - where m and n are the lengths of strings s1 and s2
"""

import functools
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1, n2 = len(s1), len(s2)
        n3 = n1+n2
        if n3 != len(s3):
            return False
        
        @functools.lru_cache(None)
        def dfs(idx1, idx2) -> bool:
            idx3 = idx1+idx2
            if idx3 == n3:
                return True
            ans = False
            if idx1 < n1 and s1[idx1] == s3[idx3]:
                ans = ans or dfs(idx1+1, idx2)
            
            if idx2 < n2 and s2[idx2] == s3[idx3]:
                ans = ans or dfs(idx1, idx2+1)

            return ans

        return dfs(0, 0)

# Unit Tests
import unittest
funcs = [Solution().isInterleave]
class TestIsInterleave(unittest.TestCase):
    def testIsInterleave1(self):
        for isInterleave in funcs:
            s1 = "aabcc"
            s2 = "dbbca"
            s3 = "aadbbcbcac"
            self.assertTrue(isInterleave(s1=s1, s2=s2, s3=s3))


    def testIsInterleave2(self):
        for isInterleave in funcs:
            s1 = "aabcc"
            s2 = "dbbca"
            s3 = "aadbbbaccc"
            self.assertFalse(isInterleave(s1=s1, s2=s2, s3=s3))


    def testIsInterleave3(self):
        for isInterleave in funcs:
            s1 = ""
            s2 = ""
            s3 = ""
            self.assertTrue(isInterleave(s1=s1, s2=s2, s3=s3))

if __name__ == "__main__":
    unittest.main()
