"""
1701. Average Waiting Time
description: https://leetcode.com/problems/average-waiting-time/description/
"""

"""
Note:
1. One pass: O(n) time | O(1) space - where n is the length of the customers list
"""



from typing import List
import unittest
class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        current = 0
        totalWait = 0
        for arrival, prepare in customers:
            if current <= arrival:
                current = arrival+prepare
                totalWait += prepare
            else:
                totalWait += current+prepare-arrival
                current += prepare
        return totalWait / len(customers)
# Unit Tests
funcs = [Solution().averageWaitingTime]

class TestAverageWaitingTime(unittest.TestCase):
    def testAverageWaitingTime1(self):
        for func in funcs:
            customers = [[1,2],[2,5],[4,3]]
            self.assertEqual(func(customers=customers), 5.0)

    def testAverageWaitingTime2(self):
        for func in funcs:
            customers = [[5,2],[5,4],[10,3],[20,1]]
            self.assertEqual(func(customers=customers), 3.25)

if __name__ == "__main__":
    unittest.main()
