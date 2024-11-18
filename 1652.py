"""
1652. Defuse the Bomb
description: https://leetcode.com/problems/defuse-the-bomb/description/
"""

"""
Note:
1. prefixSum: O(2*n) time | O(2*n) space - where n is the length of array code 
"""

from typing import List
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        dp = [0] * n * 2
        if k == 0:
            return [0] * n
        
        if k > 0:
            for i in range(n+k):
                dp[i] = code[i%n] + (dp[i-1] if i-1 >= 0 else 0)
            return [dp[i+k]-dp[i] for i in range(n)]

        if k < 0:
            for i in range(2*n-1, -1, -1):
                dp[i] = code[i%n] + (dp[i+1] if i+1 <= 2*n-1 else 0)
            return [dp[i+n+k]-dp[i+n] for i in range(n)]

import unittest
funcs = [Solution().decrypt]

class TestDecrypt(unittest.TestCase):
    def testDecrypt1(self):
        for func in funcs:
            code = [5,7,1,4]
            k = 3
            self.assertEqual(func(code=code, k=k), [12,10,16,13])

    def testDecrypt2(self):
        for func in funcs:
            code = [1,2,3,4]
            k = 0
            self.assertEqual(func(code=code, k=k), [0,0,0,0]) 

    def testDecrypt3(self):
        for func in funcs:
            code = [2,4,9,3]
            k = -2
            self.assertEqual(func(code=code, k=k), [12,5,6,13]) 

if __name__ == "__main__":
    unittest.main()
