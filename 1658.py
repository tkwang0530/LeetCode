"""
1658. Minimum Operations to Reduce X to Zero
You are given an integer array nums and an integer x. In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x. Note that this modifies the array for future operations.

Return the minimum number of operations to reduce x to exactly 0 if it is possible, otherwise, return -1.

Example1:
Input: nums = [1,1,4,2,3], x = 5
Output: 2
Explanation: The optimal solution is to remove the last two elements to reduce x to zero.

Example2:
Input: nums = [5,6,7,8,9], x = 4
Output: -1

Example3:
Input: nums = [3,2,20,1,1,3], x = 10
Output: 5
Explanation: The optimal solution is to remove the last three elements and the first two elements (5 operations in total) to reduce x to zero.

Constraints:
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^4
1 <= x <= 10^9
"""

"""
Note:
1. HashTable: O(n) time | O(n) space - where n is the length of array nums
"""




import unittest
from typing import List
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        leftSumIndex = {0: -1}
        currentSum = 0
        for i, num in enumerate(nums):
            currentSum += num
            leftSumIndex[currentSum] = i

        minOperations = float("inf")
        if x in leftSumIndex:
            minOperations = min(minOperations, leftSumIndex[x]+1)

        right = len(nums) - 1
        currentSum = 0
        while right >= 0:
            operations = len(nums) - right
            currentSum += nums[right]
            leftSum = x - currentSum
            if leftSum in leftSumIndex and leftSumIndex[leftSum] < right:
                minOperations = min(
                    minOperations, operations + leftSumIndex[leftSum] + 1)
            right -= 1

        return minOperations if minOperations != float("inf") else -1


# Unit Tests
funcs = [Solution().minOperations]


class TestMinOperations(unittest.TestCase):
    def testMinOperations1(self):
        for func in funcs:
            nums = [1, 1, 4, 2, 3]
            x = 5
            self.assertEqual(func(nums=nums, x=x), 2)

    def testMinOperations2(self):
        for func in funcs:
            nums = [5, 6, 7, 8, 9]
            x = 4
            self.assertEqual(func(nums=nums, x=x), -1)

    def testMinOperations3(self):
        for func in funcs:
            nums = [3, 2, 20, 1, 1, 3]
            x = 10
            self.assertEqual(func(nums=nums, x=x), 5)


if __name__ == "__main__":
    unittest.main()
