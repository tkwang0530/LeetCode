"""
2418. Sort the People
description: https://leetcode.com/problems/sort-the-people/description/
"""

"""
Note:
1. Sort: O(nlogn) time | O(n) space - where n is the length of array names
"""

import unittest
from typing import List
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [name for name, _ in sorted(zip(names, heights), key=lambda x: -x[1])]

# Unit Tests
funcs = [Solution().sortPeople]


class TestSortPeople(unittest.TestCase):
    def testSortPeople1(self):
        for sortPeople in funcs:
            names = ["Mary","John","Emma"]
            heights = [180,165,170]
            self.assertEqual(sortPeople(names=names, heights=heights), ["Mary","Emma","John"])
    def testSortPeople2(self):
        for sortPeople in funcs:
            names = ["Alice","Bob","Bob"]
            heights = [155,185,150]
            self.assertEqual(sortPeople(names=names, heights=heights), ["Bob","Alice","Bob"])

if __name__ == "__main__":
    unittest.main()
