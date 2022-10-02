"""
661. Image Smoother
An image smoother is a filter of the size 3 x 3 that can be applied to each cell of an image by rounding down the average of the cell and the eight surrounding cells (i.e., the average of the nine cells in the blue smoother). If one or more of the surrounding cells of a cell is not present, we do not consider it in the average (i.e., the average of the four cells in the red smoother).

Given an m x n integer matrix img representing the grayscale of an image, return the image after applying the smoother on each cell of it.

Example1:
Input: img = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[0,0,0],[0,0,0],[0,0,0]]
Explanation:
For the points (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
For the points (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
For the point (1,1): floor(8/9) = floor(0.88888889) = 0

Example2:
Input: img = [[100,200,100],[200,50,200],[100,200,100]]
Output: [[137,141,137],[141,138,141],[137,141,137]]
Explanation:
For the points (0,0), (0,2), (2,0), (2,2): floor((100+200+200+50)/4) = floor(137.5) = 137
For the points (0,1), (1,0), (1,2), (2,1): floor((200+200+50+200+100+100)/6) = floor(141.666667) = 141
For the point (1,1): floor((50+200+200+200+200+100+100+100+100)/9) = floor(138.888889) = 138

Constraints:
m == img.length
n == img[i].length
1 <= m, n <= 200
0 <= img[i][j] <= 255
"""

"""
Note:
1. Brute-Force: O(mn) time | O(mn) space - where m, n is the dimension of img
"""




import unittest
from typing import List
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        rows = len(img)
        cols = len(img[0])
        updatedImage = [[0] * cols for _ in range(rows)]

        def getSmootherVal(row, col):
            count = 0
            total = 0
            for r, c in [(row-1, col-1), (row-1, col), (row-1, col+1), (row, col+1), (row+1, col+1), (row+1, col), (row+1, col-1), (row, col-1), (row, col)]:
                if r in (-1, rows) or c in (-1, cols):
                    continue
                count += 1
                total += img[r][c]
            return int(total/count)

        for row in range(rows):
            for col in range(cols):
                updatedImage[row][col] = getSmootherVal(row, col)
        return updatedImage


# Unit Tests
funcs = [Solution().imageSmoother]


class TestImageSmoother(unittest.TestCase):
    def testImageSmoother1(self):
        for func in funcs:
            img = [[100, 200, 100], [200, 50, 200], [100, 200, 100]]
            self.assertEqual(
                func(img=img), [[137, 141, 137], [141, 138, 141], [137, 141, 137]])

    def testImageSmoother2(self):
        for func in funcs:
            img = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
            self.assertEqual(
                func(img=img), [[0, 0, 0], [0, 0, 0], [0, 0, 0]])


if __name__ == "__main__":
    unittest.main()
