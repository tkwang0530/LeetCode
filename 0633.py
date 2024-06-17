"""
633. Sum of Square Numbers
description: https://leetcode.com/problems/sum-of-square-numbers/description/
"""

"""
Note:
1. HashSet: O(sqrt(c)) time | O(sqrt(c)) space
2. Two Pointers: O(sqrt(c)) time | O(1) space
"""

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        squares = set()
        for i in range(int(c ** 0.5)+1):
            if c - i*i in squares or c == 2 * i * i:
                return True
            
            squares.add(i*i)
        return False

class Solution2:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = int(c ** 0.5)
        while left <= right:
            currentSum = left*left + right*right
            if currentSum == c:
                return True
            elif currentSum > c:
                right -= 1
            else:
                left += 1
        return False

# Unit Tests
import unittest
funcs = [Solution().judgeSquareSum, Solution2().judgeSquareSum]
class TestJudgeSquareSum(unittest.TestCase):
    def testJudgeSquareSum1(self):
        for func in funcs:
            c = 5
            self.assertEqual(func(c), True)


    def testJudgeSquareSum2(self):
        for func in funcs:
            c = 3
            self.assertEqual(func(c), False)


if __name__ == "__main__":
    unittest.main()
