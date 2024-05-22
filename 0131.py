"""
131. Palindrome Partitioning
description: https://leetcode.com/problems/palindrome-partitioning/description/
"""

"""
Note:
1. backtrack: O(2^n * n) time | O(2^n * n) space - n is the length of the input string
"""

from typing import List
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        output = []
        current = []
        currentChars = 0

        def isPalindrome(s: str):
            left, right = 0, len(s)-1
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        def backtrack(i, currentChars):
            if i == n:
                if currentChars == n:
                    output.append(current.copy())
                return

            for j in range(i+1, n+1):
                subs = s[i:j]
                if isPalindrome(subs):
                    current.append(subs)
                    backtrack(j, currentChars+len(subs))
                    current.pop()
        
        backtrack(0, 0)
        return output

# Unit Tests
import unittest
funcs = [Solution().partition]
class TestPartition(unittest.TestCase):
    def testPartition1(self):
        for func in funcs:
            s = "aab"
            self.assertEqual(func(s), [["a", "a", "b"], ["aa", "b"]])

    def testPartition2(self):
        for func in funcs:
            s = "a"
            self.assertEqual(func(s), [["a"]])

if __name__ == "__main__":
    unittest.main()
