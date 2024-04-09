"""
2073. Time Needed to Buy Tickets
description: https://leetcode.com/problems/time-needed-to-buy-tickets/description
"""

"""
Note:
1. Simulation with queue: O(T) time | O(n) space - where T is the sum of the array tickets and n is the length of array tickets
2. One pass: O(n) time | O(1) space - where n is the length of array tickets
ref: https://www.youtube.com/watch?v=cVmS9N6kf2Y
"""

from typing import List
import collections
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = collections.deque()
        for i, num in enumerate(tickets):
            queue.append((i, num))

        time = 0
        while queue:
            idx, count = queue.popleft()
            count -= 1
            time += 1
            if count == 0 and idx == k:
                return time

            if count > 0:
                queue.append((idx, count))
        return 0

class Solution2:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        seconds = 0
        for i, num in enumerate(tickets):
            if i <= k:
                seconds += min(num, tickets[k])
            else:
                seconds += min(num, tickets[k]-1)
        return seconds

# Unit Tests
import unittest
funcs = [Solution().timeRequiredToBuy, Solution2().timeRequiredToBuy] 

class TestTimeRequiredToBuy(unittest.TestCase):
    def testTimeRequiredToBuy1(self):
        for func in funcs:
            tickets = [2,3,2]
            k = 2
            self.assertEqual(func(tickets=tickets, k=k), 6)
    
    def testTimeRequiredToBuy2(self):
        for func in funcs:
            tickets = [5,1,1,1]
            k = 0
            self.assertEqual(func(tickets=tickets, k=k), 8)

if __name__ == "__main__":
    unittest.main()
