"""
678. Valid Parenthesis String
description: https://leetcode.com/problems/valid-parenthesis-string/description/
"""

"""
Note:
1. dfs+memo: O(n^2) time | O(n) space - where n is the length of string s
2. Greedy: O(n) time | O(1) space - where n is the length of string s
ref: https://www.youtube.com/watch?v=QhPdNS143Qg
"""

import unittest
import functools
class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)

        @functools.lru_cache(None)
        def dfs(i, left):
            if i == n or left < 0:
                return left == 0
            
            char = s[i]
            if char == "(":
                return dfs(i+1, left+1)
            elif char == ")":
                return dfs(i+1, left-1)
            else:
                return dfs(i+1, left-1) or dfs(i+1, left+1) or dfs(i+1, left)
        
        return dfs(0, 0)
    
class Solution2:
    def checkValidString(self, s: str) -> bool:
        leftMin, leftMax = 0, 0
        for char in s:
            if char == "(":
                leftMin, leftMax = leftMin + 1, leftMax + 1
            elif char == ")":
                leftMin, leftMax = leftMin - 1, leftMax - 1
            else:
                leftMin, leftMax = leftMin - 1, leftMax + 1
            if leftMax < 0:
                return False
            if leftMin < 0:
                leftMin = 0
        return leftMin == 0

# Unit Tests
funcs = [Solution().checkValidString, Solution2().checkValidString]
class TestCheckValidString(unittest.TestCase):
    def testCheckValidString1(self):
        for func in funcs:
            s = "()"
            self.assertEqual(func(s=s), True)

    def testCheckValidString2(self):
        for func in funcs:
            s = "(*)"
            self.assertEqual(func(s=s), True)

    def testCheckValidString3(self):
        for func in funcs:
            s = "(*))"
            self.assertEqual(func(s=s), True)

if __name__ == "__main__":
    unittest.main()
