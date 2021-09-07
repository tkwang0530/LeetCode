"""
60. Permutation Sequence
The set [1, 2, 3, ..., n] contains a total of n! unique permutations.
By listing the labeling all of the permutations in order, we get the following sequence for n = 3:
1. "123"
2. "132"
3. "213"
4. "231"
5. "312"
6. "321"

Given n and k, return kth permutation sequence.

Example1:
Input: n = 3, k = 3
Output: "213"

Example2:
Input: n = 4, k = 9
Output: "2314"

Example3:
Input: n = 3, k = 1
Output: "123"

Constraints:
1 <= n <= 9
1 <= k <= n!
"""

"""
Note:
1. Find Quotient and Remainder: O(n^2) time | O(n) space
e.g.
n = 3, k = 3, session list [1, 2, 3]
each session has 2! numbers
3 / 2! = 1...1 => first number = 2
k = 1 list [1, 3]
1 / 1! = 1...0 => corner case => convert to (0 ... 1!) => second number = 1
k = 1 list [3] => third number = 3
"""

import unittest
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        fac = 1
        candidates = []
        for i in range(1, n+1): # O(n)
            fac *= i
            candidates.append(i)

        chars = []
        while len(candidates) > 0: # O(n^2) 
            fac = fac // len(candidates)
            remainder = k % fac 
            session = k // fac if remainder != 0 else k // fac - 1 
            chars.append(candidates[session])

            candidates.pop(session) # O(n)
            k = remainder
        return "".join(str(x) for x in chars) # O(n)


# Unit Tests
funcs = [Solution().getPermutation]


class TestGetPermutation(unittest.TestCase):
    def testGetPermutation1(self):
        for func in funcs:
            self.assertEqual(func(n=3,k=3), "213")

    def testGetPermutation2(self):
        for func in funcs:
            self.assertEqual(func(n=4,k=9), "2314")

    def testGetPermutation3(self):
        for func in funcs:
            self.assertEqual(func(n=3,k=1), "123")

if __name__ == "__main__":
    unittest.main()
