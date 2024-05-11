"""
898. Bitwise ORs of Subarrays
description: https://leetcode.com/problems/bitwise-ors-of-subarrays/description/
"""

"""
Note:
1.  PreSum concept: O(n^2) time | O(1) space - where n is the length of array arr
2. dp: O(log(max(arr)*n)) time | O(32) space - where n is the length of array arr 
"""

from typing import List
class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        n = len(arr)
        output = set()
        for i in range(n):
            runningVal = 0
            for j in range(i, n):
                runningVal |= arr[j]
                output.add(runningVal)
        return len(output)

class Solution2:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        n = len(arr)
        currentSet = set()
        output = set()
        for i in range(n):
            nextSet = {num | arr[i] for num in currentSet}
            nextSet.add(arr[i])

            output |= nextSet
            currentSet = nextSet
        return len(output)

# Unit Tests
import unittest
funcs = [Solution().subarrayBitwiseORs, Solution2().subarrayBitwiseORs]

class TestSubarrayBitwiseORs(unittest.TestCase):
    def testSubarrayBitwiseORs1(self):
        for func in funcs:
            arr = [0]
            self.assertEqual(func(arr), 1)

    def testSubarrayBitwiseORs2(self):
        for func in funcs:
            arr = [1,1,2]
            self.assertEqual(func(arr), 3)

    def testSubarrayBitwiseORs3(self):
        for func in funcs:
            arr = [1,2,4]
            self.assertEqual(func(arr), 6)

if __name__ == "__main__":
    unittest.main()