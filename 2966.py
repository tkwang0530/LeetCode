
"""
2966. Divide Array Into Arrays With Max Difference
description: https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/description/
"""

"""
Note:
1. Sort: O(nlogn) time | O(n) space - where n is the length of nums
"""

from typing import List
class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        output = []
        for i in range(0, n, 3):
            if nums[i+2]-nums[i] <= k:
                output.append(nums[i:i+3])
            else:
                return []
        return output


# Unit Tests
import unittest
funcs = [Solution().divideArray]

class TestDivideArray(unittest.TestCase):
    def testDivideArray1(self):
        for divideArray in funcs:
            nums = [1,3,4,8,7,9,3,5,1]
            k = 2
            self.assertEqual(divideArray(nums=nums, k=k), [[1,1,3],[3,4,5],[7,8,9]])

    def testDivideArray2(self):
        for divideArray in funcs:
            nums = [1,3,3,2,7,3]
            k = 3
            self.assertEqual(divideArray(nums=nums, k=k), [])

if __name__ == "__main__":
    unittest.main()