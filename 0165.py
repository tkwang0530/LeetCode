"""
165. Compare Version Numbers
description: https://leetcode.com/problems/compare-version-numbers/description/
"""

"""
Note:
1. One pass: O(m+n) time | O(m+n) space - where m is the length of version1 and n is the length of version2
"""

from typing import List
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        revisions1 = version1.split(".")
        revisions2 = version2.split(".")
        maxLen = max(len(revisions1), len(revisions2))
        if len(revisions1) < maxLen:
            revisions1.extend(["0"]*(maxLen-len(revisions1)))
        if len(revisions2) < maxLen:
            revisions2.extend(["0"]*(maxLen-len(revisions2)))

        def compareRevision(revision1, revision2) -> int:
            if int(revision1) > int(revision2):
                return 1
            elif int(revision1) < int(revision2):
                return -1
            else:
                return 0

        for i in range(maxLen):
            result = compareRevision(revisions1[i], revisions2[i])
            if result != 0:
                return result
        return 0

# Unit Tests
import unittest
funcs = [Solution().compareVersion]

class TestCompareVersion(unittest.TestCase):
    def testCompareVersion1(self):
        for func in funcs:
            version1 = "1.01"
            version2 = "1.001"
            self.assertEqual(func(version1=version1, version2=version2), 0)

    def testCompareVersion2(self):
        for func in funcs:
            version1 = "1.0"
            version2 = "1.0.0"
            self.assertEqual(func(version1=version1, version2=version2), 0)

    def testCompareVersion3(self):
        for func in funcs:
            version1 = "0.1"
            version2 = "1.1"
            self.assertEqual(func(version1=version1, version2=version2), -1)

if __name__ == "__main__":
    unittest.main()
