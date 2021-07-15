"""
503. Next Greater Element II
Given a circular integer array nums (i.e., the next element of nums[nums.length - 1]) is nums[0]), return the next greater number for every element in nums.

The next greater number of a number x is the first greater to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.


Example1:
Input: nums = [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number. 
The second 1's next greater number needs to search circularly, which is also 2.

Example2:
Input: nums = [1,2,3,4,3]
Output: [2,3,4,-1,4]
"""

"""
Note:
1. Using Stack: O(n) time | O(n) space
"""




from typing import List
import unittest
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        result = [-1] * len(nums)
        stack = []
        for idx in range(2 * len(nums)):
            circularIdx = idx % len(nums)
            while stack and nums[stack[-1]] < nums[circularIdx]:
                top = stack.pop()
                result[top] = nums[circularIdx]
            stack.append(circularIdx)
        return result


# Unit Tests
funcs = [Solution().nextGreaterElements]


class TestNextGreaterElements(unittest.TestCase):
    def testNextGreaterElements1(self):
        for func in funcs:
            nums = [1, 2, 1]
            self.assertEqual(func(nums=nums), [2, -1, 2])

    def testNextGreaterElements2(self):
        for func in funcs:
            nums = [1, 2, 3, 4, 3]
            self.assertEqual(func(nums=nums), [2, 3, 4, -1, 4])


if __name__ == "__main__":
    unittest.main()
