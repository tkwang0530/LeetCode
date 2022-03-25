"""
267. Palindrome Permutation II
Given a string s, return all the palindromic permutations (without duplicates) of it.

You may return the answer in any order. If s has no palindromic permutation, return an empty list.

Example1:
Input: s = "aabb"
Output: ["abba","baab"]

Example2:
Input: s = "abc"
Output: []

Constraints:
1 <= s.length <= 16
s consists of only lowercase English letters.
"""

"""
Notes:
1. Backtracking + HashTable ver1
2. Backtracking + HashTable ver2: O(2^n) time | O(2^n) space - where n is the length of s
could be further optimized by bitmap because len(s) <= 16
3. DFS + memo: O(n) time | O(n) space - where n is the length of output
"""

import collections
from typing import List
class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        middleStr = ""
        charCount = [0] * 26
        for char in s:
            charCount[ord(char) - ord('a')] += 1
        
        for i, count in enumerate(charCount):
            if count % 2 == 1 and len(middleStr) > 0:
                return []
            elif count % 2 == 1:
                middleStr = chr(i + ord('a'))
                charCount[i] -= 1

        totalCount = sum(charCount)
        
        # find uniqueLefts
        uniqueLefts = set()
        result = []
        currentLeft = []
        def dfs(currentLeft):
            leftStr = "".join(currentLeft)
            if len(currentLeft) * 2 == totalCount and leftStr not in uniqueLefts:
                uniqueLefts.add(leftStr)
                result.append(leftStr+middleStr+leftStr[::-1])
                return
            
            for j in range(len(charCount)):
                if charCount[j] == 0:
                    continue
                currentLeft.append(chr(j + ord('a')))
                charCount[j] -= 2
                dfs(currentLeft)
                currentLeft.pop()
                charCount[j] += 2
        
        dfs(currentLeft)
        return result

    def generatePalindromes2(self, s: str) -> List[str]:
        middleStr = ""
        charCount = [0] * 26
        choices = []
        for char in s:
            charCount[ord(char) - ord('a')] += 1
        
        for i, count in enumerate(charCount):
            if count % 2 == 1 and len(middleStr) > 0:
                return []
            elif count % 2 == 1:
                middleStr = chr(i + ord('a'))
                charCount[i] -= 1
            
            if charCount[i] % 2 == 0:
                choices.extend([chr(i + ord('a'))] * (charCount[i] // 2))

        totalCount = sum(charCount)

        visited = [False] * len(choices)
        result = []
        currentLeft = []
        def dfs(currentLeft):
            if len(currentLeft)*2 == totalCount:
                leftStr = "".join(currentLeft)
                result.append(leftStr+middleStr+leftStr[::-1])
                return
            
            for j in range(len(choices)):
                if visited[j]:
                    continue
                if j > 0 and choices[j] == choices[j-1] and not visited[j-1]:
                    continue
                visited[j] = True
                currentLeft.append(choices[j])
                dfs(currentLeft)
                currentLeft.pop()
                visited[j] = False
        
        dfs(currentLeft)
        return result

    def generatePalindromes3(self, s: str) -> List[str]:
        charCount = collections.Counter(s)
        middleStr = ""
        for char, count in charCount.items():
            if count % 2 == 1 and middleStr != "":
                return []
            elif count % 2 == 1:
                middleStr = char
                charCount[char] -= 1
        
        memo = {}
        def dfs():
            key = tuple(charCount.values())
            if sum(key) == 0:
                return [middleStr]

            if key in memo:
                return memo[key]
            
            result = []
            for char, count in charCount.items():
                if count == 0:
                    continue
                charCount[char] -= 2
                for m in dfs():
                    result.append(char + m + char)
                charCount[char] += 2
            memo[key] = result
            return memo[key]
        return dfs()
            

# Unit Tests
import unittest
funcs = [Solution().generatePalindromes, Solution().generatePalindromes2, Solution().generatePalindromes3]

class TestGeneratePalindromes(unittest.TestCase):
    def testGeneratePalindromes1(self):
        for func in funcs:
            s = "aabb"
            expect = sorted(["abba","baab"])
            actual = sorted(func(s=s))
            self.assertEqual(actual, expect)

    def testGeneratePalindromes2(self):
        for func in funcs:
            s = "abc"
            expect = sorted([])
            actual = sorted(func(s=s))
            self.assertEqual(actual, expect)

    def testGeneratePalindromes3(self):
        for func in funcs:
            s = "aaa"
            expect = sorted(["aaa"])
            actual = sorted(func(s=s))
            self.assertEqual(actual, expect)

if __name__ == "__main__":
    unittest.main()