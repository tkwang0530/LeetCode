"""
80. Remove Duplicates from Sorted Array II
Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

Example1:
Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

Example2:
Input: nums = [0,0,1,1,1,1,2,3,3]
Output: 7, nums = [0,0,1,1,2,3,3,_,_]
Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

Constraints:
1 <= nums.length <= 3 * 10^4
-10^4 <= nums[i] <= 10^4
nums is sorted in non-decreasing order.
"""

""" 
1. Two Pointers: O(n) time | O(1) space
"""
from typing import List
class Solution(object):
    def removeDuplicates(self, nums: List[int]) -> int:
        i = count = 0
        for num in nums:
            if nums[i-1] != num:
                count = 0
            
            if count == 2:
                continue
            
            # after this line, count < 2
            # so we should assign the value into result
            nums[i] = num
            count += 1
            i += 1
        return i 

# Unit Tests
import unittest
funcs = [Solution().removeDuplicates]


class TestRemoveDuplicates(unittest.TestCase):
    def testRemoveDuplicates1(self):
        for func in funcs:
            nums = [1,1,1,2,2,3]
            self.assertEqual(func(nums=nums), 5)
            self.assertEqual(nums[:5], [1, 1, 2, 2, 3])

    def testRemoveDuplicates2(self):
        for func in funcs:
            nums = [0,0,1,1,1,1,2,3,3]
            self.assertEqual(func(nums=nums), 7)
            self.assertEqual(nums[:7], [0, 0, 1, 1, 2, 3, 3])

if __name__ == "__main__":
    unittest.main()
