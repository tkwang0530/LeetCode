"""
22. Generate Parentheses
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example2:
Input: n = 1
Output: ["()"]

Constraints:
1 <= n <= 8
"""

"""
Note:
1. DFS (append to result when index == len(nums)): O(2^(2n)) time | O(n) space
The time complexity is upper bound

(1) Definition
left: the number of available open parentheses
right: the number of available close parentheses

(2) edge case: when left == 0 and right == 0: result.append("".join(chars))
(3) if left > 0: append "(" to chars, dfs(left+1 ...), and then chars.pop()
(4) if right > 0 and left < right: append ")" to chars, dfs(right)
"""

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        if n <= 0:
            return result
        self.dfs(n, n, [], result)
        return result
    
    def dfs(self, left: int, right: int, chars: List[str], result: List[str]):
        if left == 0 and right == 0:
            result.append("".join(chars))
            return
        
        if left > 0:
            chars.append("(")
            self.dfs(left - 1, right, chars, result)
            chars.pop()
        if right > 0 and left < right:
            chars.append(")")
            self.dfs(left, right - 1, chars, result)
            chars.pop()


# Unit Tests
import unittest
funcs = [Solution().generateParenthesis]

class TestGenerateParenthesis(unittest.TestCase):
    def testGenerateParenthesis1(self):
        for func in funcs:
            n = 3
            self.assertEqual(sorted(func(n=n)), sorted(["((()))","(()())","(())()","()(())","()()()"]))

    def testGenerateParenthesis2(self):
        for func in funcs:
            n = 1
            self.assertEqual(sorted(func(n=n)), sorted(["()"]))

if __name__ == "__main__":
    unittest.main()