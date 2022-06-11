"""
1698. Number of Distinct Substrings in a String
Given a string s, return the number of distinct substrings of s.

A substring of a string is obtained by deleting any number of characters (possibly zero) from the front of the string and any number (possibly zero) from the back of the string.

Example1:
Input: s = "aabbaba"
Output: 21
Explanation: The set of distinct strings is ["a","b","aa","bb","ab","ba","aab","abb","bab","bba","aba","aabb","abba","bbab","baba","aabba","abbab","bbaba","aabbab","abbaba","aabbaba"]

Example2:
Input: s = "abcdefg"
Output: 28

Constraints:
1 <= s.length <= 500
s consists of lowercase English letters.
"""

"""
Note:
1. Rolling Hash: O(n^2) time | O(n) space - where n is the length of string s
"""

import collections
from typing import List
class Solution:
    def countDistinct(self, s: str) -> int:
        MOD = 1e9 + 7
        a = 26
        n = len(s)
        power = [1] * n
        for i in range(1, n):
            power[i] = (power[i-1] * a) % MOD
        
        # map characters into numbers
        nums = [ord(char) - ord('a') for char in s]
        def search(L: int, nums: List[int]) -> int:
            if L == n:
                return 1
            h = 0
            # calculate the initial window hash value
            for i in range(L):
                h = (h * a + nums[i]) % MOD

            hashStartIndice = collections.defaultdict(list)
            hashStartIndice[h].append(0)
            for start in range(1, n-L+1):
                h = h * a  # move window
                h = (h - nums[start - 1] * power[L] % MOD + MOD) % MOD  # remove tail digit
                h = (h + nums[start + L - 1]) % MOD # add new head digit
                foundRealMatch = False
                for i in hashStartIndice[h]:
                    if nums[i:i+L] == nums[start:start+L]:
                        foundRealMatch = True
                        break
                if not foundRealMatch:
                    hashStartIndice[h].append(start)
            return sum([len(arr) for arr in hashStartIndice.values()])

        total = 0
        for length in range(1, n+1):
            count = search(length, nums)
            total += count
        return total

# Unit Tests
import unittest
funcs = [Solution().countDistinct]

class TestCountDistinct(unittest.TestCase):
    def testCountDistinct1(self):
        for func in funcs:
            s = "aabbaba"
            self.assertEqual(func(s=s), 21)

    def testCountDistinct2(self):
        for func in funcs:
            s = "abcdefg"
            self.assertEqual(func(s=s), 28)

if __name__ == "__main__":
    unittest.main()
