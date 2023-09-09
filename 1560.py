"""
1560. Most Visited Sector in a Circular Track
description: https://leetcode.com/problems/most-visited-sector-in-a-circular-track/description/
"""

"""
Note:
1. Simulation: O(nm) time | O(n) space
2. Greedy
                          s------n
1----------------------n
1 ---------------------n
1 ----- e
Only need to care the start point and end point.
If start <= end, return the range [start, end]
if end < start, return the range [1, end] + range [start, n]
"""

from typing import List
class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        roundsIndex = 0
        i = rounds[0]-1
        counter = [0] * n
        maxCount = 0
        while roundsIndex < len(rounds):
            counter[i % n] += 1
            maxCount = max(maxCount, counter[i % n])
            if i % n == rounds[roundsIndex] - 1:
                roundsIndex += 1
            i += 1
        
        output = []
        for i in range(n):
            if counter[i] == maxCount:
                output.append(i+1)
        return output

class Solution2:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        start, end = rounds[0], rounds[-1]
        if start <= end:
            return [i for i in range(start, end+1)]
        else:
            return [i for i in range(1, end+1)] + [i for i in range(start, n+1)]

# Unit Tests
import unittest
funcs = [Solution().mostVisited, Solution2().mostVisited]
class TestMostVisited(unittest.TestCase):
    def testMostVisited1(self):
        for mostVisited in funcs:
            n = 4
            rounds = [1,3,1,2]
            self.assertEqual(mostVisited(n=n, rounds=rounds), [1,2])

    def testMostVisited2(self):
        for mostVisited in funcs:
            n = 2
            rounds = [2,1,2,1,2,1,2,1,2]
            self.assertEqual(mostVisited(n=n, rounds=rounds), [2])

    def testMostVisited3(self):
        for mostVisited in funcs:
            n = 7
            rounds = [1,3,5,7]
            self.assertEqual(mostVisited(n=n, rounds=rounds), [1,2,3,4,5,6,7])

if __name__ == "__main__":
    unittest.main()
