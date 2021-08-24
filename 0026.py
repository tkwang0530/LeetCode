"""
26. Remove Duplicates from Sorted Array
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that unique element appears only once. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some language, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

Example1:
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

Example2:
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

Constraints:
0 <= nums.length <= 3 * 10^4
-100 <= nums[i] <= 100
nums is sorted in non-decreasing order.
"""

"""
Note:
1. Two Pointer(index and i): O(n) time | O(1) space
"""

from typing import List
import unittest
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 0
        preNum = None
        for num in nums:
            if num != preNum:
                nums[index] = num
                index += 1
                preNum = num
        return index



# Unit Tests
funcs = [Solution().removeDuplicates]


class TestRemoveDuplicates(unittest.TestCase):
    def testRemoveDuplicates1(self):
        for func in funcs:
            nums = [1,1,2]
            self.assertEqual(func(nums=nums), 2)
            self.assertEqual(nums[0:2], [1, 2])

    def testRemoveDuplicates2(self):
        for func in funcs:
            nums = [0,0,1,1,1,2,2,3,3,4]
            self.assertEqual(func(nums=nums), 5)
            self.assertEqual(nums[0:5], [0,1,2,3,4])

if __name__ == "__main__":
    unittest.main()
