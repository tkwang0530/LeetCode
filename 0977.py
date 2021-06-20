"""
977. Squares of a Sorted Array
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Example1:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Example2:
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]

Constraints:
1 <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4
nums is sorted in non-decreasing order.

Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?
"""

"""
Note:
1. square and sort: O(nlogn) time | O(n) space
2. Two pointers: O(n) time | O(n) space
"""




import unittest
from  typing import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squares = [value ** 2 for value in nums]
        squares.sort()
        return squares

    def sortedSquares2(self, nums: List[int]) -> List[int]:
        sortedSquares = [0 for _ in nums]
        leftIdx = 0
        rightIdx = len(nums) - 1

        for idx in reversed(range(len(nums))):
            leftValue = nums[leftIdx]
            rightValue = nums[rightIdx]

            if abs(leftValue) > abs(rightValue):
                sortedSquares[idx] = leftValue ** 2
                leftIdx += 1
            else:
                sortedSquares[idx] = rightValue ** 2
                rightIdx -= 1
        return sortedSquares


# Unit Tests

funcs = [Solution().sortedSquares, Solution().sortedSquares2]


class TestSortedSquares(unittest.TestCase):
    def testSortedSquares1(self):
        for func in funcs:
            self.assertEqual(func(nums=[-4, -1, 0, 3, 10]), [0, 1, 9, 16, 100])

    def testSortedSquares2(self):
        for func in funcs:
            self.assertEqual(func(nums=[-7, -3, 2, 3, 11]), [4, 9, 9, 49, 121])


if __name__ == "__main__":
    unittest.main()
