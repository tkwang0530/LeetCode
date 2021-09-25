"""
153. Find Minimum in Rotated Sorted Array
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0, 1, 2, 4, 5, 6, 7] might become:
- [4, 5, 6, 7, 0, 1, 2] if it was rotated 4 times.
- [0, 1, 2, 4, 5, 6, 7] if it was rotated 7 times.

Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(logn) time.

Example1:
Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.

Example2:
Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

Example3:
Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 

Constraints:
n == nums.length
1 <= n <= 5000
-5000 <= nums[i] <= 5000
All the integers of nums are unique.
nums is sorted and rotated between 1 and n times.
"""

"""
Note:
1. Binary Search: O(logn) time | O(1) space
if nums[mid] >= nums[left]: move left, otherwise move right 
"""

from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)
        minVal = nums[0]
        while left < right:
            mid = left + (right - left) // 2
            if nums[left] < nums[right-1]:
                minVal = min(minVal, nums[left])
                break
            minVal = min(minVal, nums[mid])
            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid
        return minVal

# Unit Tests
import unittest
funcs = [Solution().findMin]

class TestFindMin(unittest.TestCase):
    def testFindMin1(self):
        for func in funcs:
            nums = [3,4,5,1,2]
            self.assertEqual(func(nums=nums), 1)
    
    def testFindMin2(self):
        for func in funcs:
            nums = [4,5,6,7,0,1,2]
            self.assertEqual(func(nums=nums), 0)

    def testFindMin3(self):
        for func in funcs:
            nums = [11,13,15,17]
            self.assertEqual(func(nums=nums), 11)

if __name__ == "__main__":
    unittest.main()
