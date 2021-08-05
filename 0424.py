"""
424. Longest Repeating Character Replacement
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

Example1:
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example2:
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.

Constraints:
0 <= s.length <= 10^5
s consists of only uppercase English letters.
0 <= k <= s.length
"""

""" 
1. Sliding Window: O(n) time | O(1) space
"""

import unittest
class Solution(object):
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        dict = {}
        maxRepeat = maxLength = 0
        for end in range(len(s)):
            dict[s[end]] = dict.get(s[end], 0) + 1
            maxRepeat = max(maxRepeat, dict[s[end]])
            if end - start + 1 - maxRepeat > k:
                dict[s[start]] -= 1
                start += 1
            maxLength = max(maxLength, end - start + 1)
        return maxLength


# Unit Tests
funcs = [Solution().characterReplacement]


class TestCharacterReplacement(unittest.TestCase):
    def testCharacterReplacement1(self):
        for func in funcs:
            s = "ABAB"
            k = 2
            self.assertEqual(func(s=s, k=k), 4)

    def testCharacterReplacement2(self):
        for func in funcs:
            s = "AABABBA"
            k = 1
            self.assertEqual(func(s=s, k=k), 4)

if __name__ == "__main__":
    unittest.main()
