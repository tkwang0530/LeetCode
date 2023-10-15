"""
1598. Crawler Log Folder
description: https://leetcode.com/problems/crawler-log-folder/description/
"""

"""
Note:
1. One pass: O(n) time | O(1) space - where n is the length of array logs
"""

from typing import List
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        level = 0
        for log in logs:
            if log[:2] == "./":
                continue
            elif log[:2] == "..":
                if level > 0:
                    level -= 1
            else:
                level += 1
        return level

# Unit Tests
import unittest
funcs = [Solution().minOperations]

class TestMinOperations(unittest.TestCase):
    def testMinOperations1(self):
        for minOperations in funcs:
            logs = ["d1/","d2/","../","d21/","./"]
            self.assertEqual(minOperations(logs=logs), 2)

    def testMinOperations2(self):
        for minOperations in funcs:
            logs = ["d1/","d2/","./","d3/","../","d31/"]
            self.assertEqual(minOperations(logs=logs), 3)

    def testMinOperations3(self):
        for minOperations in funcs:
            logs = ["d1/","../","../","../"]
            self.assertEqual(minOperations(logs=logs), 0)

if __name__ == "__main__":
    unittest.main()