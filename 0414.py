"""
414. Third Maximum Number
Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

Example1:
Input: nums = [3,2,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2.
The third distinct maximum is 1.

Example2:
Input: nums = [1,2]
Output: 2
Explanation:
The first distinct maximum is 2.
The second distinct maximum is 1.
The third distinct maximum does not exist, so the maximum (2) is returned instead.

Example3:
Input: nums = [2,2,3,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2 (both 2's are counted together since they have the same value).
The third distinct maximum is 1.

Constraints:
1 <= nums.length <= 10^4
-2^31 <= nums[i] <= 2^31 - 1

Follow up: Can you find an O(n) solution?
"""

"""
Note:
1. Hash Table: O(n) time | O(n) space
2. minHeap: O(n) time | O(1) space
"""
import heapq
from typing import List
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        numSet = set(nums)
        if len(numSet) < 3:
            return max(numSet)
        numSet.remove(max(numSet))
        numSet.remove(max(numSet))
        return max(numSet)

    def thirdMax2(self, nums: List[int]) -> int:
        minHeap = []
        for num in nums:
            if num in minHeap:
                continue
            if len(minHeap) < 3:
                heapq.heappush(minHeap, num)
            else:
                heapq.heappushpop(minHeap, num)
        if len(minHeap) < 3:
            return minHeap[-1]
        return minHeap[0]

# Unit Tests
import unittest
funcs = [Solution().thirdMax, Solution().thirdMax2]


class TestThirdMax(unittest.TestCase):
    def testThirdMax1(self):
        for func in funcs:
            nums = [3,2,1]
            self.assertEqual(func(nums=nums), 1)

    def testThirdMax2(self):
        for func in funcs:
            nums = [1, 2]
            self.assertEqual(func(nums=nums), 2)

    def testThirdMax3(self):
        for func in funcs:
            nums = [2, 2, 3, 1]
            self.assertEqual(func(nums=nums), 1)

if __name__ == "__main__":
    unittest.main()
