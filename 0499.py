"""
499. The Maze III
description: https://leetcode.com/problems/the-maze-iii/description/
"""

"""
Notes:
1. dijkstra algorithm: O(m*n*log(mn)) time | O(m*n) space - where m is the number of rows and n is the number of columns in the maze
"""

import functools, heapq
from typing import List

class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        rows = len(maze)
        cols = len(maze[0])
        @functools.lru_cache(None)
        def getNextPoints(row, col) -> List[int]: # [(cost, instruction, row1, col1)]
            nextPoints = []
            # go down
            nextRow, nextCol = row, col
            while nextRow + 1 <= rows - 1 and maze[nextRow+1][nextCol] == 0:
                nextRow += 1
                if nextRow == hole[0] and nextCol == hole[1]:
                    break
            if nextRow != row:
                nextPoints.append((abs(nextRow-row), "d", nextRow, nextCol))

            # go left
            nextRow, nextCol = row, col
            while nextCol - 1 >= 0 and maze[nextRow][nextCol-1] == 0:
                nextCol -= 1
                if nextRow == hole[0] and nextCol == hole[1]:
                    break
            if nextCol != col:
                nextPoints.append((abs(nextCol-col), "l", nextRow, nextCol))

                        
            # go right
            nextRow, nextCol = row, col
            while nextCol + 1 <= cols-1 and maze[nextRow][nextCol+1] == 0:
                nextCol += 1
                if nextRow == hole[0] and nextCol == hole[1]:
                    break
            if nextCol != col:
                nextPoints.append((abs(nextCol-col), "r", nextRow, nextCol))

            # go up
            nextRow, nextCol = row, col
            while nextRow - 1 >= 0 and maze[nextRow-1][nextCol] == 0:
                nextRow -= 1
                if nextRow == hole[0] and nextCol == hole[1]:
                    break
            if nextRow != row:
                nextPoints.append((abs(nextRow-row), "u", nextRow, nextCol))

            return nextPoints

        minHeap = [tuple([0, "", ball[0], ball[1]])]
        minDist = {tuple(ball): 0}
        while minHeap:
            dist, instructions, row, col = heapq.heappop(minHeap)
            if row == hole[0] and col == hole[1]:
                return instructions
            
            for cost, direc, nextRow, nextCol in getNextPoints(row, col):
                if maze[nextRow][nextCol] == 1:
                    continue
                if (nextRow, nextCol) in minDist and cost+dist > minDist[(nextRow, nextCol)]:
                    continue
                minDist[(nextRow, nextCol)] = cost+dist
                heapq.heappush(minHeap, (cost+dist, instructions+direc, nextRow, nextCol))
        return "impossible"

# Unit Tests
import unittest
funcs = [Solution().findShortestWay]

class TestFindShortestWay(unittest.TestCase):
    def testFindShortestWay1(self):
        for func in funcs:
            maze = [[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]]
            ball = [4,3]
            hole = [0,1]
            self.assertEqual(func(maze=maze, ball=ball, hole=hole), "lul")

    def testFindShortestWay2(self):
        for func in funcs:
            maze = [[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]]
            ball = [4,3]
            hole = [3,0]
            self.assertEqual(func(maze=maze, ball=ball, hole=hole), "impossible")

    def testFindShortestWay3(self):
        for func in funcs:
            maze = [[0,0,0,0,0,0,0],[0,0,1,0,0,1,0],[0,0,0,0,1,0,0],[0,0,0,0,0,0,1]]
            ball = [0,4]
            hole = [3,5]
            self.assertEqual(func(maze=maze, ball=ball, hole=hole), "dldr")

if __name__ == "__main__":
    unittest.main()