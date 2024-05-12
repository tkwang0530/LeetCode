"""
2745. Construct the Longest New String
description: https://leetcode.com/problems/construct-the-longest-new-string/description/
"""

"""
Note:
1. dfs+memo: O(x*y*z*3) time | O(x*y*z*3) space
2. Greedy: O(1) time | O(1) space
ref: https://leetcode.com/problems/construct-the-longest-new-string/solutions/3677618/java-c-python-1-line-o-1
"""

import functools
class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        @functools.lru_cache(None)
        def dfs(x, y, z, prev) -> int:
            if (x,y,z) == (0,0,0):
                return 0
            
            maxLen = 0
            # use x if x > 0 and prev != "x"
            if x > 0 and prev != "x":
                maxLen = max(maxLen, 2+dfs(x-1, y, z, "x"))
            
            # use y if y > 0 and prev != "y" and prev != "z"
            if y > 0 and prev not in ("y", "z"):
                maxLen = max(maxLen, 2+dfs(x, y-1, z, "y"))

            # use z if z > 0 and prev != "x"
            if z > 0 and prev != "x":
                maxLen = max(maxLen, 2+dfs(x, y, z-1, "z"))

            return maxLen

        return dfs(x, y, z, "")

class Solution2:
    def longestString(self, x: int, y: int, z: int) -> int:
        return (min(x, y+1) + min(x+1, y) + z) * 2

# Unit Tests
import unittest
funcs = [Solution().longestString, Solution2().longestString]


class TestLongestString(unittest.TestCase):
    def testLongestString1(self):
        for func in funcs:
            x = 2
            y = 5
            z = 1
            self.assertEqual(func(x=x, y=y, z=z), 12)


    def testLongestString2(self):
        for func in funcs:
            x = 3
            y = 2
            z = 2
            self.assertEqual(func(x=x, y=y, z=z), 14)


if __name__ == "__main__":
    unittest.main()