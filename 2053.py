"""
2053. Kth Distinct String in an Array
description: https://leetcode.com/problems/kth-distinct-string-in-an-array/description/
"""

"""
Note:
1. HashMap: O(n) time | O(n*5) space - where n is the length of the input array arr
"""

from typing import List
import collections
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counter = collections.Counter(arr)
        idx = 0
        for char in arr:
            if counter[char] == 1:
                idx += 1
            
            if idx == k:
                return char

        return ""

# Unit Tests
import unittest
funcs = [Solution().kthDistinct]
class TestKthDistinct(unittest.TestCase):
    def testKthDistinct1(self):
        for kthDistinct in funcs:
            arr = ["d","b","c","b","c","a"]
            k = 2
            self.assertEqual(kthDistinct(arr=arr, k=k), "a")

    def testKthDistinct2(self):
        for kthDistinct in funcs:
            arr = ["aaa","aa","a"]
            k = 1
            self.assertEqual(kthDistinct(arr=arr, k=k), "aaa")

    def testKthDistinct3(self):
        for kthDistinct in funcs:
            arr = ["a","b","a"]
            k = 3
            self.assertEqual(kthDistinct(arr=arr, k=k), "")

if __name__ == "__main__":
    unittest.main()
