"""
747. Largest Number At Least Twice of Others
You are given an integer array nums where the largest integer is unique.

Determine whether the largest element in the array is at least twice as much as every other number in the array. If it is, return the index of the largest element, or return -1 otherwise.

Example1:
Input: nums = [3,6,1,0]
Output: 1
Explanation: 6 is the largest integer.
For every other number in the array x, 6 is at least twice as big as x.
The index of value 6 is 1, so we return 1.

Example2:
Input: nums = [1,2,3,4]
Output: -1
Explanation: 4 is less than twice the value of 3, so we return -1.

Constraints:
2 <= nums.length <= 50
0 <= nums[i] <= 100
The largest element in nums is unique.
"""

"""
Note:
1. minHeap: O(nlog(2)) time | O(2) space - where n is the length of array nums
"""




import unittest
import heapq
from typing import List
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        minHeap = []
        for i, num in enumerate(nums):
            if len(minHeap) < 2:
                heapq.heappush(minHeap, (num, i))
            else:
                heapq.heappushpop(minHeap, (num, i))
        return minHeap[1][1] if minHeap[0][0] * 2 <= minHeap[1][0] else -1


# Unit Tests
funcs = [Solution().dominantIndex]


class TestDominantIndex(unittest.TestCase):
    def testDominantIndex1(self):
        for func in funcs:
            nums = [3, 6, 1, 0]
            self.assertEqual(func(nums=nums), 1)

    def testDominantIndex2(self):
        for func in funcs:
            nums = [1, 2, 3, 4]
            self.assertEqual(func(nums=nums), -1)


if __name__ == "__main__":
    unittest.main()
