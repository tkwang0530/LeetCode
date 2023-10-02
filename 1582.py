"""
1582. Special Positions in a Binary Matrix
description: https://leetcode.com/problems/special-positions-in-a-binary-matrix/description/
"""

"""
Note:
1. Counter: O(mn) time | O(m+n) space - where m is len(mat) and n is len(mat[0])
"""


from typing import List
import collections, unittest
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        colOnes = collections.defaultdict(int)
        rowOnes = collections.defaultdict(int)
        rows = len(mat)
        cols = len(mat[0])
        for row in range(rows):
            for col in range(cols):
                if mat[row][col] == 1:
                    colOnes[col] += 1
                    rowOnes[row] += 1
        
        specials = 0
        for row in range(rows):
            for col in range(cols):
                specials += mat[row][col] == 1 and colOnes[col] == 1 and rowOnes[row] == 1
        
        return specials

# Unit Tests
funcs = [Solution().numSpecial]
class TestNumSpecial(unittest.TestCase):
    def testNumSpecial1(self):
        for numSpecial in funcs:
            mat = [[1,0,0],[0,0,1],[1,0,0]]
            self.assertEqual(numSpecial(mat=mat), 1)

    def testNumSpecial2(self):
        for numSpecial in funcs:
            mat = [[1,0,0],[0,1,0],[0,0,1]]
            self.assertEqual(numSpecial(mat=mat), 3)

if __name__ == "__main__":
    unittest.main()
