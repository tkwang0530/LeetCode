"""
2064. Minimized Maximum of Products Distributed to Any Store
description: https://leetcode.com/problems/minimized-maximum-of-products-distributed-to-any-store/description/ 
"""

"""
Note:
1. Binary Search: O(qlogm) time | O(1) space - where q is the length of array quantities, m is the max of quantities
"""

from typing import List
class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def condition(x) -> bool:
            count = 0
            for q in quantities:
                count += (q // x) + (q % x > 0)
            return count <= n
        
        left, right = 1, max(quantities)+1
        ans = right-1
        while left < right:
            x = left + (right-left)//2
            if condition(x):
                ans = x
                right = x
            else:
                left = x + 1
        return ans

import unittest
funcs = [Solution().minimizedMaximum]

class TestMinimizedMaximum(unittest.TestCase):
    def testMinimizedMaximum1(self):
        for func in funcs:
            n = 6
            quantities = [11,6]
            self.assertEqual(func(n=n, quantities=quantities), 3)

    def testMinimizedMaximum2(self):
        for func in funcs:
            n = 7
            quantities = [15,10,10]
            self.assertEqual(func(n=n, quantities=quantities), 5) 

    def testMinimizedMaximum3(self):
        for func in funcs:
            n = 1
            quantities = [100000]
            self.assertEqual(func(n=n, quantities=quantities), 100000) 

if __name__ == "__main__":
    unittest.main()
