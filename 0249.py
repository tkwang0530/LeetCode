"""
249. Group Shifted Strings
We can shift a string by shifting each of its letters to its successive letter.
- For example, "abc" can be shifted to be "bcd"
We can keep shifting the string to form a sequence.
- For example, we can keep shifting "abc" to form the sequence: "abc" -> "bcd" -> ... -> "xyz"

Given an array of strings strings, group all strings[i] that belong to the same shifting sequence. You may return the answer in any order.

Example1:
Input: strings = ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]
Output: [["acef"], ["a", "z"], ["abc", "bcd", "xyz"], ["az", "ba"]]

Example2:
Input: strings = ["a"]
Output: [["a"]]

Constraints:
1 <= strings.length <= 200
1 <= strings[i].length <= 50
strings[i] consists of lowercase English letters.
"""

"""
Note:
1. Hash Table: O(n^2) time | O(n) space
where n is the sum of the characters in the given strings
{(0, 1, 2): ["abc", "bcd"], (0, 2, 3,5): ["acef"]}
key contains all the distances between the char[i] and the char[0]
use % 26 so that  the range of differece will be [0, 25]

2. Hash Table + Tuple Comprehension: O(n) time | O(n) space
"""



from collections import defaultdict
from typing import List
import unittest
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for string in strings:
            key = ()
            for char in string:
                key += (ord(char) - ord(string[0])) % 26,
            result[key].append(string)
        return result.values()

    def groupStrings2(self, strings: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for string in strings:
            key = ((ord(char) - ord(string[0])) % 26 for char in string)
            result[key].append(string)
        return result.values()



# Unit Tests
funcs = [Solution().groupStrings, Solution().groupStrings2]


class TestGroupStrings(unittest.TestCase):
    def testGroupStrings1(self):
        for func in funcs:
            strings = ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]
            self.assertEqual(list(func(strings=strings)).sort(), [["acef"], ["a", "z"], ["abc", "bcd", "xyz"], ["az", "ba"]].sort())

    def testGroupStrings2(self):
        for func in funcs:
            strings = ["a"]
            self.assertEqual(list(func(strings=strings)).sort(), [["a"]].sort())


if __name__ == "__main__":
    unittest.main()
