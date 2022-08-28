"""
2384. Largest Palindromic Number
You are given a string num consisting of digits only.

Return the largest palindromic integer (in the form of a string) that can be formed using digits taken from num. It should not contain leading zeroes.

Notes:
You do not need to use all the digits of num, but you must use at least one digit.
The digits can be reordered.

Example1:
Input: num = "444947137"
Output: "7449447"
Explanation: 
Use the digits "4449477" from "444947137" to form the palindromic integer "7449447".
It can be shown that "7449447" is the largest palindromic integer that can be formed.

Example2:
Input: num = "00009"
Output: "9"
Explanation: 
It can be shown that "9" is the largest palindromic integer that can be formed.
Note that the integer returned should not contain leading zeroes.

Constraints:
1 <= nums.length <= 10^5
num consits of digits
"""

"""
Note:
1. HashTable: O(n) time | O(n) space - where n is the length of given string
"""

import collections
class Solution:
    def largestPalindromic(self, num: str) -> str:
        numStrCount = collections.Counter(num)
        chars = []
        maxOddNumStr = "#"
        for i in range(9, -1, -1):
            numStr = str(i)
            if numStrCount[numStr] >= 2:
                temp = numStrCount[numStr] // 2
                chars.extend([numStr] * temp)
                numStrCount[numStr] -= temp * 2
            
            if maxOddNumStr == "#" and numStrCount[numStr] > 0:
                maxOddNumStr = numStr
        
        if chars and chars[0] == "0":
            return maxOddNumStr if maxOddNumStr != "#" else "0"
            
        if maxOddNumStr != "#":
            chars = chars + [maxOddNumStr] + chars[::-1]
        else:
            chars = chars + chars[::-1]
        return "".join(chars)

# Unit Tests
import unittest
funcs = [Solution().largestPalindromic]
class TestLargestPalindromic(unittest.TestCase):
    def testLargestPalindromic1(self):
        for func in funcs:
            num = "444947137"
            self.assertEqual(func(num=num), "7449447")

    def testLargestPalindromic2(self):
        for func in funcs:
            num = "00009"
            self.assertEqual(func(num=num), "9")

if __name__ == "__main__":
    unittest.main()
