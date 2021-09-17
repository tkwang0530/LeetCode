"""
171. Excel Sheet Column Number
Given a string columnTitle that represents the column title as appear in an Excel sheet, return its corresponding column number.

For example:
A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28
...

Example1:
Input: columnTitle = "A"
Output: 1

Example2:
Input: columnTitle = "AB"
Output: 28

Example3:
Input: columnTitle = "ZY"
Output: 701

Example4:
Input: columnTitle = "FXSHRXW"
Output: 2147483647

Constraints:
1 <= columnTitle.length <= 7
columnTitle consists only of uppercase English letters.
columnTitle is in the range ["A", "FXSHRXW"].
"""

"""
Notes:
1. One pass with ord function: O(n) time | O(1) space
2. One line with functools.reduce: O(n) time | O(1) space
"""

from functools import reduce
class Solution(object):
    def titleToNumber(self, columnTitle: str) -> int:
        number = 0
        for char in columnTitle:
            number = number * 26 + (ord(char) - ord("A") + 1)
        return number

    def titleToNumber2(self, columnTitle: str) -> int:
        return reduce(lambda x, y: x * 26 + y, [ord(char) - ord("A") + 1 for char in columnTitle])

# Unit Tests
import unittest
funcs = [Solution().titleToNumber, Solution().titleToNumber2]

class TestTitleToNumber(unittest.TestCase):
    def testTitleToNumber1(self):
        for func in funcs:
            columnTitle = "A"
            self.assertEqual(func(columnTitle=columnTitle), 1)

    def testTitleToNumber2(self):
        for func in funcs:
            columnTitle = "AB"
            self.assertEqual(func(columnTitle=columnTitle), 28)

    def testTitleToNumber3(self):
        for func in funcs:
            columnTitle = "ZY"
            self.assertEqual(func(columnTitle=columnTitle), 701)

    def testTitleToNumber4(self):
        for func in funcs:
            columnTitle = "FXSHRXW"
            self.assertEqual(func(columnTitle=columnTitle), 2147483647)

if __name__ == "__main__":
    unittest.main()