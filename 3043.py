"""
3043. Find the Length of the Longest Common Prefix
description: https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/description/
"""

"""
Note:
1. HashTable: O(m+n) time | O(m) space - where m is the length of array arr1 and n is the length of array arr2
"""

from typing import List
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefixSet = set()
        for num in arr1:
            numStr = str(num)
            for i in range(1, len(numStr)+1):
                prefixSet.add(numStr[:i])
        
        longest = 0
        for num in arr2:
            numStr = str(num)
            for i in range(1, len(numStr)+1):
                prefix = numStr[:i]
                if prefix in prefixSet:
                    longest = max(longest, len(prefix))

        return longest

# Unit Tests
from typing import List
import unittest
funcs = [Solution().longestCommonPrefix]

class TestLongestCommonPrefix(unittest.TestCase):
    def testLongestCommonPrefix1(self):
        for func in funcs:
            arr1 = [1,10,100]
            arr2 = [1000]
            self.assertEqual(func(arr1=arr1, arr2=arr2), 3)

    def testLongestCommonPrefix2(self):
        for func in funcs:
            arr1 = [1,2,3]
            arr2 = [4,4,4]
            self.assertEqual(func(arr1=arr1, arr2=arr2), 0)

if __name__ == "__main__":
    unittest.main()
