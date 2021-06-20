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
1. Recursion with string concatenation: O(n*2^n) time | O(n + 2^n) space
2. Recursion with List[str]: O(n*2^n) time | O(n + 2^n) space
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

        def helper(list, i):
            if i == len(list):
                result.append("".join(list))  # O(n)
            else:
                if list[i].isalpha():
                    list[i] = list[i].lower()
                    helper(list, i + 1)
                    list[i] = list[i].upper()
                    helper(list, i + 1)
                else:
                    helper(list, i + 1)

        helper(list(s), 0)  # list("abc") => ["a", "b", "c"]
        return result


# Unit Tests
import unittest


class TestLetterCasePermutation(unittest.TestCase):
    def testLetterCasePermutation1(self):
        func = Solution().letterCasePermutation
        func2 = Solution().letterCasePermutation2
        self.assertEqual(func(s="a1b2"), ["a1b2", "a1B2", "A1b2", "A1B2"])
        self.assertEqual(func2(s="a1b2"), ["a1b2", "a1B2", "A1b2", "A1B2"])

    def testLetterCasePermutation1(self):
        func = Solution().letterCasePermutation
        func2 = Solution().letterCasePermutation2
        self.assertEqual(func(s="3z4"), ["3z4", "3Z4"])
        self.assertEqual(func2(s="3z4"), ["3z4", "3Z4"])

    def testLetterCasePermutation3(self):
        func = Solution().letterCasePermutation
        func2 = Solution().letterCasePermutation2
        self.assertEqual(func(s="12345"), ["12345"])
        self.assertEqual(func2(s="12345"), ["12345"])

    def testLetterCasePermutation4(self):
        func = Solution().letterCasePermutation
        func2 = Solution().letterCasePermutation2
        self.assertEqual(func(s="0"), ["0"])
        self.assertEqual(func2(s="0"), ["0"])


if __name__ == "__main__":
    unittest.main()