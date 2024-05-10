"""
496. Next Greater Element I
description: https://leetcode.com/problems/next-greater-element-i/description/
"""

"""
Notes:
1. monotonic stack: O(m+n) time | O(m+n) space - where n is the length of nums2, m is the length of nums1
"""
from typing import List
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = [-1] * len(nums1)
        numIndices = {num: i for i, num in enumerate(nums1)}
        stack = [] # [num]
        for num in nums2:
            while stack and stack[-1] < num:
                n = stack.pop()
                if n in numIndices:
                    output[numIndices[n]] = num
            stack.append(num)
        return output

# Unit Tests
import unittest
funcs = [Solution().nextGreaterElement]

class TestNextGreaterElement(unittest.TestCase):
    def testNextGreaterElement1(self):
        for func in funcs:
            nums1 = [4,1,2]
            nums2 = [1,3,4,2]
            self.assertEqual(func(nums1=nums1, nums2=nums2), [-1, 3, -1])

    def testNextGreaterElement2(self):
        for func in funcs:
            nums1 = [2,4]
            nums2 = [1,2,3,4]
            self.assertEqual(func(nums1=nums1, nums2=nums2), [3, -1])


if __name__ == "__main__":
    unittest.main()