"""
1854. Maximum Population Year
You are given a 2D integer array logs where each logs[i] = [birthi, deathi] indicates the birth and death years of the ith person.

The population of some year x is the number of people alive during that year. The ith person is counted in year x's population if x is in the inclusive range [birthi, deathi - 1]. Note that the person is not counted in the year that they die.

Return the earliest year with the maximum population.

Example1:
Input: logs = [[1993,1999],[2000,2010]]
Output: 1993
Explanation: The maximum population is 1, and 1993 is the earliest year with this population.

Example2:
Input: logs = [[1950,1961],[1960,1971],[1970,1981]]
Output: 1960
Explanation: 
The maximum population is 2, and it had happened in years 1960 and 1970.
The earlier year between them is 1960.

Constraints:
1 <= logs.length <= 100
1950 <= birth_i < death_i <= 2050
"""

"""
Note:
1. Sort + Sweep Line: O(nlogn) time | O(n) space - where n is the length of array logs
"""

import collections
from typing import List
class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        sweep = collections.defaultdict(int)
        for birth, death in logs:
            sweep[birth] += 1
            sweep[death] -= 1
        
        targetYear = 0
        maxPopulation = 0
        current = 0
        for year in sorted(sweep.keys()):
            current += sweep[year]
            if current > maxPopulation:
                maxPopulation = current
                targetYear = year
        return targetYear

# Unit Tests
import unittest
funcs = [Solution().maximumPopulation]

class TestMaximumPopulation(unittest.TestCase):
    def testMaximumPopulation1(self):
        for func in funcs:
            logs = [[1993,1999],[2000,2010]]
            self.assertEqual(func(logs=logs), 1993)

    def testMaximumPopulation2(self):
        for func in funcs:
            logs = [[1950,1961],[1960,1971],[1970,1981]]
            self.assertEqual(func(logs=logs), 1960)

if __name__ == "__main__":
    unittest.main()