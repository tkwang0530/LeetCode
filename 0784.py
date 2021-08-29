"""
784. Letter Case Permutation
Given a string s, we can transform every letter individually to be lowercase or uppercase to create another string.

Return a list of all possible strings we could create. You can return the output in any order.

Example1:
    Input: s = "a1b2"
    Output: ["a1b2","a1B2","A1b2","A1B2"]

Example2:
    Input: s = "3z4"
    Output: ["3z4","3Z4"]

Example3:
    Input: s = "12345"
    Output: ["12345"]

Example4:
    Input: s = "0"
    Output: ["0"]

Constraints:
    s will be s string with length between 1 and 12.
    s will consist only of letters or digits.
"""

"""
Note:
1. DFS with string concatenation: O(n^2 * 2^n) time | O(n * 2^n) space
2. DFS with List[str]: O(n * 2^n) time | O(n * 2^n) space
3. Iteration: O(n * 2^n) time | O(n * 2^n) space
(0) initiate result = [s]
(1) use index i to traverse the input string s, if the char is alphabet do the (2)
(2) for each permutation in result: swapcase the letter in position i and append it to the result
"""

from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        result = []

        def helper(s, i, curr_str):
            if i == len(s):  # base case, already finish building string
                result.append(curr_str)
            else:
                if s[i].isalpha():
                    # str is immutable, string concatenation will create a new string, O(n)
                    helper(s, i + 1, curr_str + s[i].lower())
                    helper(s, i + 1, curr_str + s[i].upper())
                else:
                    helper(s, i + 1, curr_str + s[i])

        helper(s, 0, "")
        return result

    def letterCasePermutation2(self, s: str) -> List[str]:
        result = []
        self.dfs(list(s), result, 0)
        return result
    
    def dfs(self, chars: List[str], result: List[str], index: int) -> None:
        if index == len(chars):
            result.append("".join(chars))
        else:
            if chars[index].isalpha():
                self.dfs(chars, result, index + 1)
                chars[index] = chars[index].swapcase()
                self.dfs(chars, result, index + 1)
            else:
                self.dfs(chars, result, index + 1)

    def letterCasePermutation3(self, s: str) -> List[str]:
        result = [s]
        for i in range(len(s)):
            if s[i].isalpha():
                for j in range(len(result)):
                    permutation = result[j]
                    result.append(permutation[0:i] + permutation[i].swapcase() + permutation[i+1:])
        return result


# Unit Tests
import unittest
funcs = [Solution().letterCasePermutation, Solution().letterCasePermutation2, Solution().letterCasePermutation3]

class TestLetterCasePermutation(unittest.TestCase):
    def testLetterCasePermutation1(self):
        for func in funcs:
            self.assertEqual(sorted(func(s="a1b2")), sorted(["a1b2", "a1B2", "A1b2", "A1B2"]))

    def testLetterCasePermutation2(self):
        for func in funcs:
            self.assertEqual(sorted(func(s="3z4")), sorted(["3z4", "3Z4"]))

    def testLetterCasePermutation3(self):
        for func in funcs:
            self.assertEqual(sorted(func(s="12345")), sorted(["12345"]))

    def testLetterCasePermutation4(self):
        for func in funcs:
            self.assertEqual(sorted(func(s="0")), sorted(["0"]))

if __name__ == "__main__":
    unittest.main()