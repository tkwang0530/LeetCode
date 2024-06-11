"""
1122. Relative Sort Array
description: https://leetcode.com/problems/relative-sort-array/description/
"""

"""
Note:
1. Sort: O(m+n+mlogm) time | O(m+n) space - where m is the length of arr1 and n is the length of arr2
"""

from typing import List
import unittest

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        numIndice = {num: i for i, num in enumerate(arr2)}
        excluded = []
        included = []
        for num in arr1:
            if num not in numIndice:
                excluded.append(num)
            else:
                included.append(num)

        included.sort(key = lambda x: numIndice[x])
        return included + sorted(excluded)

# Unit Tests
funcs = [Solution().relativeSortArray]


class TestRelativeSortArray(unittest.TestCase):
    def testRelativeSortArray1(self):
        for func in funcs:
            arr1 = [2,3,1,3,2,4,6,7,9,2,19]
            arr2 = [2,1,4,3,9,6]
            self.assertEqual(func(arr1=arr1, arr2=arr2), [2,2,2,1,4,3,3,9,6,7,19])

    def testRelativeSortArray2(self):
        for func in funcs:
            arr1 = [28,6,22,8,44,17]
            arr2 = [22,28,8,6]
            self.assertEqual(func(arr1=arr1, arr2=arr2), [22,28,8,6,17,44])

if __name__ == "__main__":
    unittest.main()
