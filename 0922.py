"""
922. Sort Array By Parity II
Given an array of integers nums, half of the integers in nums are odd, and the other half are even.

Sort the array so that whenever nums[i] is odd, i is odd, and whenever nums[i] is even, i is even.

Return any answer array that satisfies this condition

Example1:
Input: nums = [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.

Example2:
Input: nums = [2,3]
Output: [2,3]

Constraints:
2 <= nums.length <= 2 * 10^4
nums.length is even.
Half of the integers in nums are even.
0 <= nums[i] <= 1000

Follow up: Could you solve it in-place?
"""

"""
Note:
1. Two Pointers: O(n) time | O(1) space
"""

from typing import List
class Solution(object):
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        oddIdx = 1
        evenIdx = 0
        while oddIdx <= len(nums) - 1 and nums[oddIdx] % 2 == 1:
            oddIdx += 2
        while evenIdx <= len(nums) - 1 and nums[evenIdx] % 2 == 0:
            evenIdx += 2
        
        while oddIdx <= len(nums) - 1 and evenIdx <= len(nums) - 1:
            self.swap(oddIdx, evenIdx, nums)
            oddIdx += 2
            evenIdx += 2
            while oddIdx <= len(nums) - 1 and nums[oddIdx] % 2 == 1:
                oddIdx += 2
            while evenIdx <= len(nums) - 1 and nums[evenIdx] % 2 == 0:
                evenIdx += 2
            
        return nums
    
    def swap(self, i, j, nums):
        nums[i], nums[j] = nums[j], nums[i]

# Unit Tests
import unittest
funcs = [Solution().sortArrayByParityII]

class TestSortArrayByParityII(unittest.TestCase):
    def testSortArrayByParityII1(self):
        for func in funcs:
            nums = [4,2,5,7]
            self.assertTrue(func(nums=nums) in ([4,5,2,7], [4,7,2,5], [2,7,4,5], [2,5,4,7] ))

    def testSortArrayByParityII2(self):
        for func in funcs:
            nums = [2, 3]
            self.assertEqual(func(nums=nums), [2, 3])

if __name__ == "__main__":
    unittest.main()
