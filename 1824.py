"""
1824. Minimum Sideway Jumps
There is a 3 lane road of length n that consists of n + 1 points labeled from 0 to n. A frog starts at point 0 in the second lane and wants to jump to point n. However, there could be obstacles along the way.

You are given an array obstacles of length n + 1 where each obstacles[i] (ranging from 0 to 3) describes an obstacle on the lane obstacles[i] at point i. If obstacles[i] == 0, there are no obstacles at point i. There will be at most one obstacle in the 3 lanes at each point.

- For example, if obstacles[2] == 1, then there is an obstacle on lane 1 at point 2.

The frog can only travel from point i to point i + 1 on the same lane if there is not an obstacle on the lane at point i + 1. To avoid obstacles, the frog can also perform a side jump to jump to another lane (even if they are not adjacent) at the same point if there is no obstacle on the new lane.

- For example, the frog can jump from lane 3 at point 3 to lane 1 at point 3.

Return the minimum number of side jumps the frog needs to reach any lane at point n starting from lane 2 at point 0.

Note: There will be no obstacles on points 0 and n.

Example1:
Input: obstacles = [0,1,2,3,0]
Output: 2 
Explanation: The optimal solution is shown by the arrows above. There are 2 side jumps (red arrows).
Note that the frog can jump over obstacles only when making side jumps (as shown at point 2).

Example2:
Input: obstacles = [0,1,1,3,3,0]
Output: 0
Explanation: There are no obstacles on lane 2. No side jumps are required.

Example3:
Input: obstacles = [0,2,1,0,3,0]
Output: 2
Explanation: The optimal solution is shown by the arrows above. There are 2 side jumps.

Constraints:
obstacles.length == n + 1
1 <= n <= 5 * 10^5
0 <= obstacles[i] <= 3
obstacles[0] == obstacles[n] == 0
"""

"""
Note:
1. dp: O(n) time | O(1) space - where n is the length of array obstacles
dp[0] = minimum jump to reach lane 1
dp[1] = minimum jump to reach lane 2
dp[2] = minimum jump to reach lane 3
if meet a stone, set its dp[i] to infinity
result equals to min(dp)

2. BFS+HashTable: O(n) time | O(n) space - where n is the length of array obstacles
"""




import collections
import unittest
from typing import List
class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        dp = [1, 0, 1]
        for obstacle in obstacles:
            if obstacle:
                dp[obstacle - 1] = float('inf')
            for i in range(3):
                if obstacle != i + 1:
                    dp[i] = min(dp[i], dp[(i + 1) % 3] +
                                1, dp[(i + 2) % 3] + 1)
        return min(dp)

    def minSideJumps2(self, obstacles: List[int]) -> int:
        n = len(obstacles)

        queue = collections.deque([(1, 0, 0)])  # (lane, position, step)
        cache = set([(1, 0)])

        while queue:
            lane, position, step = queue.popleft()
            if position == n - 1:
                return step

            for nextLane, nextPosition, cost in [(lane, position+1, 0), ((lane+1) % 3, position, 1), ((lane+2) % 3, position, 1)]:
                if obstacles[nextPosition] == nextLane+1:
                    continue
                if (nextLane, nextPosition) in cache:
                    continue

                queue.append((nextLane, nextPosition, step+cost))
                cache.add((nextLane, nextPosition))
        return -1


# Unit Tests
funcs = [Solution().minSideJumps, Solution().minSideJumps2]


class TestMinSideJumps(unittest.TestCase):
    def testMinSideJumps1(self):
        for func in funcs:
            obstacles = [0, 1, 2, 3, 0]
            self.assertEqual(func(obstacles=obstacles), 2)

    def testMinSideJumps2(self):
        for func in funcs:
            obstacles = [0, 1, 1, 3, 3, 0]
            self.assertEqual(func(obstacles=obstacles), 0)

    def testMinSideJumps3(self):
        for func in funcs:
            obstacles = [0, 2, 1, 0, 3, 0]
            self.assertEqual(func(obstacles=obstacles), 2)


if __name__ == "__main__":
    unittest.main()
