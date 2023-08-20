"""
1534. Count Good Triplets
description: https://leetcode.com/problems/count-good-triplets/description/
"""

"""
Note:
1. Brute-Force: O(n^3) time | O(1) space - where n is the length of array arr
"""

from typing import List
class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        n = len(arr)
        goods = 0
        for i in range(n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    if abs(arr[i]-arr[j]) <= a and abs(arr[j]-arr[k]) <= b and abs(arr[i]-arr[k]) <= c:
                        goods += 1
        return goods

# Unit Tests
import unittest
funcs = [Solution().countGoodTriplets]
class TestCountGoodTriplets(unittest.TestCase):
    def testCountGoodTriplets1(self):
        for countGoodTriplets in funcs:
            arr = [3,0,1,1,9,7]
            a = 7
            b = 2
            c = 3
            self.assertEqual(countGoodTriplets(arr=arr, a=a, b=b, c=c), 4)

    def testCountGoodTriplets2(self):
        for countGoodTriplets in funcs:
            arr = [1,1,2,2,3]
            a = 0
            b = 0
            c = 1
            self.assertEqual(countGoodTriplets(arr=arr, a=a, b=b, c=c), 0)

if __name__ == "__main__":
    unittest.main()
