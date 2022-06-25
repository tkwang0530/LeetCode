"""
754. Reach a Number
You are standing at position 0 on an infinite number line. There is a destination at position target.
You can make some number of moves numMoves so that:
- On each move, you can either go left or right.
- During the i-th move (starting from i == 1 to i == numMoves), you take i steps in the chosen direction.

Given the integer target, return the minimum number of moves required (i.e. the minimum numMoves) to reach the destination.

Example1:
Input: target = 2
Output: 3
Explanation:
On the 1st move, we step from 0 to 1 (1 step).
On the 2nd move, we step from 1 to -1 (2 steps).
On the 3rd move, we step from -1 to 2 (3 steps).

Example2:
Input: target = 3
Output: 2
Explanation:
On the 1st move, we step from 0 to 1 (1 step).
On the 2nd move, we step from 1 to 3 (2 steps).

Constraints:
-10^9 <= target <= 10^9
target != 0
"""

"""
Note:
1. Math: O(1) time | O(1) space
"""
import math
class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        def solve(target):
            return math.ceil((-1 + (1+8*target)**0.5) / 2)
        
        n = solve(target)
        _sum = n * (n+1) // 2
        if (_sum - target) % 2 == 0:
            return n
        if (n + 1) % 2 == 0:
            return n + 2
        else:
            return n + 1

# Unit Tests
import unittest
funcs = [Solution().reachNumber]
class TestReachNumber(unittest.TestCase):
    def testReachNumber1(self):
        for func in funcs:
            target = 2
            self.assertEqual(func(target=target), 3)

    def testReachNumber2(self):
        for func in funcs:
            target = 3
            self.assertEqual(func(target=target), 2)

if __name__ == "__main__":
    unittest.main()
