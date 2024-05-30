
"""
1442. Count Triplets That Can Form Two Arrays of Equal XOR
description: https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/description/
"""

"""
Note:
1. rangeXOR: O(n^3*32) time | O(32n) space - where n is the length of the input array
TLE
"""

from typing import List
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        preBitCount = [[0] * 32 for _ in range(n)]
        for i, num in enumerate(arr):
            numBitCount = [1 if b=="1" else 0 for b in bin(num)[2:].zfill(32)]
            if i == 0:
                preBitCount[i] = numBitCount
            else:
                preBitCount[i] = preBitCount[i-1].copy()
                for j in range(32):
                    preBitCount[i][j] += numBitCount[j]
        
        def rangeXOR(i, j) -> int:
            bitCount = [0] * 32

            ans = 0
            for k in range(32):
                if i-1 >= 0:
                    bitCount[k] = preBitCount[j][k]-preBitCount[i-1][k]
                else:
                    bitCount[k] = preBitCount[j][k]
                ans += 2 ** (31-k) * (bitCount[k] % 2)
            return ans
        
        triplets = 0
        for i in range(n-1):
            for j in range(i+1, n):
                for k in range(j, n):
                    if rangeXOR(i, j-1) == rangeXOR(j, k):
                        triplets += 1
        return triplets

# Unit Tests
import unittest
funcs = [Solution().countTriplets]

class TestCountTriplets(unittest.TestCase):
    def testCountTriplets1(self):
        for countTriplets in funcs:
            arr = [2,3,1,6,7]
            self.assertEqual(countTriplets(arr=arr), 4)

    def testCountTriplets2(self):
        for countTriplets in funcs:
            arr = [1,1,1,1,1]
            self.assertEqual(countTriplets(arr=arr), 10)

if __name__ == "__main__":
    unittest.main()