"""
167. Two Sum II - Input array is sorted
Given an array of integers that is already sorted in non-decreasing ordrer, find two numbers such that they add up to a specific target number.

Return the indices of the two numbers (1-indexed) as an integer array answer of size 2, where 1 <= answer[0] < answer[1] <= numbers.length.

The tests are generated such that there is exactly one solution. You may not use the same element twice.
Example1:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.

Example2:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.

Example3:
Input: numbers = [-1,0], target = -1
Output: [1,2]
"""

"""
Note:
1. Hash Table: O(n) time | O(n) space
2. Binary Search: O(nlogn) time | O(1) space
3. Two Pointers: O(n) time | O(1) space
"""




import unittest
from typing import List
class Solution(object):
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dict = {}
        for i, num in enumerate(numbers):
            if target - num in dict:
                return [dict[target - num]+1, i+1]
            else:
                dict[num] = i
        return

    def twoSum2(self, numbers: List[int], target: int) -> List[int]:
        for i, num in enumerate(numbers):
            j = self.binarySearch(
                numbers, i+1, len(numbers) - 1, target - num)
            if j != -1:
                return [i+1, j+1]
        return

    def binarySearch(self, numbers: List[int], left: int, right: int, target: int) -> int:
        while left <= right:
            mid = (left + right) // 2
            if numbers[mid] < target:
                left = mid + 1
            elif numbers[mid] > target:
                right = mid - 1
            else:
                return mid
        return -1

    def twoSum3(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left <= right:
            total = numbers[left] + numbers[right]
            if total == target:
                return [left+1, right+1]
            elif total > target:
                right -= 1
            elif total < target:
                left += 1
        return [-1, -1]


# Unit Tests
funcs = [Solution().twoSum, Solution().twoSum2, Solution().twoSum3]


class TestTwoSum(unittest.TestCase):
    def testTwoSum1(self):
        for func in funcs:
            numbers = [2, 7, 11, 15]
            self.assertEqual(
                func(numbers=numbers, target=9), [1, 2])

    def testTwoSum2(self):
        for func in funcs:
            numbers = [2, 3, 4]
            self.assertEqual(
                func(numbers=numbers, target=6), [1, 3])

    def testTwoSum3(self):
        for func in funcs:
            numbers = [-1, 0]
            self.assertEqual(
                func(numbers=numbers, target=-1), [1, 2])


if __name__ == "__main__":
    unittest.main()
