"""
997. Find the Town Judge
description: https://leetcode.com/problems/find-the-town-judge/description/
"""

"""
Note:
1. HashMap: O(n+m) time | O(n) space - where n is the number of people and m is the number of trust relationships
"""

import collections
from typing import List
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trustBy = collections.defaultdict(int)
        trusting = collections.defaultdict(int)
        for a, b in trust:
            trustBy[b] += 1
            trusting[a] += 1

        judgeCount = 0
        judgeLabel = -1
        for people in range(1, n+1):
            if trustBy[people] == n-1 and trusting[people] == 0:
                judgeCount += 1
                judgeLabel = people
        return judgeLabel if judgeCount == 1 else -1

# Unit Tests
import unittest
funcs = [Solution().findJudge]

class TestFindJudge(unittest.TestCase):
    def testFindJudge1(self):
        for findJudge in funcs:
            n = 2
            trust = [[1,2]]
            self.assertEqual(findJudge(n=n, trust=trust), 2)

    def testFindJudge2(self):
        for findJudge in funcs:
            n = 3
            trust = [[1,3],[2,3]]
            self.assertEqual(findJudge(n=n, trust=trust), 3)

    def testFindJudge3(self):
        for findJudge in funcs:
            n = 3
            trust = [[1,3],[2,3],[3,1]]
            self.assertEqual(findJudge(n=n, trust=trust), -1)

if __name__ == "__main__":
    unittest.main()