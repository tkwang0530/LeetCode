"""
220. Contains Duplicate III
Given an integer array nums and two integers k and t, return true if there are two distinct indices i and j in the array such that abs(nums[i] - nums[j]) <= t and abs(i-j) <= k

Example1:
Input: nums = [1,2,3,1], k = 3, t = 0
Output: true

Example2:
Input: nums = [1,0,1,1], k = 1, t = 2
Output: true

Example3:
Input: nums = [1,5,9,1,5,9], k = 2, t = 3
Output: false

Constraints:
0 <= nums.length <= 2 * 10^4
-2^31 <= nums[i] <= 2^31 - 1
0 <= k <= 10^4
0 <= t <= 2^31 - 1
"""

""" 
1. Brute Force: O(n * k) time | O(1) space
2. Bucket Sort Concept + Sliding Window: O(n) time | O(k) space
"""


from typing import List
import unittest
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t:int) -> bool:
        if t == 0 and len(nums) == len(set(nums)):
            return False
        if k == 0 or t < 0:
            return False
        for i, num in enumerate(nums):
            for j in range(i+1, min(i+k+1, len(nums))):
                if abs(num - nums[j]) <= t:
                    return True
        return False

    def containsNearbyAlmostDuplicate2(self, nums: List[int], k: int, t:int) -> bool:
        if t == 0 and len(nums) == len(set(nums)):
            return False
        if k == 0 or t < 0:
            return False
        bucket = {}
        for i, value in enumerate(nums):
            bucketIdx = value // (t + 1)
            if bucketIdx in bucket:
                return True
            if bucketIdx - 1 in bucket and abs(value - bucket[bucketIdx-1]) <= t:
                return True
            if bucketIdx + 1 in bucket and abs(value - bucket[bucketIdx+1]) <= t:
                return True
            if i >= k:
                del bucket[nums[i-k] // (t+1)]
            bucket[bucketIdx] = value
        return False


            


# Unit Tests
funcs = [Solution().containsNearbyAlmostDuplicate,Solution().containsNearbyAlmostDuplicate2]


class TestContainsNearbyAlmostDuplicate(unittest.TestCase):
    def testContainsNearbyAlmostDuplicate1(self):
        for func in funcs:
            nums = [1,2,3,1]
            k = 3
            t = 0
            self.assertEqual(func(nums=nums, k=k, t=t), True)

    def testContainsNearbyAlmostDuplicate2(self):
        for func in funcs:
            nums = [1,0,1,1]
            k = 1
            t = 2
            self.assertEqual(func(nums=nums, k=k, t=t), True)

    def testContainsNearbyAlmostDuplicate3(self):
        for func in funcs:
            nums = [1,5,9,1,5,9]
            k = 2
            t = 3
            self.assertEqual(func(nums=nums, k=k, t=t), False)


if __name__ == "__main__":
    unittest.main()
