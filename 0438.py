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
"""



from typing import List
import unittest
class Solution(object):
    def findAnagrams(self, s: str, p: str) -> List[int]:
        start = matched = 0
        dict = {}
        result = []
        for letter in p:
            dict[letter] = dict.get(letter, 0) + 1
        for end, letter in enumerate(s):
            if letter in dict:
                dict[letter] -= 1
                if dict[letter] == 0:
                    matched += 1
            if matched == len(dict):
                result.append(start)
            if end - start + 1 >= len(p):
                if s[start] in dict:
                    if dict[s[start]] == 0:
                        matched -= 1
                    dict[s[start]] += 1
                start += 1
        return result
                    



# Unit Tests
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
