"""
202. Happy Number
description: https://leetcode.com/problems/happy-number/description/
"""

"""
Note:
1. HashTable: O(1) space | O(1) time
"""

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        def convert(x):
            return sum([int(dStr) * int(dStr) for dStr in str(x)])

        while n > 1:
            new = convert(n)
            if new in seen:
                return False
            seen.add(new)
            n = new
        return True

# Unit Tests
import unittest
funcs = [Solution().isHappy]

class TestIsHappy(unittest.TestCase):
    def testIsHappy1(self):
        for func in funcs:
            n = 19
            self.assertEqual(func(n=n), True)

    def testIsHappy2(self):
        for func in funcs:
            n = 2
            self.assertEqual(func(n=n), False)

if __name__ == "__main__":
    unittest.main()
