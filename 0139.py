"""
139. Word Break
description: https://leetcode.com/problems/word-break/description/
"""

"""
Note:
1. DP (traverse by i and j): O(n^3+m) time | O(n+m) space
where n is the length of s, and m is the number of words

**# dp[i] means s[:i] (exclusive) can be segmented into words in the wordDicts, so we can start trying to match from i if dp[i] is true**

2. DP (traverse by i and word from wordDict): O(n*m^2) time | O(n) space
where n is the length of s
where m is the number of words in wordDict
s[left : right] = s[left : left + len(word)]

3. DP + KMP: O(w*(n+m+m) + n^2) time | O(n^2) - where n is the length of string s, w is the number of words, m is the average length of word

4. dp + hashTable: O(wls * n * wl) time | O(n) space
where wls is the number of distinct word lengths in wordDict
where wl is the average length of word
where n is the length of s
"""



import collections
from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1) # dp[i] means s[:i] (exclusive) can be segmented into words in the wordDicts, so we can start trying to match from i if dp[i] is true
        dp[0] = True
        wordSet = set(wordDict)
        for left in range(len(s)):
            if not dp[left]: continue
            for right in range(left+1, len(s) + 1):
                if s[left:right] in wordSet:
                    dp[right] = True
        return dp[-1]

class Solution2:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1) # dp[i] means s[:i] (exclusive) can be segmented into words in the wordDicts, so we can start trying to match from i if dp[i] is true
        dp[0] = True
        for left in range(len(s)):
            if not dp[left]: continue
            for word in wordDict:
                right = left + len(word)
                if right <= len(s) and s[left: right] == word:
                    dp[right] = True 
        return dp[-1]

class Solution3:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def build(p: str) -> List[int]:
            m = len(p)
            next = [0, 0]
            j = 0
            for i in range(1, m):
                while j > 0 and p[i] != p[j]:
                    j = next[j]
                if p[i] == p[j]:
                    j += 1
                next.append(j)
            return next
        
        def match(s: str, p: str) -> List[int]:
            n, m = len(s), len(p)
            next = build(p)
            ans = []
            j = 0
            for i in range(n):
                while j > 0 and s[i] != p[j]:
                    j = next[j]
                if s[i] == p[j]:
                    j += 1
                if j == m:
                    ans.append(i-m+1)
                    j = next[j]
            return ans

        startMatches = collections.defaultdict(set)
        for word in wordDict:
            matches = match(s, word)
            for m in matches:
                startMatches[m].add(m+len(word))
        
        dp = [False] * (len(s)+1) # dp[i] means s[:i] (exclusive) can be segmented into words in the wordDicts, so we can start trying to match from i if dp[i] is true
        dp[0] = True
        for left in range(len(s)):
            if not dp[left]: continue
            for m in startMatches[left]:
                dp[m] = True
        return dp[-1]

class Solution4:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = collections.defaultdict(bool)
        wordLengthWords = collections.defaultdict(set) # <length, set{word1, word2}>
        for word in wordDict:
            wordLength = len(word)
            wordLengthWords[wordLength].add(word)

        dp[0] = True
        n = len(s)
        for i in range(n):
            if not dp[i]:
                continue
            for wordLength, words in wordLengthWords.items():
                if i+wordLength <= len(s) and s[i:i+wordLength] in words:
                    dp[i+wordLength] = True
            
        return dp[len(s)]

# Unit Tests
import unittest
funcs = [Solution().wordBreak, Solution2().wordBreak, Solution3().wordBreak, Solution4().wordBreak]

class TestWordBreak(unittest.TestCase):
    def testWordBreak1(self):
        for func in funcs:
            s = "leetcode"
            wordDict = ["leet","code"]
            self.assertEqual(func(s=s, wordDict=wordDict), True)

    def testWordBreak2(self):
        for func in funcs:
            s = "applepenapple"
            wordDict = ["apple","pen"]
            self.assertEqual(func(s=s, wordDict=wordDict), True)

    def testWordBreak3(self):
        for func in funcs:
            s = "catsandog"
            wordDict = ["cats","dog","sand","and","cat"]
            self.assertEqual(func(s=s, wordDict=wordDict), False)


if __name__ == "__main__":
    unittest.main()
