"""
316. Remove Duplicate Letters
Given a string s, remove duplicate letters so that every letter appears once and only once.
You must make sure your result is the smallest in lexicograhical order among all possible results.

Example1:
Input: s = "bcabc"
Output: "abc"

Example2:
Input: s = "cbacdcbc"
Output: "acdb"

Constraints:
1 <= s.length <= 10^4
s consists of lowercase English letters.

Note: This question is the same as 1081
"""

"""
Note:
1. Monotonic increasing stack + HashTable: O(n) time | O(1) space
2. Monotonic increasing stack + HashTable 2: O(n) time | O(1) space
"""

import unittest
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        if len(s) == 0:
            return s
        lastOccurrence = {char: i for i, char in enumerate(s)}
        used = set()
        stack = []
        
        for i, char in enumerate(s):
            if char in used:
                continue
            while len(stack) > 0 and stack[-1] > char and  lastOccurrence[stack[-1]] > i:
                used.remove(stack[-1])
                stack.pop()
            
            stack.append(char)
            used.add(char)
        return "".join(stack)

class Solution2:
    def removeDuplicateLetters(self, s: str) -> str:
        lastCharIdx = {}
        charSet = set()
        for i, char in enumerate(s):
            lastCharIdx[char] = i
            charSet.add(char)

        stack = [] # char
        charIdxMap = {}
        for i, char in enumerate(s):
            if char in charIdxMap:
                charIdxMap[char] = i
                continue

            while stack and ord(stack[-1]) >= ord(char):
                c = stack[-1]
                if charIdxMap[c] == lastCharIdx[c]:
                    break
                stack.pop()
                del charIdxMap[c]

            stack.append(char)
            charIdxMap[char] = i
        return "".join([char for char in stack[:len(charSet)]])

# Unit Tests
funcs = [Solution().removeDuplicateLetters, Solution2().removeDuplicateLetters]


class TestRemoveDuplicateLetters(unittest.TestCase):
    def testRemoveDuplicateLetters1(self):
        for func in funcs:
            s = "bcabc"
            self.assertEqual(func(s=s), "abc")

    def testRemoveDuplicateLetters2(self):
        for func in funcs:
            s = "cbacdcbc"
            self.assertEqual(func(s=s), "acdb")

if __name__ == "__main__":
    unittest.main()
