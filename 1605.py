"""
1605. Find Valid Matrix Given Row and Column Sums
You are given two arrays rowSum and colSum of non-negative integers where rowSum[i] is the sum of the elements in the ith row and colSum[j] is the sum of the elements of the jth column of a 2D matrix. In other words, you do not know the elements of the matrix, but you do know the sums of each row and column.

Find any matrix of non-negative integers of size rowSum.length x colSum.length that satisfies the rowSum and colSum requirements.

Return a 2D array representing any matrix that fulfills the requirements. It's guaranteed that at least one matrix that fulfills the requirements exists.

Example1:
Input: rowSum = [3,8], colSum = [4,7]
Output: [[3,0],
         [1,7]]
Explanation: 
0th row: 3 + 0 = 3 == rowSum[0]
1st row: 1 + 7 = 8 == rowSum[1]
0th column: 3 + 1 = 4 == colSum[0]
1st column: 0 + 7 = 7 == colSum[1]
The row and column sums match, and all matrix elements are non-negative.
Another possible matrix is: [[1,2],
                             [3,5]]

Example2:
Input: rowSum = [5,7,10], colSum = [8,6,8]
Output: [[0,5,0],
         [6,1,0],
         [2,0,8]]

Constraints:
1 <= rowSum.length, column.length <= 500
0 <= rowSum[i], colSum[i] <= 10^8
sum(rowSum) == sum(colSum)
"""

"""
Note:
1. Greedy: O(nm + n+m) time | O(nm) space - where n is the length of rowSum and m is the length of colSum
"""




import unittest
from typing import List
class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        rows = len(rowSum)
        cols = len(colSum)
        output = [[0] * cols for _ in range(rows)]

        row = col = 0
        while row < rows and col < cols:
            if rowSum[row] > colSum[col]:
                output[row][col] = colSum[col]
                rowSum[row] -= colSum[col]
                colSum[col] -= colSum[col]
                col += 1
            else:
                output[row][col] = rowSum[row]
                colSum[col] -= rowSum[row]
                rowSum[row] -= rowSum[row]
                row += 1
        return output


# Unit Tests
funcs = [Solution().restoreMatrix]


class TestRestoreMatrix(unittest.TestCase):
    def testRestoreMatrix1(self):
        for func in funcs:
            rowSum = [3, 8]
            originalRowSum = rowSum[:]

            colSum = [4, 7]
            originalColSum = colSum[:]
            output = func(rowSum=rowSum, colSum=colSum)
            actualRowSum = [0] * len(rowSum)
            actualColSum = [0] * len(colSum)
            for row in range(len(rowSum)):
                for col in range(len(colSum)):
                    actualRowSum[row] += output[row][col]
                    actualColSum[col] += output[row][col]

            self.assertEqual(actualRowSum, originalRowSum)
            self.assertEqual(actualColSum, originalColSum)

    def testRestoreMatrix2(self):
        for func in funcs:
            rowSum = [5, 7, 10]
            originalRowSum = rowSum[:]

            colSum = [8, 6, 8]
            originalColSum = colSum[:]
            output = func(rowSum=rowSum, colSum=colSum)
            actualRowSum = [0] * len(rowSum)
            actualColSum = [0] * len(colSum)
            for row in range(len(rowSum)):
                for col in range(len(colSum)):
                    actualRowSum[row] += output[row][col]
                    actualColSum[col] += output[row][col]

            self.assertEqual(actualRowSum, originalRowSum)
            self.assertEqual(actualColSum, originalColSum)


if __name__ == "__main__":
    unittest.main()
