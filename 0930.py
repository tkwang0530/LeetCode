"""
930. Binary Subarrays With Sum
description: https://leetcode.com/problems/binary-subarrays-with-sum/description/
"""

""" 
1. PreSum + Binary Search: O(n+nlogn) time | O(n) space - where n is array nums
2. PreSum + HashMap: O(n) time | O(n) space - where n is array nums
3. Sliding Window: O(n) time | O(1) space - where n is array nums
ref: https://leetcode.com/problems/binary-subarrays-with-sum/solutions/186683/c-java-python-sliding-window-o-1-space
"""
import bisect, collections
from typing import List

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        preSums = [0] * (n+1)
        for i in range(1, n+1):
            preSums[i] = preSums[i-1] + nums[i-1]
        
        count = 0
        for i in range(n):
            left = bisect.bisect_left(preSums, goal+preSums[i], lo=i+1)
            right = bisect.bisect_right(preSums, goal+preSums[i], lo=i+1)
            count += right-left
        return count

class Solution2:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        counter = collections.defaultdict(int)
        counter[0] = 1
        preSum = 0
        count = 0
        for num in nums:
            preSum += num
            count += counter[preSum-goal]
            counter[preSum] += 1
        return count
    
class Solution3:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def atMost(goal):
            if goal < 0:
                return 0

            count = start = 0
            current = 0
            for end in range(len(nums)):
                current += nums[end]
                while current > goal:
                    current -= nums[start]
                    start += 1
                count += end - start + 1
            return count
        return atMost(goal) - atMost(goal-1)

# Unit Tests
import unittest
funcs = [Solution().numSubarraysWithSum, Solution2().numSubarraysWithSum, Solution3().numSubarraysWithSum]


class TestNumSubarraysWithSum(unittest.TestCase):
    def testNumSubarraysWithSum1(self):
        for func in funcs:
            nums = [1,0,1,0,1]
            goal = 2
            self.assertEqual(func(nums=nums, goal=goal), 4)

    def testNumSubarraysWithSum2(self):
        for func in funcs:
            nums = [0,0,0,0,0]
            goal = 0
            self.assertEqual(func(nums=nums, goal=goal), 15)

if __name__ == "__main__":
    unittest.main()
