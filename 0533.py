"""
533. Lonely Pixel II
Given an m x n picture consisting of black 'B' and white 'W' pixels and an integer target, return the number of black lonely pixels.

A black lonely pixel is a character 'B' that located at a specific position (r, c) where:
- Row r and column c both contain exactly target black pixels.
- For all rows that have a black pixel at column c, they should be exactly the same as row r.

Example1:
Input: picture = [["W","B","W","B","B","W"],["W","B","W","B","B","W"],["W","B","W","B","B","W"],["W","W","B","W","B","W"]], target = 3
Output: 6
Explanation: All the green 'B' are the black pixels we need (all 'B's at column 1 and 3).
Take 'B' at row r = 0 and column c = 1 as an example:
 - Rule 1, row r = 0 and column c = 1 both have exactly target = 3 black pixels. 
 - Rule 2, the rows have black pixel at column c = 1 are row 0, row 1 and row 2. They are exactly the same as row r = 0.

Example2:
Input: picture = [["W","W","B"],["W","W","B"],["W","W","B"]], target = 1
Output: 0

Constraints:
m == picture.length
n == picture.length
1 <= m, n <= 200
picture[i][j] is 'W' or 'B'.
1 <= target <= min(m, n)
"""

"""
Note:
1. HashTable: O(mn) time | O(m+n) space
"""

from typing import List
class Solution:
    def findBlackPixel(self, picture: List[List[str]], target: int) -> int:
        rows = len(picture)
        cols = len(picture[0])
        rowBCounts = [0] * rows
        colBCounts = [0] * cols
        
        for row in range(rows):
            for col in range(cols):
                if picture[row][col] == "B":
                    rowBCounts[row] += 1
                    colBCounts[col] += 1
        
        
        for row in range(rows):
            for col in range(cols):
                if picture[row][col] == "B" and rowBCounts[row] == colBCounts[col] == target:
                    picture[row][col] = "X"
        
        rowString = {}
        for row in range(rows):
            rowString[row] = "".join(picture[row])
        
        count = 0
        for col in range(cols):
            keySet = set()
            temp = 0
            for row in range(rows):
                if picture[row][col] == 'X':
                    keySet.add(rowString[row])
                    temp += 1
                elif picture[row][col] == 'B':
                    temp = 0
                    break
            if len(keySet) == 1:
                count += temp
        return count

# Unit Tests
import unittest
funcs = [Solution().findBlackPixel]
class TestFindBlackPixel(unittest.TestCase):
    def testFindBlackPixel1(self):
        for func in funcs:
            picture = [["W","B","W","B","B","W"],["W","B","W","B","B","W"],["W","B","W","B","B","W"],["W","W","B","W","B","W"]]
            target = 3
            self.assertEqual(func(picture=picture, target=target), 6)

    def testFindBlackPixel2(self):
        for func in funcs:
            picture = [["W","W","B"],["W","W","B"],["W","W","B"]]
            target = 1
            self.assertEqual(func(picture=picture, target=target), 0)


if __name__ == "__main__":
    unittest.main()
