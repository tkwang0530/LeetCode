"""
219. Contains Duplicate II
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k

Example1:
Input: nums = [1,2,3,1], k = 3
Output: true

Example2:
Input: nums = [1,0,1,1], k = 1
Output: true

Example3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: false

Constraints:
1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
0 <= k <= 10^5
"""

""" 
1. Hash Table + Sliding Window: O(n) time | O(k) space
2. Hash Table store last seen index: O(n) time | O(n) space
"""


from typing import List
class Solution(object):
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()
        for i, num in enumerate(nums):
            if num in seen:
                return True
            seen.add(num)
            if len(seen) > k:
                seen.remove(nums[i-k])
        return False

    def containsNearbyDuplicate2(self, nums: List[int], k: int) -> bool:
        lastSeen = {} # <num, lastSeenIdx>
        for i, num in enumerate(nums):
            if num in lastSeen and abs(i - lastSeen[num]) <= k:
                return True
            lastSeen[num] = i
        return False

# Unit Tests
import unittest
funcs = [Solution().containsNearbyDuplicate, Solution().containsNearbyDuplicate2]


class TestContainsNearbyDuplicate(unittest.TestCase):
    def testContainsNearbyDuplicate1(self):
        for func in funcs:
            nums = [1,2,3,1]
            k = 3
            self.assertEqual(func(nums=nums, k=k), True)

    def testContainsNearbyDuplicate2(self):
        for func in funcs:
            nums = [1,0,1,1]
            k = 1
            self.assertEqual(func(nums=nums, k=k), True)

    def testContainsNearbyDuplicate3(self):
        for func in funcs:
            nums = [1,2,3,1,2,3]
            k = 2
            self.assertEqual(func(nums=nums, k=k), False)


if __name__ == "__main__":
    unittest.main()
