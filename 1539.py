"""
1539. K+h Missing Positive Number
Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.
Find the kth positive integer that is missing from this array.

Example1:
Input: arr = [2, 3, 4, 7, 11], k = 5
Output: 9
Explanation: The missing positive integers are [1, 5, 6, 8, 9, 10, 12, 13]. The 5th missing positive integer is 9.

Example2:
Input: arr = [1, 2, 3, 4], k = 2
Output: 6
Explanation:The missing positive integers are [5, 6, 7, ...]. The 2nd missing positive integer is 6.

Constraints:
1 <= arr.length <= 1000
1 <= arr[i] <= 1000
1 <= k <= 1000
arr[i] < arr[j] for 1 <= i < j <= arr.length
"""

"""
Note:
1. Using set: O(n) time | O(n) space
2. Binary Search: O(logn) time | O(1) space
How many missing number between 1 and arr[mid]?
arr[mid] - (mid + 1)
"""

from typing import List
import unittest
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        if k < arr[0]:
            return k
        arrSet = set(arr)
        i = 1
        while i <= arr[len(arr) - 1]:
            if i not in arrSet:
                k -= 1
            if k == 0:
                return i
            i += 1
        return i + k - 1

    def findKthPositive2(self, arr: List[int], k: int) -> int:
        if k < arr[0]:
            return k
        left, right = 0, len(arr)
        while left < right:
            mid = (left + right) // 2
            if arr[mid] - (mid + 1) < k:
                left = mid + 1
            else:
                right = mid
        return left + k # existing + missing



# Unit Tests
funcs = [Solution().findKthPositive, Solution().findKthPositive2]


class TestFindKthPositive(unittest.TestCase):
    def testFindKthPositive1(self):
        for func in funcs:
            arr = [2, 3, 4, 7, 11]
            k = 5
            self.assertEqual(func(arr=arr, k=k), 9)

    def testFindKthPositive2(self):
        for func in funcs:
            arr = [1, 2, 3, 4]
            k = 2
            self.assertEqual(func(arr=arr, k=k), 6)

if __name__ == "__main__":
    unittest.main()
