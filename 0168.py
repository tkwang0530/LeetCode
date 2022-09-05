"""
168. Excel Sheet Column Title
Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

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
Input: columnNumber = 1
Output: "A"

Example2:
Input: columnNumber = 28
Output: "AB"

Example3:
Input: columnNumber = 701
Output: "ZY"

Constraints:
1 <= columnNumber <= 2^31 - 1
"""

"""
Note:
1. HashTable: O(logn) time | O(1) space - where n is columnNumber
"""




import unittest
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        chars = []
        mod = 26
        numChar = {i % 26: chr(i-1+ord('A')) for i in range(1, 26+1)}
        while columnNumber > 0:
            r = columnNumber % mod
            columnNumber = columnNumber // mod
            if r == 0:
                columnNumber -= 1
            chars.append(numChar[r])
        return "".join(chars[::-1])


# Unit Tests
funcs = [Solution().convertToTitle]


class TestConvertToTitle(unittest.TestCase):
    def testConvertToTitle1(self):
        for func in funcs:
            columnNumber = 1
            self.assertEqual(func(columnNumber=columnNumber), "A")

    def testConvertToTitle2(self):
        for func in funcs:
            columnNumber = 28
            self.assertEqual(func(columnNumber=columnNumber), "AB")

    def testConvertToTitle3(self):
        for func in funcs:
            columnNumber = 701
            self.assertEqual(func(columnNumber=columnNumber), "ZY")


if __name__ == "__main__":
    unittest.main()
