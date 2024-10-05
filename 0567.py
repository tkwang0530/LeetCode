"""
567. Permutation in String
description: https://leetcode.com/problems/permutation-in-string/description/
"""

"""
Note:
1. Sliding Window + HashTable: O(m+n) time | O(26) space - where m is the length of string s1 and n is the length of string  s2
"""

import collections
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        targetCounter = collections.Counter(s1)
        start = 0
        runningCounter = collections.defaultdict(int)
        for end in range(len(s2)):
            char = s2[end]
            runningCounter[char] += 1
            if char not in targetCounter:
                start = end+1
                runningCounter = collections.defaultdict(int)
                continue
            
            while start < len(s2) and runningCounter[char] > targetCounter[char]:
                runningCounter[s2[start]] -= 1
                start += 1
            
            if end-start+1 == len(s1):
                return True

        return False

funcs = [Solution().checkInclusion]

import unittest
class TestCheckInclusion(unittest.TestCase):
    def testCheckInclusion1(self):
        for func in funcs:
            s1 = "ab"
            s2 = "eidbaooo"
            self.assertEqual(func(s1=s1, s2=s2), True)

    def testCheckInclusion2(self):
        for func in funcs:
            s1 = "ab"
            s2 = "eidboaoo"
            self.assertEqual(func(s1=s1, s2=s2), False)

if __name__ == "__main__":
    unittest.main()
