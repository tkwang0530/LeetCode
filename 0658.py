"""
658. Find K Closest Elements
Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:
- |a - x| < |b - x|, or
- |a - x| == |b - x| and a < b

Example1:
Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]

Example2:
Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]

Constraints:
1 <= k <= arr.length
1 <= arr.length <= 10^4
arr is sorted in ascending order.
-10^4 <= arr[i], x <= 10^4
"""

"""
Note:
1. Two Pointers: O(n) time | O(k) space - where n is the length of array arr
"""




from typing import List
import unittest
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr) - 1
        while right - left + 1 > k:
            leftVal, rightVal = arr[left], arr[right]
            if abs(leftVal - x) <= abs(rightVal - x):
                right -= 1
            else:
                left += 1
        return arr[left:right+1]


# Unit Tests
funcs = [Solution().findClosestElements]


class TestFindClosestElements(unittest.TestCase):
    def testFindClosestElements1(self):
        for func in funcs:
            arr = [1, 2, 3, 4, 5]
            k = 4
            x = 3
            self.assertEqual(func(arr=arr, k=k, x=x), [1, 2, 3, 4])

    def testFindClosestElements2(self):
        for func in funcs:
            arr = [1, 2, 3, 4, 5]
            k = 4
            x = -1
            self.assertEqual(func(arr=arr, k=k, x=x), [1, 2, 3, 4])


if __name__ == "__main__":
    unittest.main()
