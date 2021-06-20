"""
217. Contains Duplicate
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value at least twice in the array, and it should return false if every element is distinct.

Example1:
Input: [1, 2, 3, 1]
Output: true

Example2:
Input: [1, 2, 3, 4]
Output: false

Example3:
Input: [1, 1, 1, 3, 3, 4 ,3, 2, 4, 2]
Output: true
"""

"""
Note:
1. Hash Table: O(n) time | O(n) space
2. Sorting: O(nlogn) time | O(1) space
If there are duplicate numbers, they will be adjacent in a sorted array
"""

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)

    def containsDuplicate2(self, nums: List[int]) -> bool:
        s = set()
        for num in nums:
            if num in s:
                return True
            s.add(num)
        return False

    def containsDuplicate3(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False


# Unit Tests
import unittest


class TestContainsDuplicate(unittest.TestCase):
    def testContainsDuplicate1(self):
        func = Solution().containsDuplicate
        func2 = Solution().containsDuplicate2
        func3 = Solution().containsDuplicate3
        self.assertEqual(func(nums=[1, 2, 3, 1]), True)
        self.assertEqual(func2(nums=[1, 2, 3, 1]), True)
        self.assertEqual(func3(nums=[1, 2, 3, 1]), True)

    def testContainsDuplicate2(self):
        func = Solution().containsDuplicate
        func2 = Solution().containsDuplicate2
        func3 = Solution().containsDuplicate3
        self.assertEqual(func(nums=[1, 2, 3, 4]), False)
        self.assertEqual(func2(nums=[1, 2, 3, 4]), False)
        self.assertEqual(func3(nums=[1, 2, 3, 4]), False)

    def testContainsDuplicate3(self):
        func = Solution().containsDuplicate
        func2 = Solution().containsDuplicate2
        func3 = Solution().containsDuplicate3
        self.assertEqual(func(nums=[1, 1, 1, 3, 3, 4, 3, 2, 4, 2]), True)
        self.assertEqual(func2(nums=[1, 1, 1, 3, 3, 4, 3, 2, 4, 2]), True)
        self.assertEqual(func3(nums=[1, 1, 1, 3, 3, 4, 3, 2, 4, 2]), True)


if __name__ == "__main__":
    unittest.main()