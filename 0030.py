"""
30. Substring with Concatenation of All Words
You are given a string s and an array of strings words of the same length.
Return all starting indices of substring(s) in s that is a concatenation of each word in words exactly once, in any order, and without any intervening characters.

You can return the answer in any order.

Example1:
Input: s = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.

Example2:
Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
Output: []

Example3:
Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
Output: [6,9,12]

Constraints:
1 <= s.length <= 10^4
s consists of lower-case English letters.
1 <= words.length <= 5000
1 <= words[i].length <= 30
words[i] consists of lower-case English letters.
"""

""" 
1. HashTable/Sliding Window: O(n * m * len) time | O(m) space
n: string length
m: total number of words
len: length of word
"""

from typing import List
import unittest
class Solution(object):
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if len(s) == 0 or len(words[0]) == 0:
            return []
        dict = {}
        result = []
        wordCount = len(words)
        wordLength = len(words[0])
        for word in words:
            dict[word] = dict.get(word, 0) + 1
        for i in range((len(s) - wordCount * wordLength) + 1):
            dict2 = {}
            matched = 0
            while matched < wordCount:
                nextWordIndex = i + matched * wordLength
                word = s[nextWordIndex : nextWordIndex + wordLength]
                if word not in dict or dict[word] == dict2.get(word, 0):
                    break
                dict2[word] = dict2.get(word, 0) + 1
                matched += 1
            if matched == wordCount:
                result.append(i)
        return result


            

        




# Unit Tests
funcs = [Solution().findSubstring]


class TestFindSubstring(unittest.TestCase):
    def testFindSubstring1(self):
        for func in funcs:
            s = "barfoothefoobarman"
            words = ["foo","bar"]
            self.assertEqual(func(s=s, words=words), [0, 9])

    def testFindSubstring2(self):
        for func in funcs:
            s = "wordgoodgoodgoodbestword"
            words = ["word","good","best","word"]
            self.assertEqual(func(s=s, words=words), [])

    def testFindSubstring3(self):
        for func in funcs:
            s = "barfoofoobarthefoobarman"
            words = ["bar","foo","the"]
            self.assertEqual(func(s=s, words=words), [6,9,12])

    def testFindSubstring4(self):
        for func in funcs:
            s = "lingmindraboofooowingdingbarrwingmonkeypoundcake"
            words = ["fooo","barr","wing","ding","wing"]
            self.assertEqual(func(s=s, words=words), [13])

if __name__ == "__main__":
    unittest.main()
