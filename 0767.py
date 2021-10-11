"""
767. Reorganize String
Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.
Return any possible rearrangement of s or return "" if not possible.

Example1:
Input: s = "aab"
Output: "aba"

Example2:
Input: s = "aaab"
Output: ""

Constraints:
1 <= s.length <= 500
s consists of lowercase English letters
"""

"""
Note:
1. maxHeap: O(n) time | O(n) space - where n is the length of given string s
(1) store the char count using collections.Counter(s)
(2) using a maxHeap with (-count, char)
(3) for each run, pop two items out and append one by one, heappush back to the maxHeap if new count are still larger than 0
"""
import collections
import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        charCount = collections.Counter(s)
        if len(s) % 2 == 1 and max(charCount.values()) > len(s) // 2 + 1:
            return ""
        if len(s) % 2 == 0 and max(charCount.values()) > len(s) // 2:
            return ""
        
        maxHeap = []
        for char, count in charCount.items():
            heapq.heappush(maxHeap, (-1 * count, char))
        
        chars = []
        while len(chars) < len(s):
            if len(maxHeap) == 1:
                chars.append(heapq.heappop(maxHeap)[1])
            else:
                firstMaxItem = heapq.heappop(maxHeap)
                secondMaxItem = heapq.heappop(maxHeap)
                chars.append(firstMaxItem[1])
                chars.append(secondMaxItem[1])

                newFirstItemCount = -1 * firstMaxItem[0] - 1
                newSecondItemCount = -1 * secondMaxItem[0] - 1
                if newFirstItemCount > 0:
                    heapq.heappush(maxHeap, (-1 * (newFirstItemCount), firstMaxItem[1]))
                if newSecondItemCount> 0:
                    heapq.heappush(maxHeap, (-1 * (newSecondItemCount), secondMaxItem[1]))
        return "".join(chars)

# Unit Tests
import unittest
funcs = [Solution().reorganizeString]


class TestReorganizeString(unittest.TestCase):
    def testReorganizeString1(self):
        for func in funcs:
            s = "aab"
            self.assertEqual(func(s=s), "aba")

    def testReorganizeString2(self):
        for func in funcs:
            s = "aaab"
            self.assertEqual(func(s=s), "")

    def testReorganizeString3(self):
        for func in funcs:
            s = "vvvlo"
            self.assertTrue(func(s=s) in ("vlvov", "vlvov"))

if __name__ == "__main__":
    unittest.main()
