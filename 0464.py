"""
464. Can I Win
description: https://leetcode.com/problems/can-i-win/description/
"""

"""
Note:
1. bitmask + dfs+ memo: O(2^M*M) time | O(2^M) space - where M is maxChoosableInteger
"""

import functools
class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if desiredTotal <= 0:
            return True

        if (1+maxChoosableInteger)*maxChoosableInteger//2 < desiredTotal:
            return False
    
        @functools.lru_cache(None)
        def dfs(mask, desiredTotal) -> bool:
            if desiredTotal <= 0:
                return False
            
            for i in range(maxChoosableInteger):
                if mask & (1 << i) > 0:
                    continue

                if not dfs(mask | (1 << i), desiredTotal-(i+1)):
                    return True

            return False
        return dfs(0, desiredTotal)

# Unit Tests
import unittest
funcs = [Solution().canIWin]

class TestCanIWin(unittest.TestCase):
    def testCanIWin1(self):
        for func in funcs:
            maxChoosableInteger = 10
            desiredTotal = 11
            self.assertEqual(func(maxChoosableInteger=maxChoosableInteger, desiredTotal=desiredTotal), False)

    def testCanIWin2(self):
        for func in funcs:
            maxChoosableInteger = 10
            desiredTotal = 0
            self.assertEqual(func(maxChoosableInteger=maxChoosableInteger, desiredTotal=desiredTotal), True)

    def testCanIWin3(self):
        for func in funcs:
            maxChoosableInteger = 10
            desiredTotal = 1
            self.assertEqual(func(maxChoosableInteger=maxChoosableInteger, desiredTotal=desiredTotal), True)

if __name__ == "__main__":
    unittest.main()