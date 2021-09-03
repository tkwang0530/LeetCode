"""
6. ZigZag Conversion
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
P     A     H       N
A P L   S I   I   G
Y     I      R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:
string convert(string s, int numRows);

Example1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"

Example3:
Input: s = "A", numRows = 1
Output: "A"

Constraints:
1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), "," and ".".
1 <= numRows <= 1000
"""

"""
Notes:
1. Find the Period: O(n) time | O(n) space
where n is the length of the input string s
(1) the general period is index + 2 * (numRows - 1)
(2) additional period for rows from index 2 to len(s) - 2: index + 2 * (numRows - 1) - 2 * row
"""

class Solution(object):
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        chars = []
        for row in range(numRows):
            increment = 2 * (numRows - 1)
            for i in range(row, len(s), increment):
                chars.append(s[i])

                # the following command is for rows from index 2 to len(s) - 2 only
                if row > 0 and row < numRows - 1 and \
                    i + increment - 2 * row < len(s):
                    chars.append(s[i + increment - 2 * row])
        return "".join(chars)


# Unit Tests
import unittest
funcs = [Solution().convert]

class TestConvert(unittest.TestCase):
    def testConvert1(self):
        for func in funcs:
            s = "PAYPALISHIRING"
            numRows = 3
            self.assertEqual(func(s=s, numRows=numRows), "PAHNAPLSIIGYIR")

    def testConvert2(self):
        for func in funcs:
            s = "PAYPALISHIRING"
            numRows = 4
            self.assertEqual(func(s=s, numRows=numRows), "PINALSIGYAHRPI")

    def testConvert3(self):
        for func in funcs:
            s = "A"
            numRows = 1
            self.assertEqual(func(s=s, numRows=numRows), "A")


if __name__ == "__main__":
    unittest.main()