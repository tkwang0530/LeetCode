"""
49. Group Anagrams
Given an array of strings, strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example2:
Input: strs = [""]
Output: [[""]]

Example3:
Input: strs = ["a"]
Output: [["a"]]

Constraints:
1 <= strs.length <= 10^4
0 <= strs[i].length <= 100
strs[i] consists of lower-case English letters.
"""

"""
Note:
1. Hash Table: O(n * mlogm) time | O(nm) space - where n is the length of strs and m is the length of the longest word
using sorted word as key {"act": ["act", "tac", "cat"]}
2. Brute Force: O(n * mlogm + m * nlogn) time | O(nm) space - where n is the length of strs and m is the length of the longest word
m * nlogn: m is for string comparison of sorting
"""




from typing import List
import unittest
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for word in strs:
            sortedWord = "".join(sorted(word))
            if sortedWord in anagrams:
                anagrams[sortedWord].append(word)
            else:
                anagrams[sortedWord] = [word]
        return list(anagrams.values())

    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        sortedWords = ["".join(sorted(w)) for w in strs]
        indices = [i for i in range(len(strs))]
        indices.sort(key=lambda x: sortedWords[x])

        result = []
        currentAnagramGroup = []
        currentAnagram = sortedWords[indices[0]]
        for index in indices:
            word = strs[index]
            sortedWord = sortedWords[index]
            if sortedWord == currentAnagram:
                currentAnagramGroup.append(word)
                continue
            result.append(currentAnagramGroup)
            currentAnagramGroup = [word]
            currentAnagram = sortedWord
        result.append(currentAnagramGroup)
        return result


# Unit Tests
funcs = [Solution().groupAnagrams, Solution().groupAnagrams2]


class TestGroupAnagrams(unittest.TestCase):
    def testGroupAnagrams1(self):
        for func in funcs:
            strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
            self.assertEqual(func(strs=strs).sort(), [
                             ["bat"], ["nat", "tan"], ["ate", "eat", "tea"]].sort())

    def testGroupAnagrams2(self):
        for func in funcs:
            strs = [""]
            self.assertEqual(func(strs=strs).sort(), [[""]].sort())

    def testGroupAnagrams3(self):
        for func in funcs:
            strs = ["a"]
            self.assertEqual(func(strs=strs).sort(), [["a"]].sort())


if __name__ == "__main__":
    unittest.main()
