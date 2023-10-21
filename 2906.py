"""
2906. Construct Product Matrix
description: https://leetcode.com/problems/construct-product-matrix/description/
"""

"""
Note:
1. Math: O(mn) time | O(mn) space - where m is len(grid) and n is len(grid[0])
"""

from typing import List
class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])
        three = five = eightTwoThree = 0
        product = 1
        for row in range(rows):
            for col in range(cols):
                current = grid[row][col]
                while not current % 3:
                    current //= 3
                    three += 1
                
                while not current % 5:
                    current //= 5
                    five += 1

                while not current % 823:
                    current //= 823
                    eightTwoThree += 1
                
                product *= current
                product %= 12345
        

        output = [[1] * cols for _ in range(rows)]
        for row in range(rows):
            for col in range(cols):
                current = grid[row][col]
                nThree = three
                nFive = five
                nEightTwoThree = eightTwoThree
                while not current % 3:
                    current //= 3
                    nThree -= 1
                
                while not current % 5:
                    current //= 5
                    nFive -= 1

                while not current % 823:
                    current //= 823
                    nEightTwoThree -= 1

                output[row][col] = (pow(3, nThree, 12345) * pow(5, nFive, 12345) * pow(823, nEightTwoThree, 12345) * pow(current, -1, 12345) * product) % 12345
        return output

# Unit Tests
import unittest
funcs = [Solution().constructProductMatrix]

class TestConstructProductMatrix(unittest.TestCase):
    def testConstructProductMatrix1(self):
        for constructProductMatrix in funcs:
            grid = [[1,2],[3,4]]
            self.assertEqual(constructProductMatrix(grid=grid), [[24,12],[8,6]])

    def testConstructProductMatrix2(self):
        for constructProductMatrix in funcs:
            grid = [[12345],[2],[1]]
            self.assertEqual(constructProductMatrix(grid=grid), [[2],[0],[0]])

if __name__ == "__main__":
    unittest.main()