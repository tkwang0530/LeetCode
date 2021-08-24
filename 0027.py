"""
27. Remove Element
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

Example1:
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).

Example2:
Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).

Constraints:
0 <= nums.length <= 100
0 <= nums[i] <= 50
0 <= val <= 100
"""

"""
Note:
1. Two Pointer(left and right): O(n) time | O(1) space
2. Two Pointer(index and i): O(n) time | O(1) space
"""


from typing import List
import unittest
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left] == val:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
            else:
                left += 1
        return left

    def removeElement2(self, nums: List[int], val: int) -> int:
        index = 0
        for num in nums:
            if num != val:
                nums[index] = num
                index += 1
        return index



# Unit Tests
funcs = [Solution().removeElement, Solution().removeElement2]


class TestRemoveElement(unittest.TestCase):
    def testRemoveElement1(self):
        for func in funcs:
            nums = [3,2,2,3]
            val = 3
            self.assertEqual(func(nums=nums, val=val), 2)
            self.assertEqual(sorted(nums[0:2]), sorted([2, 2]))

    def testRemoveElement2(self):
        for func in funcs:
            nums = [0,1,2,2,3,0,4,2]
            val = 2
            self.assertEqual(func(nums=nums, val=val), 5)
            self.assertEqual(sorted(nums[0:5]), sorted([0,1,4,0,3]))

if __name__ == "__main__":
    unittest.main()
