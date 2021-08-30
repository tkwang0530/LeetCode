"""
139. Word Break
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Example1:
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example2:
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

Example3:
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false

Constraints:
1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict.length <= 20
s and wordDict[i] consist only lowercase English letters.
All the strings of wordDict are unique.
"""

"""
Note:
1. DP (traverse by i and j): O(n^2) time | O(n+m) space
where n is the length of s
the time complexity should be O(n^3) 
but the constraint (1 <= wordDict[i].length <= 20) make it O(n^2 * 20) => O(n^2)

**dp[i] means s[:i+1] can be segmented into words in the wordDicts**

2. DP (traverse by i and word from wordDict): O(n*m) time | O(n) space
where n is the length of s
where m is the number of words in wordDict
s[left : right] = s[left : left + len(word)]
"""



from typing import List
import unittest
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1) # dp[i] means s[:i+1] can be segmented into words in the wordDicts
        dp[0] = True
        wordSet = set(wordDict)
        for left in range(len(s)):
            if not dp[left]: continue
            for right in range(left+1, len(s) + 1):
                if s[left:right] in wordSet:
                    dp[right] = True
        return dp[-1]

    def wordBreak2(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1) # dp[i] means s[:i+1] can be segmented into words in the wordDicts
        dp[0] = True
        for left in range(len(s)):
            if not dp[left]: continue
            for word in wordDict:
                right = left + len(word)
                if right <= len(s) and s[left: right] == word:
                    dp[right] = True 
        return dp[-1]


# Unit Tests
funcs = [Solution().wordBreak, Solution().wordBreak2]


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
