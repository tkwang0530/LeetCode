"""
14. Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings
If there is no common prefix, return an empty string "".

Example1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Constraints:
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.
"""

"""
Note:
1. one pass (while + for): O(n) time | O(n) space - where n is the length of common prefix
2. one pass (for + for): O(n) time | O(1) space - where n is the length of common prefix
find the shortest string first
"""

from typing import List
class Solution(object):
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefixEndIndex = 0
        while True:
            if len(strs[0]) == prefixEndIndex:
                return strs[0]
            char = strs[0][prefixEndIndex]
            for str in strs:
                if len(str) == prefixEndIndex or char != str[prefixEndIndex]:
                    return str[:prefixEndIndex]
            prefixEndIndex += 1

    def longestCommonPrefix2(self, strs: List[str]) -> str:
        if not strs:
            return ""
        shortest = min(strs, key=len)
        for i, char in enumerate(shortest):
            for str in strs:
                if str[i] != char:
                    return shortest[:i]
        return shortest


# Unit Tests
import unittest
funcs = [Solution().longestCommonPrefix, Solution().longestCommonPrefix2]

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
