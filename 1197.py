"""
1197. Minimum Knight Moves
In an infinite chess board with coordinates from -infinity to +infinity,
you have a knight at square [0, 0].

A knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.

Example1:
Input: x = 2, y = 1
Output: 1
Explanation: [0, 0] → [2, 1]

Example2:
Input: x = 5, y = 5
Output: 4
Explanation: [0, 0] → [2, 1] → [4, 2] → [3, 4] → [5, 5]

Constraints:
-300 <= x, y <= 300
0 <= |x| + |y| <= 300
"""

""" 
1. BFS + HashSet: O(8 ** minSteps) time | O(8 ** minSteps) space
"""

import collections
class Solution:
    def minKnightMoves(self, i: int, j: int) -> int:
        visitedPoint = set()
        
        def getNextPoints(x: int, y: int):
            return [(x+1, y+2), (x+2, y+1), 
                    (x+2, y-1), (x+1, y-2), 
                    (x-1, y-2), (x-2, y-1), 
                    (x-2, y+1), (x-1, y+2)]
        
        
        def bfs(x, y):
            queue = collections.deque([(x, y, 0)])
            visitedPoint.add((x, y))
            while queue:
                x, y, step = queue.popleft()
                if x == i and y == j:
                    return step
                for nextPoint in getNextPoints(x, y):
                    if nextPoint in visitedPoint:
                        continue
                    queue.append((nextPoint[0], nextPoint[1], step+1))
                    visitedPoint.add((nextPoint[0], nextPoint[1]))
        
        return bfs(0, 0)


# Unit Tests
import unittest
funcs = [Solution().minKnightMoves]

class TestMinKnightMoves(unittest.TestCase):
    def testMinKnightMoves1(self):
        for func in funcs:
            self.assertEqual(func(i=2, j=1), 1)

    def testMinKnightMoves2(self):
        for func in funcs:
            self.assertEqual(func(i=5, j=5), 4)

if __name__ == "__main__":
    unittest.main()
