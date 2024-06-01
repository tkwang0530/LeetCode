"""
3144. Minimum Substring Partition of Equal Character Frequency
description: https://leetcode.com/problems/minimum-substring-partition-of-equal-character-frequency/description/
"""

"""
Note:
1. dfs+memo+greedy: O(n^2) time | O(n^2) space - where n is the length of string s
"""

import collections
import functools
class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        n = len(s)
        
        @functools.lru_cache(None)
        def dfs(i):
            if i == n:
                return 0
            minLen = n-i

            maxCount = 0
            counter = collections.defaultdict(int)
            for j in range(i, n):
                counter[s[j]] += 1
                if counter[s[j]] > maxCount:
                    maxCount = counter[s[j]] 

                if (j-i+1) == (maxCount * len(counter)):
                    minLen = min(minLen, 1+dfs(j+1))
            return minLen

        return dfs(0)

# Unit Tests
import unittest
funcs = [Solution().minimumSubstringsInPartition]

class TestMinimumSubstringsInPartition(unittest.TestCase):
    def testMinimumSubstringsInPartition1(self):
        for func in funcs:
            s = "fabccddg"
            self.assertEqual(func(s=s), 3)


    def testMinimumSubstringsInPartition2(self):
        for func in funcs:
            s = "abababaccddb"
            self.assertEqual(func(s=s), 2)


if __name__ == "__main__":
    unittest.main()