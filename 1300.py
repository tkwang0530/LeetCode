"""
1300. Sum of Mutated Array Closest to Target
Given an integer array arr and a target value target, return the integer value such that when we change all the integers larger than value, the sum of the array gets as close as possible (in absolute difference) to target.

In case of a tie, return the minimum such integer.

Notice that the answer is not neccesarilly a number from arr.

Example1:
Input: arr = [4,9,3], target = 10
Output: 3
Explanation: When using 3 arr converts to [3, 3, 3] which sums 9 and that's the optimal answer.

Example2:
Input: arr = [2,3,5], target = 10
Output: 5

Example3:
Input: arr = [60864,25176,27249,21296,20204], target = 56803
Output: 11361

Constraints:
1 <= arr.length <= 10^4
1 <= arr[i], target <= 10^5
"""

"""
Note:
1. Binary Search: O(nlogn) time | O(1) space
"""
from typing import List

class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        def calculate(value) -> int:
            currentSum = 0
            for num in arr:
                toAdd = num if num < value else value
                currentSum += toAdd
            return abs(currentSum - target)

        left, right = 0, target+1
        while left < right:
            mid = left + (right - left) // 2
            scoreLeft = calculate(mid)
            scoreRight = calculate(mid+1)
            
            if scoreLeft <= scoreRight:
                right = mid
            else:
                left = mid+1
        return left

# Unit Tests
import unittest
funcs = [Solution().findBestValue]

class TestFindBestValue(unittest.TestCase):
    def testFindBestValue1(self):
        for func in funcs:
            arr = [4,9,3]
            target = 10
            self.assertEqual(func(arr=arr, target=target), 3)

    def testFindBestValue2(self):
        for func in funcs:
            arr = [2,3,5]
            target = 10
            self.assertEqual(func(arr=arr, target=target), 5)

    def testFindBestValue3(self):
        for func in funcs:
            arr = [60864,25176,27249,21296,20204]
            target = 56803
            self.assertEqual(func(arr=arr, target=target), 11361)

if __name__ == "__main__":
    unittest.main()