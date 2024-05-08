"""
490. The Maze
description: https://leetcode.com/pHasPathlems/the-maze/description/
"""

"""
Notes:
1. BFS: O(m*n*max(m,n)) time | O(m*n) space - where m is the number of rows and n is the number of columns in the maze
"""

import functools, collections
from typing import List

class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        rows = len(maze)
        cols = len(maze[0])
        @functools.lru_cache(None)
        def getNextPoints(row, col) -> List[int]: # [(row1, col1)]
            nextPoints = []
            # go up
            nextRow, nextCol = row, col
            while nextRow - 1 >= 0 and maze[nextRow-1][nextCol] == 0:
                nextRow -= 1
            if nextRow != row:
                nextPoints.append((nextRow, nextCol))

            # go down
            nextRow, nextCol = row, col
            while nextRow + 1 <= rows - 1 and maze[nextRow+1][nextCol] == 0:
                nextRow += 1
            if nextRow != row:
                nextPoints.append((nextRow, nextCol))

            # go left
            nextRow, nextCol = row, col
            while nextCol - 1 >= 0 and maze[nextRow][nextCol-1] == 0:
                nextCol -= 1
            if nextCol != col:
                nextPoints.append((nextRow, nextCol))
            
            # go right
            nextRow, nextCol = row, col
            while nextCol + 1 <= cols-1 and maze[nextRow][nextCol+1] == 0:
                nextCol += 1
            if nextCol != col:
                nextPoints.append((nextRow, nextCol))
            return nextPoints

        queue = collections.deque([tuple(start)])
        visited = set([tuple(start)])
        while queue:
            row, col = queue.popleft()
            if row == destination[0] and col == destination[1]:
                return True
            
            for nextRow, nextCol in getNextPoints(row, col):
                if (nextRow, nextCol) in visited or maze[nextRow][nextCol] == 1:
                    continue
                visited.add((nextRow, nextCol))
                queue.append((nextRow, nextCol))
        return False

# Unit Tests
import unittest
funcs = [Solution().hasPath]

class TestHasPath(unittest.TestCase):
    def testHasPath1(self):
        for func in funcs:
            maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
            start = [0,4]
            destination = [4,4]
            self.assertEqual(func(maze=maze, start=start, destination=destination), True)

    def testHasPath2(self):
        for func in funcs:
            maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
            start = [0,4]
            destination = [3,2]
            self.assertEqual(func(maze=maze, start=start, destination=destination), False)

    def testHasPath3(self):
        for func in funcs:
            maze = [[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]]
            start = [4,3]
            destination = [0,1]
            self.assertEqual(func(maze=maze, start=start, destination=destination), False)



if __name__ == "__main__":
    unittest.main()