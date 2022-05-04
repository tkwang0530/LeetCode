"""
893. Groups of Special-Equivalent Strings
You are given an strings of the same length words.

In one move, you can swap any two even indexed characters or any two odd indexed characters of a string words[i].

Two strings words[i] and words[j] are special-equivalent if after any number of moves, words[i] == word[j].
- For example, words[i] = "zzxy" and words[j] = "xyzz" are special-equivalent because we may make the moves "zzxy" -> "xzzy" -> "xyzz"

A group of special-equivalent strings from words is a non-empty subset of words such that of words such that:
- Every pair of strings in the group are special equivalent
- The group is the largest size possible (i.e. there is not a string words[i] not in the group such that words[i] is a special-equivalent to every string in the group).

Return the number of groups of special-equivalent strings from words.

Example1:
Input: words = ["abcd","cdab","cbad","xyzz","zzxy","zzyx"]
Output: 3
Explanation: 
One group is ["abcd", "cdab", "cbad"], since they are all pairwise special equivalent, and none of the other strings is all pairwise special equivalent to these.
The other two groups are ["xyzz", "zzxy"] and ["zzyx"].
Note that in particular, "zzxy" is not special equivalent to "zzyx".

Example2:
Input: words = ["abc","acb","bac","bca","cab","cba"]
Output: 3

Constraints:
1 <= words.length <= 1000
1 <= words[i].length <= 20
words[i] consist of lowercase English letters.
All the strings are of the same length.
"""

"""
Note:
1. HashTable: O(wlogw*n) time | O(n) space - where w is the max length of all words and n is the len(words)
"""

import collections
from typing import List
class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        def getKey(word):
            charCountEven = collections.Counter(word[0:len(word):2])
            charCountOdd = collections.Counter(word[1:len(word):2])
            temp1 = []
            temp2 = []
            for char, count in sorted(charCountEven.items()):
                temp1.append(char)
                temp1.append(str(count))

            for char, count in sorted(charCountOdd.items()):
                temp2.append(char)
                temp2.append(str(count))
            return "".join(temp1), "".join(temp2)

        group = set()
        for word in words:
            group.add(getKey(word))
        return len(group)

        

# Unit Tests
import unittest
funcs = [Solution().numSpecialEquivGroups]

class TestNumSpecialEquivGroups(unittest.TestCase):
    def testNumSpecialEquivGroups1(self):
        for func in funcs:
            words = ["abcd","cdab","cbad","xyzz","zzxy","zzyx"]
            self.assertEqual(func(words=words), 3)

    def testNumSpecialEquivGroups2(self):
        for func in funcs:
            words = ["abc","acb","bac","bca","cab","cba"]
            self.assertEqual(func(words=words), 3)

if __name__ == "__main__":
    unittest.main()