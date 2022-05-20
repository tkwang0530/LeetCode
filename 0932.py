"""
932. Beautiful Array
An array nums of length n is beautiful if:
- nums is a permutation of the integers in the range [1, n].
- For every 0 <= i < j < n, there is no index k with i < k < j where 2 * nums[k] == nums[i] + nums[j].

Given the integer n, return any beautiful array nums of length n. There will be at least one valid answer for the given n.

Example1:
Input: n = 4
Output: [2,1,4,3]

Example2:
Input: n = 5
Output: [3,1,2,5,4]

Constraints:
1 <= n <= 1000
"""

""" 
Notes:
1. Divide and Conquer: O(nlogn) time | O(n) space
n * (1+1/2+1/4+...) = n * [1*(1-(1/2)^k)/(1/2)] = n * (1-(1/2)^k) * 2 = 2n * (1-1/n) = 2n - 2 ~= n 
"""

from typing import List
class Solution(object):
    def beautifulArray(self, n: int) -> List[int]:
        def recur(arr):
            if len(arr) <= 2:
                return arr
            return recur(arr[::2]) + recur(arr[1::2])
        
        return recur(list(range(1, n+1)))

# Unit Tests
import unittest
funcs = [Solution().beautifulArray]

def isBeautifulArray(arr):
    if len(arr) <= 2:
        return True
    
    for i in range(len(arr)-2):
        for k in range(i+1, len(arr) - 1):
            for j in range(k+1, len(arr)):
                if 2 * arr[k] == arr[i] + arr[j]:
                    return False
    return True


class TestBeautifulArray(unittest.TestCase):
    def testBeautifulArray1(self):
        for func in funcs:
            n = 4
            arr = func(n)
            self.assertEqual(isBeautifulArray(arr), True)

    def testBeautifulArray2(self):
        for func in funcs:
            n = 5
            arr = func(n)
            self.assertEqual(isBeautifulArray(arr), True)

if __name__ == "__main__":
    unittest.main()
