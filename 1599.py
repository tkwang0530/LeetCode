"""
1599. Maximum Profit of Operating a Centennial Wheel
description: https://leetcode.com/problems/maximum-profit-of-operating-a-centennial-wheel/description/
"""

"""
Note:
1. Simulation: O(n) time | O(1) space - where n is the length of array customers
"""

from typing import List
class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        if runningCost >= 4 * boardingCost:
            return -1
    
        maxProfit = 0
        currentProfit = 0
        bestShifts = -1
        currentShifts = 0
        waitingPeople = 0
        while currentShifts < len(customers):
            waitingPeople += customers[currentShifts]
            currentProfit += min(waitingPeople, 4) * boardingCost - runningCost
            currentShifts += 1
            waitingPeople -= min(waitingPeople, 4)
            if currentProfit > maxProfit:
                maxProfit = currentProfit
                bestShifts = currentShifts

        fullShifts = waitingPeople // 4
        currentProfit += 4 * fullShifts * boardingCost - fullShifts * runningCost
        currentShifts += fullShifts
        if currentProfit > maxProfit:
            maxProfit = currentProfit
            bestShifts = currentShifts
        
        notFullShifts = 1 if (waitingPeople % 4) > 0 else 0
        if notFullShifts > 0:
            currentProfit += (waitingPeople % 4) * boardingCost -  runningCost
            currentShifts += 1
            if currentProfit > maxProfit:
                maxProfit = currentProfit
                bestShifts = currentShifts
        return bestShifts

# Unit Tests
import unittest
funcs = [Solution().minOperationsMaxProfit]

class TestMinOperationsMaxProfit(unittest.TestCase):
    def testMinOperationsMaxProfit1(self):
        for minOperationsMaxProfit in funcs:
            customers = [8,3]
            boardingCost = 5
            runningCost = 6
            self.assertEqual(minOperationsMaxProfit(customers=customers, boardingCost=boardingCost, runningCost=runningCost), 3)

    def testMinOperationsMaxProfit2(self):
        for minOperationsMaxProfit in funcs:
            customers = [10,9,6]
            boardingCost = 6
            runningCost = 4
            self.assertEqual(minOperationsMaxProfit(customers=customers, boardingCost=boardingCost, runningCost=runningCost), 7)

    def testMinOperationsMaxProfit3(self):
        for minOperationsMaxProfit in funcs:
            customers = [3,4,0,5,1]
            boardingCost = 1
            runningCost = 92
            self.assertEqual(minOperationsMaxProfit(customers=customers, boardingCost=boardingCost, runningCost=runningCost), -1)

if __name__ == "__main__":
    unittest.main()