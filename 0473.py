"""
473. Matchsticks to Square
You are given an integer array matchsticks where matchsticks[i] is the length of the i-th matchstick. You want to use all the matchsticks to make one square. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.

Return true if you can make this square and false otherwise.

Example1:
Input: matchsticks = [1,1,2,2,2]
Output: true
Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.

Example2:
Input: matchsticks = [3,3,3,3,4]
Output: false
Explanation: You cannot find a way to form a square with all the matchsticks.

Constraints:
1 <= matchsticks.length <= 15
1 <= matchsticks[i] <= 10^8
"""

"""
Note:
1. DFS + Sort: O(4 ** n) time | O(n) space - where n is the length of array matchsticks
"""




import unittest
from typing import List
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total % 4 != 0:
            return False

        sideSum = total // 4
        n = len(matchsticks)
        matchsticks.sort(key=lambda x: -x)

        def dfs(i, currentSums) -> bool:
            if i >= n:
                return True
            for group in range(4):
                if currentSums[group] + matchsticks[i] > sideSum:
                    continue
                currentSums[group] += matchsticks[i]
                if dfs(i+1, currentSums):
                    return True
                currentSums[group] -= matchsticks[i]
                if currentSums[group] == 0:
                    break
            return False

        currentSums = [0] * 4
        return dfs(0, currentSums)


# Unit Tests
funcs = [Solution().makesquare]


class TestMakesquare(unittest.TestCase):
    def testMakesquare1(self):
        for func in funcs:
            matchsticks = [1, 1, 2, 2, 2]
            self.assertEqual(func(matchsticks=matchsticks), True)

    def testMakesquare2(self):
        for func in funcs:
            matchsticks = [3, 3, 3, 3, 4]
            self.assertEqual(func(matchsticks=matchsticks), False)


if __name__ == "__main__":
    unittest.main()
