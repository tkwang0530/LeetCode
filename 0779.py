"""
779. K-th Symbol in Grammar
We build a table of n rows (1-indexed). We start by writing 0 in the 1st row. Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.
- For example, for n = 3, the 1st row is 0, the 2nd row is 01, and the 3rd row is 0110.

Given two integer n and k, return the k-th (1-indexed) symbol in the n-th row of a table of n rows.

Example1:
Input: n = 1, k = 1
Output: 0
Explanation: row 1: 0

Example2:
Input: n = 2, k = 1
Output: 0
Explanation: 
row 1: 0
row 2: 01

Example3:
Input: n = 2, k = 2
Output: 1
Explanation: 
row 1: 0
row 2: 01

Constraints:
1 <= n <= 30
1 <= k <= 2^n - 1
"""

"""
Note:
1. Recursion: O(n) time | O(n) space
"""




import unittest
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        # k is the idx (based-0)
        def dfs(n, k) -> int:
            if n == 1:
                return "0"
            parentBinary = dfs(n-1, k//2)
            if k % 2 > 0:
                return "0" if parentBinary == "1" else "1"
            else:
                return parentBinary
        return int(dfs(n, k-1))


# Unit Tests
funcs = [Solution().kthGrammar]


class TestKthGrammar(unittest.TestCase):
    def testKthGrammar1(self):
        for func in funcs:
            n = 1
            k = 1
            self.assertEqual(func(n=n, k=k), 0)

    def testKthGrammar2(self):
        for func in funcs:
            n = 2
            k = 1
            self.assertEqual(func(n=n, k=k), 0)

    def testKthGrammar3(self):
        for func in funcs:
            n = 2
            k = 2
            self.assertEqual(func(n=n, k=k), 1)


if __name__ == "__main__":
    unittest.main()
