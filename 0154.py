"""
154. Find Minimum in Rotated Sorted Array II
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0, 1, 2, 4, 5, 6, 7] might become:
- [4, 5, 6, 7, 0, 1, 2] if it was rotated 4 times.
- [0, 1, 2, 4, 5, 6, 7] if it was rotated 7 times.

Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums that may contain duplicates, return the minimum element of this array.

You must decrease the overall operation steps as much as possible.

Example1:
Input: nums = [1,3,5]
Output: 1

Example2:
Input: nums = [2,2,2,0,1]
Output: 0

Constraints:
n == nums.length
1 <= n <= 5000
-5000 <= nums[i] <= 5000
nums is sorted and rotated between 1 and n times.

Follow up: This problem is similar to Find Minimum in Rotated Sorted Array, but nums may contain duplicates. Would this affect the runtime complexity? How and why?
"""

"""
Note:
1. Iterative Binary Search: O(n) time | O(1) space
(1) if nums[mid] > nums[left]: move left to mid + 1
(2) if nums[mid] < nums[left]: move right to mid
(3) if nums[mid] == nums[left]: left += 1

2. Recursive Binary Search: O(n) time | O(n) space 
(1) One or two element, solve it directly
(2) if sorted: return nums[left]
(3) Recursively find the solution: return min(leftPart, rightPart)
"""

from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)
        minVal = nums[0]
        while left < right:
            if nums[left] < nums[right-1]:
                minVal = min(minVal, nums[left])
                break
            mid = left + (right - left) // 2
            minVal = min(minVal, nums[mid])
            if nums[mid] > nums[left]:
                left = mid + 1
            elif nums[mid] < nums[left]:
                right = mid
            else:
                left += 1
        return minVal

    def findMin2(self, nums: List[int]) -> int:
        return self.findMinHelper(nums, 0, len(nums) - 1)
    
    def findMinHelper(self, nums: List[int], left: int, right: int) -> int:
        # One or two element, solve it directly
        if left+1 >= right:
            return min(nums[left], nums[right])
        
        # Sorted
        if nums[left] < nums[right]:
            return nums[left]
        
        # Recursively find the solution
        mid = left + (right - left) // 2
        return min(self.findMinHelper(nums, left, mid-1), self.findMinHelper(nums, mid, right))


# Unit Tests
import unittest
funcs = [Solution().findMin, Solution().findMin2]

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
