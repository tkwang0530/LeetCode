
"""
954. Array of Doubled Pairs
description: https://leetcode.com/problems/array-of-doubled-pairs/description/
"""

"""
Note:
1. Counter + Sort: O(n + klogk) time | O(k) space - where n is the length of nums and k is the number of unique elements in nums
"""

import collections
from typing import List
class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        numCounter = collections.Counter(arr)
        for num in sorted(numCounter.keys()):
            if numCounter[num] == 0:
                continue
            if num == 0:
                if num % 2 != 0:
                    return False
                else:
                    numCounter[num] = 0
            elif num < 0:
                if num % 2 == 0 and num // 2 in numCounter and numCounter[num // 2] >= numCounter[num]:
                    numCounter[num // 2] -= numCounter[num]
                    numCounter[num] = 0
                else:
                    return False
            else:
                if num * 2 in numCounter and numCounter[num*2] >= numCounter[num]:
                    numCounter[num*2] -= numCounter[num]
                    numCounter[num] = 0
                else:
                    return False

        return True

# Unit Tests
import unittest
funcs = [Solution().canReorderDoubled]

class TestCanReorderDoubled(unittest.TestCase):
    def testCanReorderDoubled1(self):
        for canReorderDoubled in funcs:
            arr = [3,1,3,6]
            self.assertEqual(canReorderDoubled(arr=arr), False)

    def testCanReorderDoubled2(self):
        for canReorderDoubled in funcs:
            arr = [2,1,2,6]
            self.assertEqual(canReorderDoubled(arr=arr), False)

    def testCanReorderDoubled3(self):
        for canReorderDoubled in funcs:
            arr = [4,-2,2,-4]
            self.assertEqual(canReorderDoubled(arr=arr), True)

if __name__ == "__main__":
    unittest.main()