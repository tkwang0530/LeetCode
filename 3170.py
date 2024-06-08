"""
3170. Lexicographically Minimum String After Removing Stars
description: https://leetcode.com/problems/lexicographically-minimum-string-after-removing-stars/description/
"""

""" 
Notes:
1. minHeap: O(nlogn) time | O(n) space - where n is the length of s
"""

import heapq
class Solution:
    def clearStars(self, s: str) -> str:
        minHeap = []
        exists = [True] * len(s)
        for i, char in enumerate(s):
            if char == "*":
                _, negIdx = heapq.heappop(minHeap)
                idx = -1 * negIdx
                exists[idx] = False
            else:
                heapq.heappush(minHeap, (char, -1 * i))
                
        return "".join([s[i] for i in range(len(s)) if exists[i] and s[i] != "*"])

# Unit Tests
import unittest
funcs = [Solution().clearStars]

class TestClearStars(unittest.TestCase):
    def testClearStars1(self):
        for func in funcs:
            s = "aaba*"
            self.assertEqual(func(s=s), "aab")

    def testClearStars2(self):
        for func in funcs:
            s = "abc"
            self.assertEqual(func(s=s), "abc")

if __name__ == "__main__":
    unittest.main()
