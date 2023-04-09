"""
1654. Minimum Jumps to Reach Home
A certain bug's home is on the x-axis at position x. Help them get there from position 0.

The bug jumps according to the following rules:
- It can jump exactly a positions forward (to the right).
- It can jump exactly b positions backward (to the left).
- It cannot jump backward twice in a row.
- It cannot jump to any forbidden positions.

The bug may jump forward beyond its home, but it cannot jump to positions numbered with negative integers.

Given an array of integers forbidden, where forbidden[i] means that the bug cannot jump to the position forbidden[i], and integers a, b, and x, return the minimum number of jumps needed for the bug to reach its home. If there is no possible sequence of jumps that lands the bug on position x, return -1.

Example1:
Input: forbidden = [14,4,18,1,15], a = 3, b = 15, x = 9
Output: 3
Explanation: 3 jumps forward (0 -> 3 -> 6 -> 9) will get the bug home.

Example2:
Input: forbidden = [8,3,16,6,12,20], a = 15, b = 13, x = 11
Output: -1

Example3:
Input: forbidden = [1,6,2,14,5,17,4], a = 16, b = 9, x = 7
Output: 2
Explanation: One jump forward (0 -> 16) then one jump backward (16 -> 7) will get the bug home.

Constraints:
1 <= forbidden.length <= 1000
1 <= a, b, forbidden[i] <= 2000
0 <= x <= 2000
All the elements in forbidden are distinct.
Position x is not forbidden.
"""

"""
Note:
1. BFS (layer order traversal): O(n) time | O(n) space - where n is max(x, max(forbidden))+a+b
"""




import unittest
from typing import List
class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        maxVal = max(x, max(forbidden)) + a + b
        forbiddenSet = set(forbidden)
        visited = set()
        currentSet = set([(0, 0)])
        step = 0
        while currentSet:
            nextSet = set()
            for pos, backward in currentSet:
                if (pos, backward) in visited or pos in forbiddenSet:
                    continue
                visited.add((pos, backward))
                if pos == x:
                    return step

                if pos+a <= maxVal:
                    nextSet.add((pos+a, 0))
                if backward == 0 and pos-b > 0 and pos-b <= maxVal:
                    nextSet.add((pos-b, 1))
            step += 1
            currentSet = nextSet
        return -1


# Unit Tests
funcs = [Solution().minimumJumps]


class TestMinimumJumps(unittest.TestCase):
    def testMinimumJumps1(self):
        for func in funcs:
            forbidden = [14, 4, 18, 1, 15]
            a = 3
            b = 15
            x = 9
            self.assertEqual(
                func(forbidden=forbidden, a=a, b=b, x=x),
                3
            )

    def testMinimumJumps2(self):
        for func in funcs:
            forbidden = [8, 3, 16, 6, 12, 20]
            a = 15
            b = 13
            x = 11
            self.assertEqual(
                func(forbidden=forbidden, a=a, b=b, x=x),
                -1
            )

    def testMinimumJumps3(self):
        for func in funcs:
            forbidden = [1, 6, 2, 14, 5, 17, 4]
            a = 16
            b = 9
            x = 7
            self.assertEqual(
                func(forbidden=forbidden, a=a, b=b, x=x),
                2
            )

    def testMinimumJumps4(self):
        for func in funcs:
            forbidden = [162, 118, 178, 152, 167, 100, 40, 74, 199, 186, 26, 73, 200, 127, 30, 124, 193, 84, 184, 36, 103, 149, 153, 9, 54,
                         154, 133, 95, 45, 198, 79, 157, 64, 122, 59, 71, 48, 177, 82, 35, 14, 176, 16, 108, 111, 6, 168, 31, 134, 164, 136, 72, 98]
            a = 29
            b = 98
            x = 80
            self.assertEqual(
                func(forbidden=forbidden, a=a, b=b, x=x),
                121
            )


if __name__ == "__main__":
    unittest.main()
