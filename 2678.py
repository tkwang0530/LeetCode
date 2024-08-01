"""
2678. Number of Senior Citizens
description: https://leetcode.com/problems/number-of-senior-citizens/description/
"""

"""
Note:
1. One pass: O(n) time | O(1) space - where n is the length of array details
"""
from typing import List
class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return sum([int(detail[11:13]) > 60 for detail in details])

# Unit Tests
import unittest
funcs = [Solution().countSeniors]

class TestCountSeniors(unittest.TestCase):
    def testCountSeniors1(self):
        for func in funcs:
            details = ["7868190130M7522","5303914400F9211","9273338290F4010"]
            self.assertEqual(func(details=details), 2)

    def testCountSeniors2(self):
        for func in funcs:
            details = ["1313579440F2036","2921522980M5644"]
            self.assertEqual(func(details=details), 0)


if __name__ == "__main__":
    unittest.main()
