"""
1312. Minimum Insertion Steps to Make a String Palindrome
Given a string s. In one step you can insert any character at any index of the string.

Return the minimum number of steps to make s palindrome.

A Palindrome String is one that reads the same backward as well as forward.

Example1:
Input: s = "zzazz"
Output: 0
Explanation: The string "zzazz" is already palindrome we do not need any insertions.

Example2:
Input: s = "mbadm"
Output: 2
Explanation: String can be "mbdadbm" or "mdbabdm".

Example3:
Input: s = "leetcode"
Output: 5
Explanation: Inserting 5 characters the string becomes "leetcodocteel".

Constraints:
1 <= s.length <= 500
s consists of lowercase English letters.
"""

"""
Note:
1. Two Pointers + dfs + memo: O(n^2) time | O(n^2) space - where n is the length of string s
"""

import unittest
import functools
class Solution:
    def minInsertions(self, s: str) -> int:
        @functools.lru_cache(None)
        def dfs(left, right):
            if right - left <= 0:
                return 0
            
            if s[right] == s[left]:
                return dfs(left+1, right-1)
            return min(1+dfs(left+1, right), 1+dfs(left, right-1))

        return dfs(0, len(s)-1)

# Unit Tests
funcs = [Solution().minInsertions]


class TestMinInsertions(unittest.TestCase):
    def testMinInsertions1(self):
        for func in funcs:
            s = "mbadm"
            self.assertEqual(func(s=s), 2)

    def testMinInsertions2(self):
        for func in funcs:
            s = "zzazz"
            self.assertEqual(func(s=s), 0)

    def testMinInsertions3(self):
        for func in funcs:
            s = "leetcode"
            self.assertEqual(func(s=s), 5)


if __name__ == "__main__":
    unittest.main()
