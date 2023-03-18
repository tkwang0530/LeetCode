"""
2567. Minimum Score by Changing Two Elements
You are given a 0-indexed integer array nums.

The low score of nums is the minimum value of |nums[i] - nums[j]| over all 0 <= i < j < nums.length.
The high score of nums is the maximum value of |nums[i] - nums[j]| over all 0 <= i < j < nums.length.
The score of nums is the sum of the high and low scores of nums.
To minimize the score of nums, we can change the value of at most two elements of nums.

Return the minimum possible score after changing the value of at most two elements of nums.

Note that |x| denotes the absolute value of x.

Example1:
Input: nums = [1,4,3]
Output: 0
Explanation: Change value of nums[1] and nums[2] to 1 so that nums becomes [1,1,1]. Now, the value of |nums[i] - nums[j]| is always equal to 0, so we return 0 + 0 = 0.

Example2:
Input: nums = [1,4,7,8,5]
Output: 3
Explanation: Change nums[0] and nums[1] to be 6. Now nums becomes [6,6,7,8,5].
Our low score is achieved when i = 0 and j = 1, in which case |nums[i] - nums[j]| = |6 - 6| = 0.
Our high score is achieved when i = 3 and j = 4, in which case |nums[i] - nums[j]| = |8 - 5| = 3.
The sum of our high and low score is 3, which we can prove to be minimal.

Constraints:
3 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
"""

"""
Note:
1. Sorting: O(nlogn) time | O(1) space - where n is the length of array nums
2. Priority queue: O(nlog(3)) time | O(1) space - where n is the length of array nums
"""




from typing import List
import unittest
import heapq
class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        # [1,4,3]
        nums.sort()
        minVal = min(
            nums[-1] - nums[2],  # remove two smallest numbers
            nums[-3] - nums[0],  # remove two largest numbers
            nums[-2] - nums[1],  # remove largest and smallest numbers
        )
        return minVal

    def minimizeSum2(self, nums: List[int]) -> int:
        threshold = 3
        minHeap = []  # for finding the max three numbers
        maxHeap = []  # for finding the min three numbers
        for num in nums:
            if len(minHeap) == threshold:
                heapq.heappushpop(minHeap, num)
                heapq.heappushpop(maxHeap, -num)
            else:
                heapq.heappush(minHeap, num)
                heapq.heappush(maxHeap, -num)

        minHeap.sort()
        maxHeap = sorted([-num for num in maxHeap])

        return min(
            minHeap[-1]-maxHeap[-1],  # remove two smallest numbers
            minHeap[0]-maxHeap[0],  # remove two largest numbers
            minHeap[1]-maxHeap[1],  # remove largest and smallest numbers
        )


# Unit Tests
funcs = [Solution().minimizeSum, Solution().minimizeSum2]


class TestMinimizeSum(unittest.TestCase):
    def testMinimizeSum1(self):
        for func in funcs:
            nums = [1, 4, 3]
            self.assertEqual(func(nums=nums), 0)

    def testMinimizeSum2(self):
        for func in funcs:
            nums = [1, 4, 7, 8, 5]
            self.assertEqual(func(nums=nums), 3)


if __name__ == "__main__":
    unittest.main()
