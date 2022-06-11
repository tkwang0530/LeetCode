"""
2101. Detonate the Maximum Bombs
You are given a list of bombs. The range of a bomb is defined as the area where its effect can be felt. This area is in the shape of a circle with the center as the location of the bomb.

The bombs are represented by a 0-indexed 2D integer array bombs where bombs[i] = [xi, yi, ri]. xi and y1 denote the X-coordinate and Y-coordinate of the location of the i-th bomb, whereas ri denotes the radius of its range.

You may choose to detonate a single bomb. When a bomb is detonated, it will detonate all bombs that lie in its range. These bombs will further detonate the bombs that lie in their ranges.

Given the list of bombs, return the maximum number of bombs that can be detonated if you are allowed to detonate only one bomb.

Example1:
Input: bombs = [[2,1,3],[6,1,4]]
Output: 2
Explanation:
The above figure shows the positions and ranges of the 2 bombs.
If we detonate the left bomb, the right bomb will not be affected.
But if we detonate the right bomb, both bombs will be detonated.
So the maximum bombs that can be detonated is max(1, 2) = 2.

Example2:
Input: bombs = [[1,1,5],[10,10,5]]
Output: 1
Explanation:
Detonating either bomb will not detonate the other bomb, so the maximum number of bombs that can be detonated is 1.

Example3:
Input: bombs = [[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]
Output: 5
Explanation:
The best bomb to detonate is bomb 0 because:
- Bomb 0 detonates bombs 1 and 2. The red circle denotes the range of bomb 0.
- Bomb 2 detonates bomb 3. The blue circle denotes the range of bomb 2.
- Bomb 3 detonates bomb 4. The green circle denotes the range of bomb 3.
Thus all 5 bombs are detonated.

Constraints:
1 <= bombs.length <= 100
bombs[i].length == 3
1 <= xi, yi, ri <= 10^5
"""

"""
Note:
1. dfs + HashTable: O(n^3) time | O(n^2) space - where n is the number of bombs
"""

import collections
from typing import List
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        graph = collections.defaultdict(list)
        def isBomb(i, j):
            return (bombs[i][0]-bombs[j][0])**2 + (bombs[i][1]-bombs[j][1])**2 <= bombs[i][-1]**2
        
        for i in range(n):
            for j in range(i+1, n):
                if isBomb(i, j):
                    graph[i].append(j)
                if isBomb(j, i):
                    graph[j].append(i)
        
        def dfs(i, container, visited):
            for neighbor in graph[i]:
                if neighbor in visited:
                    continue
                visited.add(neighbor)
                container[0] += 1
                dfs(neighbor, container, visited)
            return container[0]
        
        maxBombs = 0
        for i in range(n):
            container = [1]
            visited = set([i])
            maxBombs = max(maxBombs, dfs(i, container, visited))
        return maxBombs

# Unit Tests
import unittest
funcs = [Solution().maximumDetonation]

class TestMaximumDetonation(unittest.TestCase):
    def testMaximumDetonation1(self):
        for func in funcs:
            bombs = [[2,1,3],[6,1,4]]
            self.assertEqual(func(bombs=bombs), 2)

    def testMaximumDetonation2(self):
        for func in funcs:
            bombs = [[1,1,5],[10,10,5]]
            self.assertEqual(func(bombs=bombs), 1)

    def testMaximumDetonation3(self):
        for func in funcs:
            bombs = [[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]
            self.assertEqual(func(bombs=bombs), 5)

if __name__ == "__main__":
    unittest.main()
