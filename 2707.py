"""
2707. Extra Characters in a String
description: https://leetcode.com/problems/extra-characters-in-a-string/description/
"""

"""
Note:
1. dfs+memo: O(n*d*w) time | O(w*d+n) space - where n is the length of string s, d is the length of array dictionary, w is the average length of words in dictionary
2. dp: O(n*d*w) time | O(n) space - where n is the length of string s, d is the length of array dictionary, w is the average length of words in dictionary
3. dfs+memo (optimized): O(n*d*w) time |  O(w*d+n) space - where n is the length of string s, d is the length of array dictionary, w is the average length of words in dictionary
"""

from typing import List
import functools, collections
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)

        @functools.lru_cache(None)
        def dfs(i):
            if i == n:
                return 0

            # skip characters
            minLeftOver = 1 + dfs(i+1)

            for word in dictionary:
                if s[i:i+len(word)] == word:
                    minLeftOver = min(minLeftOver, dfs(i+len(word)))
            return minLeftOver

        return dfs(0)
    
class Solution2:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)

        dp = [0] * (n+1)
        for i in range(n-1, -1, -1):
            # skip characters
            minLeftOver = 1 + dp[i+1]

            for word in dictionary:
                if s[i:i+len(word)] == word:
                    minLeftOver = min(minLeftOver, dp[i+len(word)])
            
            dp[i] = minLeftOver
        return dp[0]

class Solution3:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        wordMap = collections.defaultdict(set) # <(headChar): [word]>
        for word in dictionary:
            headChar = word[0]
            wordMap[headChar].add(word)
        
        n = len(s)
        @functools.lru_cache(None)
        def dfs(i):
            if i == n:
                return 0
            minLeft = n-i
            headChar = s[i]
            for word in wordMap[headChar]:
                wLen = len(word)
                if wLen <= n-i and s[i:i+wLen] == word:
                    minLeft = min(minLeft, dfs(i+wLen)) 

            minLeft = min(minLeft, 1+dfs(i+1))
            return minLeft

        return dfs(0)

# Unit Tests
from typing import List
import unittest
funcs = [Solution().minExtraChar, Solution2().minExtraChar, Solution3().minExtraChar]


class TestMinExtraChar(unittest.TestCase):
    def testMinExtraChar1(self):
        for func in funcs:
            s = "leetscode"
            dictionary = ["leet","code","leetcode"]
            self.assertEqual(func(s=s, dictionary=dictionary), 1)


    def testMinExtraChar2(self):
        for func in funcs:
            s = "sayhelloworld"
            dictionary = ["hello","world"]
            self.assertEqual(func(s=s, dictionary=dictionary), 3)


if __name__ == "__main__":
    unittest.main()
