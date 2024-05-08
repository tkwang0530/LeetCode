"""
505. The Maze II
description: https://leetcode.com/problems/the-maze-ii/description/
"""

"""
Notes:
1. dijkstra algorithm: O(m*n*log(mn)) time | O(m*n) space - where m is the number of rows and n is the number of columns in the maze
"""

import functools, heapq
from typing import List

class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        rows = len(maze)
        cols = len(maze[0])
        @functools.lru_cache(None)
        def getNextPoints(row, col) -> List[int]: # [(cost, row1, col1)]
            nextPoints = []
            # go up
            nextRow, nextCol = row, col
            while nextRow - 1 >= 0 and maze[nextRow-1][nextCol] == 0:
                nextRow -= 1
            if nextRow != row:
                nextPoints.append((abs(nextRow-row),nextRow, nextCol))

            # go down
            nextRow, nextCol = row, col
            while nextRow + 1 <= rows - 1 and maze[nextRow+1][nextCol] == 0:
                nextRow += 1
            if nextRow != row:
                nextPoints.append((abs(nextRow-row),nextRow, nextCol))

            # go left
            nextRow, nextCol = row, col
            while nextCol - 1 >= 0 and maze[nextRow][nextCol-1] == 0:
                nextCol -= 1
            if nextCol != col:
                nextPoints.append((abs(nextCol-col),nextRow, nextCol))
            
            # go right
            nextRow, nextCol = row, col
            while nextCol + 1 <= cols-1 and maze[nextRow][nextCol+1] == 0:
                nextCol += 1
            if nextCol != col:
                nextPoints.append((abs(nextCol-col), nextRow, nextCol))
            return nextPoints

        minHeap = [tuple([0, start[0], start[1]])]
        minDist = {tuple(start): 0}
        while minHeap:
            dist, row, col = heapq.heappop(minHeap)
            if row == destination[0] and col == destination[1]:
                return dist
            
            for cost, nextRow, nextCol in getNextPoints(row, col):
                if maze[nextRow][nextCol] == 1:
                    continue
                if (nextRow, nextCol) in minDist and cost+dist >= minDist[(nextRow, nextCol)]:
                    continue
                minDist[(nextRow, nextCol)] = cost+dist
                heapq.heappush(minHeap, (cost+dist, nextRow, nextCol))
        return -1


# Unit Tests
import unittest
funcs = [Solution().shortestDistance]

class TestShortestDistance(unittest.TestCase):
    def testShortestDistance1(self):
        for func in funcs:
            maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
            start = [0,4]
            destination = [4,4]
            self.assertEqual(func(maze=maze, start=start, destination=destination), 12)

    def testShortestDistance2(self):
        for func in funcs:
            maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
            start = [0,4]
            destination = [3,2]
            self.assertEqual(func(maze=maze, start=start, destination=destination), -1)

    def testShortestDistance3(self):
        for func in funcs:
            maze = [[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]]
            start = [4,3]
            destination = [0,1]
            self.assertEqual(func(maze=maze, start=start, destination=destination), -1)



if __name__ == "__main__":
    unittest.main()