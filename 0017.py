"""
17. Letter Combinations of a Phone Number
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 doest not map to any letters.
2 -> abc
3 -> def
4 -> ghi
5 -> jkl
6 -> mno
7 -> pqrs
8 -> tuc
9 -> wxyz

Example1:
    Input: digits = "23"
    Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example2:
    Input: digits = ""
    Output: []

Example3:
    Input: digits = "2"
    Output: ["a","b","c"]
"""

"""
Note:
1. Recursion with curr_list: O(n) time | O(1) space
"""




import unittest
from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []

        dict = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        results = []
        self.dfs(digits, 0, [], results, dict)
        return results

    def dfs(self, digits, i, currentList, results, dict):
        if len(currentList) == len(digits):
            results.append("".join(currentList))
        else:
            for letter in dict[digits[i]]:
                currentList.append(letter)
                self.dfs(digits, i + 1, currentList, results, dict)
                currentList.pop()


# Unit Tests
funcs = [Solution().letterCombinations]


class TestLetterCombinations(unittest.TestCase):
    def testLetterCombinations1(self):
        for func in funcs:
            self.assertEqual(
                func(digits="23").sort(),
                ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].sort(),
            )

    def testLetterCombinations2(self):
        for func in funcs:
            self.assertEqual(
                func(digits="").sort(),
                [].sort(),
            )

    def testLetterCombinations3(self):
        for func in funcs:
            self.assertEqual(
                func(digits="2").sort(),
                ["a", "b", "c"].sort(),
            )


if __name__ == "__main__":
    unittest.main()
