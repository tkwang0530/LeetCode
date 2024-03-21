"""
1239. Maximum Length of a Concatenated String with Unique Characters
description: https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/description/
"""

"""
Note:
1. backtracking: O(n) time | O(n) space - where n is the length of arr
"""

from typing import List
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        n = len(arr)
        container = [0]
        used = set()
        def dfs(i):
            nonlocal used
            if i == n or len(used) == 26:
                container[0] = max(container[0], len(used))
                return

            # not use
            dfs(i+1)

            # use if allow
            charSet = set(arr[i])
            if len(charSet) < len(arr[i]):
                return
            interSect = charSet & used
            if len(interSect) == 0:
                used |= charSet
                dfs(i+1)
                used ^= charSet
        dfs(0)
        return container[0]

# Unit Tests
import unittest
funcs = [Solution().maxLength]


class TestMaxLength(unittest.TestCase):
    def testMaxLength1(self):
        for func in funcs:
            arr = ["un","iq","ue"]
            self.assertEqual(func(arr=arr), 4)

    def testMaxLength2(self):
        for func in funcs:
            arr = ["cha","r","act","ers"]
            self.assertEqual(func(arr=arr), 6)

    def testMaxLength3(self):
        for func in funcs:
            arr = ["abcdefghijklmnopqrstuvwxyz"]
            self.assertEqual(func(arr=arr), 26)

if __name__ == "__main__":
    unittest.main()
