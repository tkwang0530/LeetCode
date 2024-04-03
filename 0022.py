"""
22. Generate Parentheses
description: https://leetcode.com/problems/generate-parentheses/description/
"""

"""
Note:
1. backtracking: O(n * 2^(2n)) time | O(2n) space
"""

from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        counter = [n] * 2
        output = []
        chars = []
        def backtrack():
            if sum(counter) == 0:
                output.append("".join(chars))
                return

            # left
            if counter[0] > 0:
                counter[0] -= 1
                chars.append("(")
                backtrack()
                chars.pop()
                counter[0] += 1

            # right
            if counter[1] > counter[0]:
                counter[1] -= 1
                chars.append(")")
                backtrack()
                chars.pop()
                counter[1] += 1
        backtrack()
        return output

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