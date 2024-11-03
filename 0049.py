"""
49. Group Anagrams
description: https://leetcode.com/problems/group-anagrams/description/
"""

"""
Note:
1. Hash Table: O(n * mlogm) time | O(nm) space - where n is the length of strs and m is the length of the longest word
using sorted word as key {"act": ["act", "tac", "cat"]}
2. Brute Force: O(n * mlogm + m * nlogn) time | O(nm) space - where n is the length of strs and m is the length of the longest word
m * nlogn: m is for string comparison of sorting
"""




from typing import List
import unittest, collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        patternWords = collections.defaultdict(list)
        for word in strs:
            pattern = "".join(sorted(word))
            patternWords[pattern].append(word)

        return list(patternWords.values())

class Solution2:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
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
funcs = [Solution().groupAnagrams, Solution2().groupAnagrams]


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
