"""
219. Contains Duplicate II
description: https://leetcode.com/problems/contains-duplicate-ii/description/
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
