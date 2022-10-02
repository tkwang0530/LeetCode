"""
733. Flood Fill
An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.

Return the modified image after performing the flood fill.

Example1:
Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.

Example2:
Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
Output: [[0,0,0],[0,0,0]]
Explanation: The starting pixel is already colored 0, so no changes are made to the image.

Constraints:
m == image.length
n == image[i].length
1 <= m, n <= 50
0 <= image[i][j], color < 2^16
0 <= sr < m
0 <= sc < n
"""

"""
Note:
1. DFS: O(mn) time | O(mn) space - where m is len(image), and n is len(image[i])
"""




import unittest
from typing import List
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        startPointColor = image[sr][sc]
        if startPointColor == color:
            return image

        rows = len(image)
        cols = len(image[0])

        def dfs(row, col):
            if row in (-1, rows) or col in (-1, cols) or image[row][col] != startPointColor:
                return
            image[row][col] = color
            for r, c in [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]:
                dfs(r, c)
        dfs(sr, sc)
        return image


# Unit Tests
funcs = [Solution().floodFill]


class TestFloodFill(unittest.TestCase):
    def testFloodFill1(self):
        for func in funcs:
            image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
            sr = 1
            sc = 1
            color = 2
            self.assertEqual(func(image=image, sr=sr, sc=sc, color=color), [
                             [2, 2, 2], [2, 2, 0], [2, 0, 1]])

    def testFloodFill2(self):
        for func in funcs:
            image = [[0, 0, 0], [0, 0, 0]]
            sr = 0
            sc = 0
            color = 0
            self.assertEqual(func(image=image, sr=sr, sc=sc, color=color), [
                             [0, 0, 0], [0, 0, 0]])


if __name__ == "__main__":
    unittest.main()
