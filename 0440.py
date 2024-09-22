"""
440. K-th Smallest in Lexicographical Order
description: https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/description/ 
"""

"""
Note:
1. prefix tree: O((logn)^2) time | O(1) space
ref: https://youtu.be/wRubz1zhVqk?si=Cd9Zq--gUr7ZZ_u7
"""

class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        current = 1
        i = 1
        
        def count(current):
            output = 0
            next = current + 1
            while current <= n:
                output += min(next, n+1) - current
                current *= 10
                next *= 10
            return output
        
        while i < k:
            steps = count(current)
            if i + steps <= k:
                current += 1
                i += steps
            else:
                current *= 10
                i += 1

        return current

# Unit Tests
import unittest
funcs = [Solution().findKthNumber]

class TestFindKthNumber(unittest.TestCase):
    def testFindKthNumber1(self):
        for func in funcs:
            n = 13
            k = 2
            self.assertEqual(func(n=n, k=k), 10)
    def testFindKthNumber2(self):
        for func in funcs:
            n = 1
            k = 1
            self.assertEqual(func(n=n, k=k), 1)

if __name__ == "__main__":
    unittest.main()
