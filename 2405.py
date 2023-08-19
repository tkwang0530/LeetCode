"""
2405. Optimal Partition of String
description: https://leetcode.com/problems/optimal-partition-of-string/description/
"""

"""
Note:
1. Greedy Algorithm + hashTable: O(n) time | O(26) space - where n is the length of string s
"""

import collections
class Solution:
    def partitionString(self, s: str) -> int:
        charCount = collections.defaultdict(int)
        partitions = 1
        for char in s:
            charCount[char] += 1
            if charCount[char] > 1:
                charCount = collections.defaultdict(int)
                charCount[char] += 1
                partitions += 1
        return partitions

# Unit Tests
import unittest
funcs = [Solution().partitionString]
class TestPartitionString(unittest.TestCase):
    def testPartitionString1(self):
        for partitionString in funcs:
            s = "abacaba"
            self.assertEqual(partitionString(s=s), 4)

    def testPartitionString2(self):
        for partitionString in funcs:
            s = "ssssss"
            self.assertEqual(partitionString(s=s), 6)

if __name__ == "__main__":
    unittest.main()
