"""
202. Happy Number
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

Example1:
Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

Example2:
Input: n = 2
Output: false

Constraints:
1 <= n <= 2^31 - 1
"""

"""
Note:
1. HashTable: O(1) space | O(1) time
"""

class Solution:
    def isHappy(self, n: int) -> bool:
        visitedSum = {n}
        result = n
        def getSquareSums(n):
            return sum([int(numStr) * int(numStr) for numStr in str(n)])
        
        while result != 1:
            result = getSquareSums(result)
            if result in visitedSum:
                return False
            visitedSum.add(result)
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
