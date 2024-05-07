"""
2100. Find Good Days to Rob the Bank
description: https://leetcode.com/problems/find-good-days-to-rob-the-bank/description/
"""

"""
Note:
1. Prefix concept: O(n) time | O(n) space - where n is the length of array security
"""

import unittest
from typing import List
class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        nonIncreaseCount = [0] * n
        nonDecreaseCount = [0] * n
        
        for i in range(1, n):
            nonIncreaseCount[i] = nonIncreaseCount[i-1]+1 if security[i] <= security[i-1] else 0
            
        for i in range(n-2, -1, -1):
            nonDecreaseCount[i] = nonDecreaseCount[i+1]+1 if security[i] <= security[i+1] else 0
        
        output = []
        for i in range(n):
            if nonIncreaseCount[i] >= time and nonDecreaseCount[i] >= time:
                output.append(i)
        return output

# Unit Tests
import unittest
funcs = [Solution().goodDaysToRobBank]
class TestGoodDaysToRobBank(unittest.TestCase):
    def testGoodDaysToRobBank1(self):
        for func in funcs:
            security = [5,3,3,3,5,6,2]
            time = 2
            self.assertEqual(func(security=security, time=time), [2,3])

    def testGoodDaysToRobBank2(self):
        for func in funcs:
            security = [1,1,1,1,1]
            time = 0
            self.assertEqual(func(security=security, time=time), [0,1,2,3,4])

    def testGoodDaysToRobBank3(self):
        for func in funcs:
            security = [1,2,3,4,5,6]
            time = 2
            self.assertEqual(func(security=security, time=time), [])

if __name__ == "__main__":
    unittest.main()
