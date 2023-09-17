"""
1566. Detect Pattern of Length M Repeated K or More Times
description: https://leetcode.com/problems/detect-pattern-of-length-m-repeated-k-or-more-times/description/
"""

""" 
1. Brute-Force: O(mn) time | O(mn) space - where n is the length of array arr
2. Count Matches: O(n) | O(1) space - where n is the length of array arr
"""

from typing import List
class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        n = len(arr)
        for i in range(n-m+1):
            element = arr[i:i+m]
            if i+m*k <= n and element*k == arr[i:i+m*k]:
                return True
        return False

class Solution2:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        n = len(arr)
        matches = 0
        for i in range(n-m):
            if arr[i] != arr[i+m]:
                matches = 0
                continue
            
            matches += 1
            if matches//m == k-1:
                return True
        return False

# Unit Tests
import unittest
funcs = [Solution().containsPattern, Solution2().containsPattern]


class TestContainsPattern(unittest.TestCase):
    def testContainsPattern1(self):
        for containsPattern in funcs:
            arr = [1,2,4,4,4,4]
            m = 1
            k = 3
            self.assertEqual(containsPattern(arr=arr, m=m, k=k), True)

    def testContainsPattern2(self):
        for containsPattern in funcs:
            arr = [1,2,1,2,1,1,1,3]
            m = 2
            k = 2
            self.assertEqual(containsPattern(arr=arr, m=m, k=k), True)

    def testContainsPattern3(self):
        for containsPattern in funcs:
            arr = [1,2,1,2,1,3]
            m = 2
            k = 3
            self.assertEqual(containsPattern(arr=arr, m=m, k=k), False)

if __name__ == "__main__":
    unittest.main()
