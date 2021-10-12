"""
374. Guess Number Higher or Lower
We are playing the Guess Game. The game is as follows:
I pick a number from 1 to n. You have to guess which number I picked.
Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.
You call a pre-defined API int guess(int num), which returns 3 possible results:
- -1: The number I picked is lower than your guess (i.e. pick < num).
- 1: The number I picked is higher than your guess (i.e. pick > num).
- 0: The number I picked is equal to your guess (i.e. pick == num).

Return the number that I picked.

Example1:
Input: n = 10, pick = 6
Output: 6

Example2:
Input: n = 1, pick = 1
Output: 1

Example3:
Input: n = 2, pick = 1
Output: 1

Example4:
Input: n = 2, pick = 2
Output: 2

Constraints:
1 <= n <= 2^31 - 1
1 <= pick <= n
"""

"""
Note:
1. Binary Search: O(logn) time | O(1) space
"""
def guess(num: int) -> int:
    if 6 == num:
        return 0
    return 1 if 6 > num else -1

class Solution(object):
    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        while left <= right:
            mid = left + (right - left) // 2
            result = guess(mid)
            if result == -1:
                right = mid - 1
            elif result == 1:
                left = mid + 1
            else:
                return mid


# Unit Tests
import unittest
funcs = [Solution().guessNumber]

class TestGuessNumber(unittest.TestCase):
    def testGuessNumber1(self):
        for func in funcs:
            self.assertEqual(func(n=10), 6)

if __name__ == "__main__":
    unittest.main()