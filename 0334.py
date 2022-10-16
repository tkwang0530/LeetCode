"""
334. Increasing Triplet Subsequence
Given an integer array nums, return true if there exists a triple indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

Example1:
Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.

Example2:
Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.

Example3:
Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.

Constraints:
1 <= nums.length <= 5 * 10^5
-2^31 <= nums[i] <= 2^31 - 1

Follow up: Could you implement a solution that runs in O(n) time complexity and O(1) space complexity?
"""

"""
Notes:
1. One pass: O(n) time | O(1) space - where n is the length of array nums
Start with the maximum numbers for the first and second element. Then
(1) Find the first smallest numbe in the 3 subsequence
(2) Find the second one greater than the first element, reset the first one if it's smaller

2. PrefixMax + SuffixMax: O(n) time | O(n) space - where n is the length of array nums
"""




import unittest
from typing import List
class Solution(object):
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        first = second = float("inf")
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False

    def increasingTriplet2(self, nums: List[int]) -> bool:
        n = len(nums)
        prefixMin = [float("inf")] * (n+1)
        suffixMax = [float("-inf")] * (n+1)
        for i in range(1, n+1):
            prefixMin[i] = min(prefixMin[i-1], nums[i-1])

        for i in range(n-1, -1, -1):
            suffixMax[i] = max(suffixMax[i+1], nums[i])

        for i, num in enumerate(nums):
            if prefixMin[i] < num and suffixMax[i+1] > num:
                return True

        return False


# Unit Tests
funcs = [Solution().increasingTriplet, Solution().increasingTriplet2]


class TestIncreasingTriplet(unittest.TestCase):
    def testIncreasingTriplet1(self):
        for func in funcs:
            nums = [1, 2, 3, 4, 5]
            self.assertEqual(func(nums=nums), True)

    def testIncreasingTriplet2(self):
        for func in funcs:
            nums = [5, 4, 3, 2, 1]
            self.assertEqual(func(nums=nums), False)

    def testIncreasingTriplet3(self):
        for func in funcs:
            nums = [2, 1, 5, 0, 4, 6]
            self.assertEqual(func(nums=nums), True)


if __name__ == "__main__":
    unittest.main()
