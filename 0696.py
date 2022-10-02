"""
696. Count Binary Substrings
Given a binary string s, return the number of non-empty substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur.

Example1:
Input: s = "00110011"
Output: 6
Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".
Notice that some of these substrings repeat and are counted the number of times they occur.
Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.

Example2:
Input: s = "10101"
Output: 4
Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.

Constraints:
1 <= s.length <= 10^5
s[i] is either '0' or '1'.
"""

"""
Note:
1. HashTable: O(n) time | O(1) space - where n is the length of string s
"""




import unittest
import collections
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        charCount = collections.defaultdict(int)
        prev = ""
        output = 0
        for char in s:
            if char != prev and charCount[char] > 0:
                charCount[char] = 1
            else:
                charCount[char] += 1

            opposite = "0" if char == "1" else "1"
            if charCount[opposite] >= charCount[char] and charCount[opposite] > 0:
                output += 1
            prev = char
        return output


# Unit Tests
funcs = [Solution().countBinarySubstrings]


class TestCountBinarySubstrings(unittest.TestCase):
    def testCountBinarySubstrings1(self):
        for func in funcs:
            s = "00110011"
            self.assertEqual(func(s=s), 6)

    def testCountBinarySubstrings2(self):
        for func in funcs:
            s = "10101"
            self.assertEqual(func(s=s), 4)


if __name__ == "__main__":
    unittest.main()
