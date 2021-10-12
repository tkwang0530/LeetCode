"""
438. Find All Anagrams in a String
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

Example1:
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example2:
Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

Constraints:
1 <= s.length, p.length <= 3 * 10^4
s and p consist of lowercase English letters
"""

""" 
1. HashTable/Sliding Window: O(n+m) time | O(1) space
(1) use collections.Counter to generate charCount
(2) apply sliding windows with the following rules
    - keep extending  right side of the window and decrease the charCount[char] if char in charCount, update the matched variable if updated charCount[char] == 0
    - if matched == len(charCount): append the start index into result list
    - if end - start + 1 == len(p): shrink the left side of the window and increase the charCount[s[start]] if s[start] in charCount, update the matched variable when init charCounts[start]] == 0
"""



from typing import List
import collections
class Solution(object):
    def findAnagrams(self, s: str, p: str) -> List[int]:
        charCount = collections.Counter(p)
        start = matched = 0
        result = []
        for end, char in enumerate(s):
            if char in charCount:
                charCount[char] -= 1
                if charCount[char] == 0:
                    matched += 1
            if matched == len(charCount):
                result.append(start)
            if end - start + 1 >= len(p):
                if s[start] in charCount:
                    if charCount[s[start]] == 0:
                        matched -= 1
                    charCount[s[start]] += 1
                start += 1
        return result


# Unit Tests
import unittest
funcs = [Solution().findAnagrams]
class TestFindAnagrams(unittest.TestCase):
    def testFindAnagrams1(self):
        for func in funcs:
            s = "cbaebabacd"
            p = "abc"
            self.assertEqual(func(s=s, p=p), [0, 6])

    def testFindAnagrams2(self):
        for func in funcs:
            s = "abab"
            p = "ab"
            self.assertEqual(func(s=s, p=p), [0, 1, 2])

if __name__ == "__main__":
    unittest.main()
