"""
1405. Longest Happy String
description: https://leetcode.com/problems/longest-happy-string/description/
"""

"""
Note:
1. maxHeap: O(n) time | O(n) space - where n is equal to a+b+c
"""

import heapq
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        maxHeap = []
        for count, char in [(a, "a"), (b, "b"), (c, "c")]:
            if count > 0:
                heapq.heappush(maxHeap, (-count, char))

        output = []
        while maxHeap:
            negCount, char = heapq.heappop(maxHeap)
            count = -negCount
            if len(output) >= 2 and output[-1] == output[-2] == char:
                if not maxHeap:
                    break
                negCount2, char2 = heapq.heappop(maxHeap)
                count2 = -negCount2
                output.append(char2)
                count2 -= 1
                if count2:
                    heapq.heappush(maxHeap, (-count2, char2))
            else:
                output.append(char)
                count -= 1
            if count:
                heapq.heappush(maxHeap, (-count, char))

        return "".join(output)

funcs = [Solution().longestDiverseString]

import unittest
class TestLongestDiverseString(unittest.TestCase):
    def testLongestDiverseString1(self):
        for func in funcs:
            a = 1
            b = 1
            c = 7
            self.assertTrue(func(a=a, b=b, c=c) in ("ccaccbcc", "ccbccacc"))

    def testLongestDiverseString2(self):
        for func in funcs:
            a = 7
            b = 1
            c = 0
            self.assertEqual(func(a=a, b=b, c=c), "aabaa")

if __name__ == "__main__":
    unittest.main()
