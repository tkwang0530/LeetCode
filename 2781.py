"""
2781. Length of the Longest Valid Substring
You are given a string word and an array of strings forbidden.

A string is called valid if none of its substrings are present in forbidden.

Return the length of the longest valid substring of the string word.

A substring is a contiguous sequence of characters in a string, possibly empty.

Example1:
Input: word = "cbaaaabc", forbidden = ["aaa","cb"]
Output: 4
Explanation: There are 9 valid substrings in word: "c", "b", "a", "ba", "aa", "bc", "baa", "aab", and "aabc". The length of the longest valid substring is 4. 
It can be shown that all other substrings contain either "aaa" or "cb" as a substring. 

Example2:
Input: word = "leetcode", forbidden = ["de","le","e"]
Output: 4
Explanation: There are 11 valid substrings in word: "l", "t", "c", "o", "d", "tc", "co", "od", "tco", "cod", and "tcod". The length of the longest valid substring is 4.
It can be shown that all other substrings contain either "de", "le", or "e" as a substring. 

Constraints:
1 <= word.length <= 10^5
word consists only of lowercase English letters.
1 <= forbidden.length <= 10^5
1 <= forbidden[i].length <= 10
forbidden[i] consists only of lowercase English letters.
"""

"""
Note:
1. HashTable + Sliding Window: O(w + f) time | O(f) space - where w is the length of string word and f is the length of array forbidden
"""

from typing import List
class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        forbiddenSet = set(forbidden)
        n = len(word)
        start = 0
        longest = 0
        for end in range(n):
            for k in range(end, max(end-10, start)-1, -1):
                subword = word[k:end+1]
                if subword in forbiddenSet:
                    start = k+1
                    break
            longest = max(longest, end - start+1)
        return longest

# Unit Tests
import unittest
funcs = [Solution().longestValidSubstring]

class TestLongestValidSubstring(unittest.TestCase):
    def testLongestValidSubstring1(self):
        for func in funcs:
            word = "cbaaaabc"
            forbidden = ["aaa","cb"]
            self.assertEqual(func(word=word, forbidden=forbidden), 4)

    def testLongestValidSubstring2(self):
        for func in funcs:
            word = "leetcode"
            forbidden = ["de","le","e"]
            self.assertEqual(func(word=word, forbidden=forbidden), 4)

if __name__ == "__main__":
    unittest.main()