"""
896. Monotonic Array
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

Return true if and only if the given array nums is monotonic.

Example1:
Input: nums = [1,2,2,3]
Output: true

Example2:
Input: nums = [6,5,4,4]
Output: true

Example3:
Input: nums = [1,3,2]
Output: false

Example4:
Input: nums = [1,2,4,5]
Output: true

Example5:
Input: nums = [1,1,1]
Output: true

Constraints:
1 <= nums.length <= 50000
-100000 <= nums[i] <= 100000
"""

"""
Note:
1. track two vars (isNonDecreasing and isNonIncreasing): O(n) time | O(1) space
a. initiate isNonDecreasing, isNonIncreasing = True, True
b. Traverse the array and update those two vars
c. return isNonDecreasing or isNonIncreasing
2. check direction consistency: O(n) time | O(1) space
a. calculate direction in the first few steps
b. check if it breaksDirections during the traversing
"""




import unittest
from  typing import List
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        isNonDecreasing = True
        isNonIncreasing = True
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                isNonDecreasing = False
            if nums[i] > nums[i-1]:
                isNonIncreasing = False
        return isNonDecreasing or isNonIncreasing

    def isMonotonic2(self, nums: List[int]) -> bool:
        if len(nums) <= 2:
            return True
        direction = nums[1] - nums[0]
        for i in range(2, len(nums)):
            if direction == 0:
                direction = nums[i] - nums[i-1]
                continue
            if self.breaksDirection(direction, nums[i-1], nums[i]):
                return False
        return True

    def breaksDirection(self, direction: bool, previousInt, currentInt):
        difference = currentInt - previousInt
        if direction > 0:
            return difference < 0
        return difference > 0


# Unit Tests

funcs = [Solution().isMonotonic, Solution().isMonotonic2]


class TestIsMonotonic(unittest.TestCase):
    def testIsMonotonic1(self):
        for func in funcs:
            self.assertEqual(func(nums=[1, 2, 2, 3]), True)

    def testIsMonotonic2(self):
        for func in funcs:
            self.assertEqual(func(nums=[6, 5, 4, 4]), True)

    def testIsMonotonic3(self):
        for func in funcs:
            self.assertEqual(func(nums=[1, 3, 2]), False)

    def testIsMonotonic4(self):
        for func in funcs:
            self.assertEqual(func(nums=[1, 2, 4, 5]), True)

    def testIsMonotonic5(self):
        for func in funcs:
            self.assertEqual(func(nums=[1, 1, 1]), True)


if __name__ == "__main__":
    unittest.main()
