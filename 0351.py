"""
351. Android Unlock Patterns
Android devices have a special lock screen with a 3 x 3 grid of dots.
Users can set an "unlock pattern" by connecting the dots in a specific sequence, forming a series of joined line segments where each segment's endpoints are two consecutive dots in the sequence. A sequence of k dots is a valid unlock pattern if both of the following are true:

- All the dots in the sequence are distinct.
- If the line segment connecting two consecutive dots in the sequence passes through the center of any other dot, the other dot must have previously appeared in the sequence. No jumps through the center non-selected dots are allowed.
    - For example, connecting dots 2 and 9 without dots 5 or 6 appearing beforehand is valid because the line from dot 2 to dot 9 does not pass through the center of either dot 5 or 6.
    - However, connecting dots 1 and 3 without dot 2 appearing beforehand is invalid because the line from dot 1 to dot 3 passes through the center of dot 2.

More details: https://leetcode.com/problems/android-unlock-patterns/

Given two integers m and n, return the number of unique and valid unlock patterns of the Android grid lock screen that consist of at least m keys and at most n keys.

Two unlock patterns are considered unique if there is a dot in one sequence that is not in the other, or the order of the dots is different.

Example1:
Input: m = 1, n = 1
Output: 9

Example2:
Input: m = 1, n = 2
Output: 65

Constraints:
1 <= m, n <= 9
"""

""" 
1. dfs + bitmap + memo
"""

class Solution(object):
    def numberOfPatterns(self, m: int, n: int) -> int:
        def isExist(bitmask, i):
            return (bitmask & 2**(i-1)) > 0
        
        def checkMiddle(x, y):
            if x > y:
                x, y = y, x
            return (x, y) in {(1, 3), (1, 7), (1, 9), (3, 7), (3, 9), (7, 9), (2, 8), (4,6)}

        def dfs(i, step, maxStep, bitmask):
            nonlocal ans
            
            bitmask |= 2**(i-1)

            if (bitmask, i) in memo:
                return memo[bitmask, i]
            
            if step == maxStep:
                return 1
            
            current = 0
            for neighbor in range(1, 10):
                if isExist(bitmask, neighbor) or (checkMiddle(i, neighbor) and isExist(bitmask, (i+neighbor) // 2) == False):
                    continue
                current += dfs(neighbor, step+1, maxStep, bitmask)
            
            memo[bitmask, i] = current
            return current
        
        ans = 0
        for maxStep in range(m, n+1):
            memo = {}
            for i in range(1, 10):
                ans += dfs(i, 1, maxStep, 0)
        
        return ans


# Unit Tests
import unittest
funcs = [Solution().numberOfPatterns]


class TestNumberOfPatterns(unittest.TestCase):
    def testNumberOfPatterns1(self):
        for func in funcs:
            m = 1
            n = 1
            self.assertEqual(func(m=m, n=n), 9)

    def testNumberOfPatterns2(self):
        for func in funcs:
            m = 1
            n = 2
            self.assertEqual(func(m=m, n=n), 65)

if __name__ == "__main__":
    unittest.main()
