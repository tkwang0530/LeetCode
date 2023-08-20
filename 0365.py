"""
365. Water and Jug Problem
description: https://leetcode.com/problems/water-and-jug-problem/description/
"""

"""
Note:
1. BFS + HashTable: O(x+y) time | O(x+y) space - where x is jug1Capacity and y is jug2Capacity
"""

import collections
class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        small = jug1Capacity
        big = jug2Capacity
        if small > big:
            small, big = big, small

        if targetCapacity > small + big:
            return False

        queue = collections.deque([(0, 0)])
        visited = set((0, 0))
        while len(queue) > 0:
            a, b = queue.popleft()
            if a + b == targetCapacity or targetCapacity in (a, b):
                return True

            for nextA, nextB in [
                (small, b), # fill jar small
                (a, big), # fill jar big
                (0, b), # empty jar small
                (a, 0), # empty jar big
                (min(small, b+a), max(0, b - (small-a))),
                (max(0, a - (big-b)), min(big, b+a))
            ]:
                if (nextA, nextB) in visited:
                    continue
                queue.append((nextA, nextB))
                visited.add((nextA, nextB))
        return False

# Unit Tests
import unittest
funcs = [Solution().canMeasureWater]
class TestCanMeasureWater(unittest.TestCase):
    def testCanMeasureWater1(self):
        for canMeasureWater in funcs:
            jug1Capacity = 3
            jug2Capacity = 5
            targetCapacity = 4
            self.assertEqual(canMeasureWater(jug1Capacity=jug1Capacity, jug2Capacity=jug2Capacity, targetCapacity=targetCapacity), True)

    def testCanMeasureWater2(self):
        for canMeasureWater in funcs:
            jug1Capacity = 2
            jug2Capacity = 6
            targetCapacity = 5
            self.assertEqual(canMeasureWater(jug1Capacity=jug1Capacity, jug2Capacity=jug2Capacity, targetCapacity=targetCapacity), False)

    def testCanMeasureWater3(self):
        for canMeasureWater in funcs:
            jug1Capacity = 1
            jug2Capacity = 2
            targetCapacity = 3
            self.assertEqual(canMeasureWater(jug1Capacity=jug1Capacity, jug2Capacity=jug2Capacity, targetCapacity=targetCapacity), True)

if __name__ == "__main__":
    unittest.main()
