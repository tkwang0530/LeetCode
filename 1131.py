"""
1131. Maximum of Absolute Value Expression
Given two arrays of integers with equal lengths, return the maximum value of:
|arr1[i] - arr1[j]| + |arr2[i] - arr2[j]| + |i-j|
where the maximum is taken over all 0 <= i, j < arr1.length

Example1:
Input: arr1 = [1,2,3,4], arr2 = [-1,4,5,6]
Output: 13

Example2:
Input: arr1 = [1,-2,-5,0,10], arr2 = [0,-2,-1,-7,-4]
Output: 20

Constraints:
2 <= arr1.length == arr2.length <= 40000
-10^6 <= arr1[i], arr2[i] <= 10^6
"""

"""
Note:
1. Maximum Manhattan Distance: O(n) time | O(1) space
Assume i < j, there are four possible expression:
|x[i] - x[j]| + |y[i] - y[j]| = (x[i] - x[j]|) + (y[i] - y[j]) = (x[i] + y[i]|) - (x[j] + y[j])
|x[i] - x[j]| + |y[i] - y[j]| = (x[i] - x[j]|) - (y[i] - y[j]) = (x[i] - y[i]|) - (x[j] - y[j])
|x[i] - x[j]| + |y[i] - y[j]| = -(x[i] - x[j]|) + (y[i] - y[j]) = (-x[i] + y[i]|) - (-x[j] + y[j])
|x[i] - x[j]| + |y[i] - y[j]| = -(x[i] - x[j]|) - (y[i] - y[j]) = (-x[i] - y[i]|) - (-x[j] - y[j])

So we can see, the expression
|x[i] - x[j]| + |y[i] - y[j]| + |i - j| = f(j) - f(i)

where f(i) = p * x[i] + q * y[i] + i
with p = 1 or -1, q = 1 or -1
"""

from typing import List

class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        result, n = 0, len(arr1)
        for p, q in [[1, 1], [1, -1], [-1, 1], [-1, -1]]:
            smallest = float("inf")
            largest = float("-inf")
            for i in range(n):
                current = p * arr1[i] + q * arr2[i] + i
                largest = max(largest, current)
                smallest = min(smallest, current)
            result = max(result, largest - smallest)
        return result

# Unit Tests
import unittest
funcs = [Solution().maxAbsValExpr]


class TestMaxAbsValExpr(unittest.TestCase):
    def testMaxAbsValExpr1(self):
        for func in funcs:
            arr1 = [1,2,3,4]
            arr2 = [-1,4,5,6]
            self.assertEqual(func(arr1=arr1, arr2=arr2), 13)

    def testMaxAbsValExpr2(self):
        for func in funcs:
            arr1 = [1,-2,-5,0,10]
            arr2 = [0,-2,-1,-7,-4]
            self.assertEqual(func(arr1=arr1, arr2=arr2), 20)
            
if __name__ == "__main__":
    unittest.main()