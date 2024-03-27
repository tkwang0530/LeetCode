"""
1220. Count Vowels Permutation
description: https://leetcode.com/problems/count-vowels-permutation/description/
"""

"""
Note:
1. dp: O(n) time | O(1) space
"""

import collections
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        if n == 1:
            return 5
        followedBy = {
            "a": ["e"],
            "e": ["a", "i"],
            "i": ["a", "e", "o", "u"],
            "o": ["i", "u"],
            "u": ["a"]
        }

        dp = collections.defaultdict(int)
        dp["a"] = dp["e"] = dp["i"] = dp["o"] = dp["u"] = 1
        before = collections.defaultdict(set)
        for vowel, afters in followedBy.items():
            for after in afters:
                before[after].add(vowel)

        for _ in range(n-1):
            newDp = collections.defaultdict(int)
            for char in dp.keys():
                for b in before[char]:
                    newDp[char] += dp[b]
            dp = newDp
        return sum(dp.values()) % (10 ** 9 + 7)
            

# Unit Tests
import unittest
funcs = [Solution().countVowelPermutation]


class TestCountVowelPermutation(unittest.TestCase):
    def testCountVowelPermutation1(self):
        for func in funcs:
            n = 1
            self.assertEqual(func(n=n), 5)

    def testCountVowelPermutation2(self):
        for func in funcs:
            n = 2
            self.assertEqual(func(n=n), 10)

    def testCountVowelPermutation3(self):
        for func in funcs:
            n = 5
            self.assertEqual(func(n=n), 68)

if __name__ == "__main__":
    unittest.main()
