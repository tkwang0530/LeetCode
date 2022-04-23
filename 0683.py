"""
683. K Empty Slots
You have n bulbs in a row numbered from 1 to n. Initially, all the bulbs are turned off.
We turn on exactly one bulb every day until all bulbs are on after n days.

You are given an array bulbs of length n where bulbs[i] = x means that on the (i+1)^th day, we will turn on the bulb at position x where i is 0-indexed and x is 1-indexed.

Given an integer k, return the minimum day number such that there exists two turned on bulbs that have exactly k bulbs between them that are all turned off. If there isn't such day, return -1.

Example1:
Input: bulbs = [1,3,2], k = 1
Output: 2
Explanation:
On the first day: bulbs[0] = 1, first bulb is turned on: [1,0,0]
On the second day: bulbs[1] = 3, third bulb is turned on: [1,0,1]
On the third day: bulbs[2] = 2, second bulb is turned on: [1,1,1]
We return 2 because on the second day, there were two on bulbs with one off bulb between them.

Example2:
Input: bulbs = [1,2,3], k = 1
Output: -1

Constraints:
n == bulbs.length
1 <= n <= 2 * 10^4
1 <= bulbs[i] <= n
bulbs is a permutation of numbers from 1 to n.
0 <= k <= 2 * 10^4
"""

""" 
1. Monotonic increasing stack: O(n) time | O(n) space
"""
from typing import List
class Solution(object):
    def kEmptySlots(self, bulbs: List[int], k: int) -> int:
        bulbDay = {} # <bulb, day to turn on>
        for i, bulb in enumerate(bulbs):
            bulbDay[bulb] = i+1

        minDay = float("inf")
        stack = []

        for nextBulbNumber in range(1, len(bulbs) + 1):
            # if the last-turned-on bulb's turned-on day is larger than the nextBulbNumber's turned-on day, pop out the lastBulbNumber from stack
            while stack and bulbDay[stack[-1]] > bulbDay[nextBulbNumber]:
                lastBulbNumber = stack.pop()
                if abs(nextBulbNumber - lastBulbNumber) - 1 == k:
                    minDay = min(minDay, bulbDay[lastBulbNumber])
            
            # if there is bulbNumber in the stack, the nextBulbNumber's turned-on day must be larger than or eqaul to the lastBulbNumer's turned-on day
            if stack:
                lastBulbNumber = stack[-1]
                if abs(nextBulbNumber - lastBulbNumber) - 1 == k:
                    minDay = min(minDay, bulbDay[nextBulbNumber])
            
            stack.append(nextBulbNumber)
        return minDay if minDay < float("inf") else -1

# Unit Tests
import unittest
funcs = [Solution().kEmptySlots]


class TestKEmptySlots(unittest.TestCase):
    def testKEmptySlots1(self):
        for func in funcs:
            bulbs = [1,3,2]
            k = 1
            self.assertEqual(func(bulbs=bulbs, k=k), 2)

    def testKEmptySlots2(self):
        for func in funcs:
            bulbs = [1,2,3]
            k = 1
            self.assertEqual(func(bulbs=bulbs, k=k), -1)

if __name__ == "__main__":
    unittest.main()
