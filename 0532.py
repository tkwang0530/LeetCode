"""
532. K-diff Pairs in an Array
Given an array of integers nums and an integer k, return the number of unique k-diff pairs in the array.

A k-diff pair is an integer pair (nums[i], nums[j]), where the following are true:
- 0 <= i, j < nums.length
- i != j
- nums[i] - nums[j] == k

Example1:
Input: nums = [3,1,4,1,5], k = 2
Output: 2
Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of unique pairs.

Example2:
Input: nums = [1,2,3,4,5], k = 1
Output: 4
Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).

Example3:
Input: nums = [1,3,1,5,4], k = 0
Output: 1
Explanation: There is one 0-diff pair in the array, (1, 1).

Constraints:
1 <= nums.length <= 10^4
-10^7 <= nums[i] <= 10^7
0 <= k <= 10^7
"""

"""
Note:
1. HashTable + Backtracking: O(n) time | O(n) space
2. HashTable: O(n) time | O(n) space
"""

import collections
from typing import List
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        numCounts = collections.Counter(nums)
        result = set()
        for num in nums:
            numCounts[num] -= 1
            if numCounts[num-k] > 0:
                result.add((num-k, num))
            if numCounts[num+k] > 0:
                result.add((num, num+k))
            numCounts[num] += 1
        return len(result)

    def findPairs2(self, nums: List[int], k: int) -> int:
        visited = set()
        result = set()
        for num in nums:
            if num + k in visited:
                result.add((num, num+k))
            if num - k in visited:
                result.add((num-k, num))
            visited.add(num)
        return len(result)

# Unit Tests
import unittest
funcs = [Solution().findPairs, Solution().findPairs2]
class TestFindPairs(unittest.TestCase):
    def testFindPairs1(self):
        for func in funcs:
            nums = [3,1,4,1,5]
            k = 2
            self.assertEqual(func(nums=nums, k=k), 2)

    def testFindPairs2(self):
        for func in funcs:
            nums = [1,2,3,4,5]
            k = 1
            self.assertEqual(func(nums=nums, k=k), 4)

    def testFindPairs3(self):
        for func in funcs:
            nums = [1,3,1,5,4]
            k = 0
            self.assertEqual(func(nums=nums, k=k), 1)


if __name__ == "__main__":
    unittest.main()
