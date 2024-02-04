"""
1711. Count Good Meals
description: https://leetcode.com/problems/count-good-meals/description/
"""

"""
Note:
1. HashMap + Counter: O(22 * n) time | O(n) space - where n is the length of array deliciousness
"""

import collections
from typing import List
class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        goodMealSet = {2**i for i in range(22)}
        numCount = collections.defaultdict(int)
        MOD = 10**9 + 7
        output = 0
        for num in deliciousness:
            for goodMeal in goodMealSet:
                if goodMeal - num in numCount:
                    output += numCount[goodMeal-num]
            numCount[num] += 1
        return output % MOD

# Unit Tests
import unittest
funcs = [Solution().countPairs]
class TestCountPairs(unittest.TestCase):
    def testCountPairs1(self):
        for func in funcs:
            deliciousness = [1,3,5,7,9]
            self.assertEqual(func(deliciousness=deliciousness), 4)

    def testCountPairs2(self):
        for func in funcs:
            deliciousness = [1,1,1,3,3,3,7]
            self.assertEqual(func(deliciousness=deliciousness), 15)

if __name__ == "__main__":
    unittest.main()
