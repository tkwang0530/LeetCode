"""
1553. Minimum Number of Days to Eat N Oranges
description: https://leetcode.com/problems/minimum-number-of-days-to-eat-n-oranges/description/
"""

"""
Note:
1. DFS + memo: O(logn) time | O(logn) space
2. BFS + HashSet: O(logn) time | O(logn) space
"""

import collections
import functools
class Solution:
    @functools.lru_cache()
    def minDays(self, n: int) -> int:
        if n <= 1:
            return n
        return 1 + min(n % 2 + self.minDays(n // 2), n % 3 + self.minDays(n // 3))

class Solution2:
    def minDays(self, n: int) -> int:
        queue = collections.deque([(0, n)])
        remainSet = {n}
        while queue:
            day, remain = queue.popleft()
            if remain == 0:
                return day

            if remain % 3 == 0 and remain-2*remain//3 not in remainSet:
                queue.append((day+1,remain-2*remain//3))
                remainSet.add(remain-2*remain//3)

            if remain % 2 == 0 and remain-remain//2 not in remainSet:
                queue.append((day+1,remain-remain//2))
                remainSet.add(remain-remain//2)

            if remain - 1 not in remainSet:
                queue.append((day+1,remain-1))
                remainSet.add(remain-1)
        return day

# Unit Tests
import unittest
funcs = [Solution().minDays, Solution2().minDays]
class TestMinDays(unittest.TestCase):
    def testMinDays1(self):
        for minDays in funcs:
            n = 10
            self.assertEqual(minDays(n=n), 4)

    def testMinDays2(self):
        for minDays in funcs:
            n = 6
            self.assertEqual(minDays(n=n), 3)

if __name__ == "__main__":
    unittest.main()
