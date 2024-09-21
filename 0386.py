"""
386. Lexicographical Numbers
description: https://leetcode.com/problems/lexicographical-numbers/description/
"""

"""
Note:
1. Backtracking (preorder): O(n) time | O(logn) space
2. Backtracking (iterative): O(n) time | O(1) space
ref: https://www.youtube.com/watch?v=QihtII-FvLo
"""

from typing import List
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        output = []
        def dfs(k):
            if k > n:
                return

            output.append(k)
            k *= 10

            for i in range(10):
                dfs(k + i)

        for i in range(1, 10):
            dfs(i)
        
        return output

class Solution2:
    def lexicalOrder(self, n: int) -> List[int]:
        output = []
        current = 1
        while len(output) < n:
            output.append(current)
            if current * 10 <= n:
                current *= 10
            else:
                while current % 10 == 9 or current == n:
                    current //= 10
                current += 1
        return output

# Unit Tests
import unittest
funcs = [Solution().lexicalOrder, Solution2().lexicalOrder]

class TestLexicalOrder(unittest.TestCase):
    def testLexicalOrder1(self):
        for func in funcs:
            n = 13
            self.assertEqual(func(n=n), [1,10,11,12,13,2,3,4,5,6,7,8,9])

    def testLexicalOrder2(self):
        for func in funcs:
            n =2
            self.assertEqual(func(n=n), [1,2])

if __name__ == "__main__":
    unittest.main()