"""
393. UTF-8 Validation
Given an integer array data representing the data, return whether it is a valid UTF-8 encoding.

A character in UTF8 can be from 1 to 4 bytes long, subjected to the following rules:
1. For a 1-byte character, the first bit is a 0, followed by its Unicode code.
2. For an n-bytes character, the first n bits are all one's, the n + 1 bits is 0, followed by n-1 bytes with the most significant 2 bits being 10.

This is how the UTF-8 encoding would work:
Char. number range  |        UTF-8 octet sequence
   (hexadecimal)    |              (binary)
--------------------+---------------------------------------------
0000 0000-0000 007F | 0xxxxxxx
0000 0080-0000 07FF | 110xxxxx 10xxxxxx
0000 0800-0000 FFFF | 1110xxxx 10xxxxxx 10xxxxxx
0001 0000-0010 FFFF | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx

Note: The input is an array of integers. Only the least significant 8 bits of each integer is used to store the data. This means each integer represents only 1 byte of data.

Example1:
Input: data = [197,130,1]
Output: true
Explanation: data represents the octet sequence: 11000101 10000010 00000001.
It is a valid utf-8 encoding for a 2-bytes character followed by a 1-byte character.

Example2:
Input: data = [235,140,4]
Output: false
Explanation: data represented the octet sequence: 11101011 10001100 00000100.
The first 3 bits are all one's and the 4th bit is 0 means it is a 3-bytes character.
The next byte is a continuation byte which starts with 10 and that's correct.
But the second continuation byte does not start with 10, so it is invalid.

Constraints:
1 <= data.length <= 2 * 10^4
0 <= data[i] <= 255
"""

""" 
Note:
1. Bitwise operation: O(n) time | O(1) space - where n is the length of data
2. String sliciing: O(n) time | O(1) space - where n is the length of data
"""

from typing import List
class Solution(object):
    def validUtf8(self, data: List[int]) -> bool:
        countOnes = 0
        for num in data:
            if countOnes == 0:
                if num >> 3 == 0b11110:
                    countOnes = 3
                elif num >> 4 == 0b1110:
                    countOnes = 2
                elif num >> 5 == 0b110:
                    countOnes = 1
                elif num >> 7 == 0b0:
                    countOnes = 0
                else:
                    return False
            else:
                if num >> 6 != 0b10:
                    return False
                countOnes -= 1
        return countOnes == 0

    def validUtf8_2(self, data: List[int]) -> bool:
        i = countOnes = 0
        isFirst = True
        while i < len(data):
            binary = bin(data[i])[2:].zfill(8)
            if isFirst:
                if binary[0] == "0":
                    pass
                elif binary[:3] == "110":
                    countOnes = 1
                    isFirst = False
                elif binary[:4] == "1110":
                    countOnes = 2
                    isFirst = False
                elif binary[:5] == "11110":
                    countOnes = 3
                    isFirst = False
                else:
                    return False
            else:
                if binary[:2] != "10":
                    return False
                countOnes -= 1
                if countOnes == 0:
                    isFirst = True
            i += 1
        return countOnes == 0


# Unit Tests
import unittest
funcs = [Solution().validUtf8, Solution().validUtf8_2]

class TestValidUtf8(unittest.TestCase):
    def testValidUtf8_1(self):
        for func in funcs:
            data = [197,130,1]
            self.assertEqual(func(data=data), True)

    def testValidUtf8_2(self):
        for func in funcs:
            data = [235,140,4]
            self.assertEqual(func(data=data), False)

    def testValidUtf8_3(self):
        for func in funcs:
            data = [240,162,138,147]
            self.assertEqual(func(data=data), True)


if __name__ == "__main__":
    unittest.main()
