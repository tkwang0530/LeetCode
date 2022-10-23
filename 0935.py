"""
935. Knight Dialer
The chess knight has a unique movement, it may move two squares vertically and one square horizontally, or two squares horizontally and one square vertically (with both forming the shape of an L). The possible movements of chess knight are shown in this diagram:

We have a chess knight and a phone pad as shown below, the knight can only stand on a numeric cell (i.e. blue cell).
123
456
789
*0#

Given an integer n, return how many distinct phone numbers of length n we can dial.

You are allowed to place the knight on any numeric cell Initially and then you should perform n-1 jumps to dial a number of length n. All jumps should be valid knight jumps.

As the answer may be very large, return the answer modulo 10^9 + 7.

Example1:
Input: n = 1
Output: 10
Explanation: We need to dial a number of length 1, so placing the knight over any numeric cell of the 10 cells is sufficient.

Example2:
Input: n = 2
Output: 20
Explanation: All the valid number we can dial are [04, 06, 16, 18, 27, 29, 34, 38, 40, 43, 49, 60, 61, 67, 72, 76, 81, 83, 92, 94]

Example3:
Input: n = 3131
Output: 136006598
Explanation: Please take care of the mod.

Constraints:
1 <= n <= 5000
"""

"""
Note:
1. dfs+memo: O(10*n) time | O(10*n) space
"""




import unittest
class Solution:
    def knightDialer(self, n: int) -> int:
        if n == 1:
            return 10
        mod = 10**9 + 7

        numNextNum = {
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [3, 9, 0],
            6: [1, 7, 0],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4],
            0: [4, 6]
        }

        memo = {}

        def dfs(num, left):
            if num in (4, 6) and left == 1:
                return 3
            elif left == 1:
                return 2

            if (num, left) in memo:
                return memo[(num, left)]
            total = 0
            for nextNum in numNextNum[num]:
                total += dfs(nextNum, left-1)

            memo[(num, left)] = total
            return memo[(num, left)]

        total = 0
        for num in range(10):
            if num == 5:
                continue
            total += dfs(num, n-1)
        return total % mod


# Unit Tests
funcs = [Solution().knightDialer]


class TestKnightDialer(unittest.TestCase):
    def testKnightDialer1(self):
        for func in funcs:
            n = 1
            self.assertEqual(func(n=n), 10)

    def testKnightDialer2(self):
        for func in funcs:
            n = 2
            self.assertEqual(func(n=n), 20)


if __name__ == "__main__":
    unittest.main()
