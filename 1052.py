"""
1052. Grumpy Bookstore Owner
description: https://leetcode.com/problems/grumpy-bookstore-owner/description/
"""

"""
Note:
1. Sliding Window: O(n) time | O(1) space - where n is the length of array customers
2. Sliding Window (one pass): O(n) time | O(1) space - where n is the length of array customers
"""




import unittest
from typing import List
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        currentCount = 0
        for i in range(n):
            currentCount += customers[i] * (grumpy[i] == 0)

        maxCount = currentCount

        start = 0
        for end in range(n):
            currentCount += grumpy[end] * customers[end]
            if end - start + 1 > minutes:
                currentCount -= grumpy[start] * customers[start]
                start += 1
            maxCount = max(maxCount, currentCount)
        return maxCount

class Solution2:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        start = 0
        window = 0
        satisfied = 0
        maxWindow = 0
        for end in range(len(customers)):
            if grumpy[end]:
                window += customers[end]
            else:
                satisfied += customers[end]

            if end - start + 1 > minutes:
                window -= customers[start] * grumpy[start]
                start += 1
            
            maxWindow = max(maxWindow, window)

        return satisfied + maxWindow
            

# Unit Tests
funcs = [Solution().maxSatisfied, Solution2().maxSatisfied]


class TestMaxSatisfied(unittest.TestCase):
    def testMaxSatisfied1(self):
        for func in funcs:
            customers = [1, 0, 1, 2, 1, 1, 7, 5]
            grumpy = [0, 1, 0, 1, 0, 1, 0, 1]
            minutes = 3
            self.assertEqual(
                func(customers=customers, grumpy=grumpy, minutes=minutes), 16)

    def testMaxSatisfied2(self):
        for func in funcs:
            customers = [1]
            grumpy = [0]
            minutes = 1
            self.assertEqual(
                func(customers=customers, grumpy=grumpy, minutes=minutes), 1)


if __name__ == "__main__":
    unittest.main()
