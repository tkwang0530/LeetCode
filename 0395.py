"""
395. Longest Substring With At Least K Repeating Characters
Given a string s and an integer k, return the length of the longest substring of s such that the frequency of each character in this substring is greater than or equal to k.

Example1:
Input: s = "aaabb", k = 3
Output: 3
Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.

Example2:
Input: s = "ababbc", k = 2
Output: 5
Explanation: The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.

Constraints:
1 <= s.length <= 10^4
s consists of only lowercase English letters.
1 <= k <= 10^5
"""

""" 
Notes:
1. Sliding Window: O(n) time | O(1) space
"""

from collections import Counter
import unittest
class Solution(object):
    def longestSubstring(self, s: str, k: int) -> int:
        if k == 0:
            return len(s)
        longest, maxUnique = 0, len(set(s))
        for unique in range(1, maxUnique + 1):
            counter = Counter()
            left, currUnique, constraints = 0, 0, 0
            for right in range(len(s)):
                counter[s[right]] += 1
                if counter[s[right]] == 1:
                    currUnique += 1
                if counter[s[right]] == k:
                    constraints += 1

                if constraints == unique and currUnique == unique:
                    longest = max(longest, right-left+1)
                while left < right and currUnique > unique:
                    counter[s[left]] -= 1
                    if counter[s[left]] == 0:
                        currUnique -= 1
                    if counter[s[left]] == k-1:
                        constraints -= 1
                    left += 1
        return longest

# Unit Tests
funcs = [Solution().longestSubstring]


class TestLongestSubstring(unittest.TestCase):
    def testLongestSubstring1(self):
        for func in funcs:
            s = "aaabb"
            k = 3
            self.assertEqual(func(s=s, k=k), 3)

    def testLongestSubstring2(self):
        for func in funcs:
            s = "ababbc"
            k = 2
            self.assertEqual(func(s=s, k=k), 5)

    def testLongestSubstring3(self):
        for func in funcs:
            s = "aaabbb"
            k = 3
            self.assertEqual(func(s=s, k=k), 6)

if __name__ == "__main__":
    unittest.main()
