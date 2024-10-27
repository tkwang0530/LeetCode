"""
14. Longest Common Prefix
description: https://leetcode.com/problems/longest-common-prefix/description/
"""

"""
Note:
1. Brute-Force: O(mn) time | O(m) space - where m is the length of array strs and m is the minimum length from the strings 
"""

import unittest
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minLen = min([len(s) for s in strs])
        common = []
        i = 0
        while i < minLen:
            allSame = True
            for j in range(1, len(strs)):
                s = strs[j]
                if s[i] != strs[j-1][i]:
                    return "".join(common)
            
            common.append(strs[0][i])
            i += 1
        return "".join(common)

# Unit Tests
import unittest
funcs = [Solution().longestCommonPrefix]
class TestLongestCommonPrefix(unittest.TestCase):
    def testLongestCommonPrefix1(self):
        for func in funcs:
            strs = ["flower","flow","flight"]
            self.assertEqual(func(strs=strs), "fl")

    def testLongestCommonPrefix2(self):
        for func in funcs:
            strs = ["dog","racecar","car"]
            self.assertEqual(func(strs=strs), "")

if __name__ == "__main__":
    unittest.main()
