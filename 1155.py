"""
1155. Number of Dice Rolls With Target Sum
You have n dice and each die has k faces numbered from 1 to k.

Given three integers n, k, and target, return the number of possible ways (out of k^n total ways) to roll the dice so the sum of the face-up numbers equals target. Since the answer may be too large, return it modulo 10^9 + 7.

Example1:
Input: n = 1, k = 6, target = 3
Output: 1
Explanation: You throw one die with 6 faces.
There is only one way to get a sum of 3.

Example2:
Input: n = 2, k = 6, target = 7
Output: 6
Explanation: You throw two dice, each with 6 faces.
There are 6 ways to get a sum of 7: 1+6, 2+5, 3+4, 4+3, 5+2, 6+1.

Example3:
Input: n = 30, k = 30, target = 500
Output: 222616187
Explanation: The answer must be returned modulo 10^9 + 7.

Constraints:
1 <= n, k <= 30
1 <= target <= 1000
"""

"""
Note:
1. DFS(Bottom-up) + memo : O(n*target*k) time | O(n*target) space
"""

class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        memo = {}
        def dfs(n, target) -> int:
            if n*k < target or n*1 > target:
                return 0
            if n == 1:
                return 1
            
            if (n, target) in memo:
                return memo[(n, target)]
            result = 0
            for i in range(1, k+1):
                result += dfs(n-1, target-i)
                
            memo[(n, target)] = result
            return memo[(n, target)]
        
        return dfs(n, target) % (10**9 + 7)

# Unit Tests
import unittest
funcs = [Solution().numRollsToTarget]
class TestNumRollsToTarget(unittest.TestCase):
    def testNumRollsToTarget1(self):
        for func in funcs:
            n = 1
            k = 6
            target = 3
            self.assertEqual(func(n=n, k=k, target=target), 1)

    def testNumRollsToTarget2(self):
        for func in funcs:
            n = 2
            k = 6
            target = 7
            self.assertEqual(func(n=n, k=k, target=target), 6)

    def testNumRollsToTarget3(self):
        for func in funcs:
            n = 30
            k = 30
            target = 500
            self.assertEqual(func(n=n, k=k, target=target), 222616187)

if __name__ == "__main__":
    unittest.main()
