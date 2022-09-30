"""
2420. Find All Good Indices
You are given a 0-indexed integer array nums of size n and a positive integer k.
We call an index i in the range k <= i < n - k good if the following conditions are satisfied:
- The k elements that are just before the index i are non-increasing order.
- The k elements that are just after the index i are in non-decreasing order.

Return an array of all good indices sorted in increasing order.

Example1:
Input: nums = [2,1,1,1,3,4,1], k = 2
Output: [2,3]
Explanation: There are two good indices in the array:
- Index 2. The subarray [2,1] is in non-increasing order, and the subarray [1,3] is in non-decreasing order.
- Index 3. The subarray [1,1] is in non-increasing order, and the subarray [3,4] is in non-decreasing order.
Note that the index 4 is not good because [4,1] is not non-decreasing.

Example2:
Input: nums = [2,1,1,2], k = 2
Output: []
Explanation: There are no good indices in this array.

Constraints:
n == nums.length
3 <= n <= 10^5
1 <= nums[i] <= 10^6
1 <= k <= n / 2
"""

"""
Note:
1. DP: O(n) time | O(n) space - where n is the length of array nums
"""




from typing import List
import unittest
class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        left = [1] * n
        right = [1] * n
        for i in range(1, n):
            if nums[i-1] >= nums[i]:
                left[i] = left[i-1] + 1

            if nums[~i] <= nums[~i + 1]:
                right[~i] = right[~i + 1] + 1

        output = []
        for i in range(k, n-k):
            if left[i-1] >= k and right[i+1] >= k:
                output.append(i)
        return output


# Unit Tests
funcs = [Solution().goodIndices]


class TestGoodIndices(unittest.TestCase):
    def testGoodIndices1(self):
        for func in funcs:
            nums = [2, 1, 1, 1, 3, 4, 1]
            k = 2
            self.assertEqual(func(nums=nums, k=k), [2, 3])

    def testGoodIndices2(self):
        for func in funcs:
            nums = [2, 1, 1, 2]
            k = 2
            self.assertEqual(func(nums=nums, k=k), [])


if __name__ == "__main__":
    unittest.main()
