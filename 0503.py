"""
503. Next Greater Element II
description: https://leetcode.com/problems/next-greater-element-ii/description/
"""

"""
Note:
1. Using Stack: O(n) time | O(n) space
Tip: idx % len(nums) + range(2 * len(nums)) to traverse the nums two times
(1) Traverse the list two times
(2) During the traversal if stack is not None and the top number is less than the currentNum: 
    result[stack.pop()] = nums[circularIdx]
(3) store number's index into the stack
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
