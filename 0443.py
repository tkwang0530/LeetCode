"""
443. String Compression
Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:
- if the group's length is 1, append the character to s.
- Otherwise, append the character followed by the group's length.

The compressed string s should not be returned separately, but instead be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.

Example1:
Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".

Example2:
Input: chars = ["a"]
Output: Return 1, and the first character of the input array should be: ["a"]
Explanation: The only group is "a", which remains uncompressed since it's a single character.

Example3:
Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".

Example4:
Input: chars = ["a","a","a","b","b","a","a"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","3","b","2","a","2"].
Explanation: The groups are "aaa", "bb", and "aa". This compresses to "a3b2a2". Note that each group is independent even if two groups have the same character.

Constraints:
1 <= chars.length <= 2000
chars[i] is a lower-case English letter, upper-case English letter, digit, or symbol.
"""

"""
Note:
1. Two Pointers: O(n) time | O(1) space
(1) Group the array into repeated chunks, keeping track of the character and the count. This forms the encoded contents.
(2) Update the original array with the encoded contents. We maintain a left pointer to know which position to update the original array with the encoded contents and increment it according to the length of the encoded contents.
"""




from typing import List
import unittest
class Solution:
    def compress(self, chars: List[str]) -> int:
        left = index = 0
        while index < len(chars):
            currentChar, count = chars[index], 0
            while index < len(chars) and chars[index] == currentChar:
                count += 1
                index += 1
            chars[left] = currentChar
            left += 1
            if count > 1:
                for char in str(count):
                    chars[left] = char
                    left += 1
        return left


# Unit Tests
funcs = [Solution().compress]


class TestCompress(unittest.TestCase):
    def testCompress1(self):
        for func in funcs:
            chars = ["a", "a", "b", "b", "c", "c", "c"]
            self.assertEqual(func(chars=chars), 6)

    def testCompress2(self):
        for func in funcs:
            chars = ["a"]
            self.assertEqual(func(chars=chars), 1)

    def testCompress3(self):
        for func in funcs:
            chars = ["a", "b", "b", "b", "b", "b",
                     "b", "b", "b", "b", "b", "b", "b"]
            self.assertEqual(func(chars=chars), 4)

    def testCompress4(self):
        for func in funcs:
            chars = ["a", "a", "a", "b", "b", "a", "a"]
            self.assertEqual(
                func(chars=chars), 6)


if __name__ == "__main__":
    unittest.main()
