"""
301. Remove Invalid Parentheses
Given a string s that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.

Return all the possible results. You may return the answer in any order.

Example1:
Input: s = "()())()"
Output: ["(())()","()()()"]

Example2:
Input: s = "(a)())()"
Output: ["(a())()","(a)()()"]

Example3:
Input: s = ")("
Output: [""]

Constraints:
1 <= s.length <= 25
s consists of lowercase English letters and parentheses '(' and ')'.
There will be at most 20 parentheses in s.
"""

"""
Note:
1. DFS: O(2^n) time | O(n) space
2. DFS (slight improve): O(2^n) time | O(n) space
more readability than sol1 but less efficiency

scan entire string s, once we find ) is more then (, delete one )
1) delete which ) ?
2) How to prevent duplicates ? track the lastRemove index
3) If ( is more than ), how to deal with this case? 
reverse the string s, pattern = [('(', ')'), (')', '(')]
4) How to determine which kind of parentheses is more than the other? stack vs count

"""

from typing import List, Tuple
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        result = []
        patterns = [('(', ')'), (')', '(')]
        self.dfs(patterns, patterns[0], s, 0, 0, result)
        return result

    # 1. definition
    def dfs(self, patterns: List[Tuple[str]], pattern: Tuple[str], s: str, start: int, lastRemove: int, result: List[str]) -> None:
        # 2. divide
        count, n = 0, len(s)
        for i in range(start, n):
            if s[i] == pattern[0]: count += 1
            if s[i] == pattern[1]: count -= 1
            if count < 0:
                # delete one
                for j in range(lastRemove, i+1):
                    char = s[j]
                    if char == pattern[1] and (j == lastRemove or char != s[j-1]) :
                        self.dfs(patterns, pattern, s[0 : j] + s[j+1:], i, j, result)
                # 3. exit
                return
        s = s[::-1]
        if pattern == patterns[0]:
            self.dfs(patterns, patterns[1], s, 0, 0, result)
        else:
            result.append(s)
    
    def removeInvalidParentheses2(self, s: str) -> List[str]:
        patterns = [('(', ')'), (')', '(')]
        result = []
        if not s or len(s) == 0:
            result.append("")
            return result
        mode = 0 # 0: check the point that close > open ; 1: check the point that open > close
        self.dfs2(patterns, mode, s, 0, result)
        return result

    def dfs2(self, patterns, mode, s, lastRemove, result) -> None:
        count = i = 0
        while i < len(s) and count >= 0:
            if s[i] == patterns[mode][0]: count += 1
            if s[i] == patterns[mode][1]: count -= 1
            i += 1
        # if count < 0, we need to remove redundant close parentheses
        if count < 0:
            for j in range(lastRemove, len(s)):
                if s[j] == patterns[mode][1] and (j == lastRemove or s[j-1] != patterns[mode][1]):
                    self.dfs2(patterns, mode, s[0: j] + s[j+1:], j, result)
        else:
            reverse = s[::-1]
            if mode == 0:
                self.dfs2(patterns, 1, reverse, 0, result)
            else:
                result.append(reverse)



# Unit Tests
import unittest
funcs = [Solution().removeInvalidParentheses, Solution().removeInvalidParentheses2]


class TestRemoveInvalidParentheses(unittest.TestCase):
    def testRemoveInvalidParentheses1(self):
        for func in funcs:
            s = "()())()"
            self.assertEqual(sorted(func(s=s)), sorted(["(())()","()()()"]))

    def testRemoveInvalidParentheses2(self):
        for func in funcs:
            s = "(a)())()"
            self.assertEqual(sorted(func(s=s)), sorted(["(a())()","(a)()()"]))

    def testRemoveInvalidParentheses3(self):
        for func in funcs:
            s = ")("
            self.assertEqual(sorted(func(s=s)), sorted([""]))


if __name__ == "__main__":
    unittest.main()