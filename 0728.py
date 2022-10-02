"""
728. Self Dividing Numbers
A self-dividing number is a number that is divisible by every digit it contains
- For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

A self-dividing number is not allowed to contain the digit zero.
Given two integer left and right, return a list of all the self-dividing numbers in the range [lleft, right]

Example1:
Input: left = 1, right = 22
Output: [1,2,3,4,5,6,7,8,9,11,12,15,22]

Example2:
Input: left = 47, right = 85
Output: [48,55,66,77]

Constraints:
1 <= left <= right <= 10^4
"""

"""
Note:
1. Brute-Force: O(n) time | O(n) space - where n is right-left+1
"""




import unittest
from typing import List
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        output = []
        for num in range(left, right+1):
            numStr = str(num)
            isValid = True
            for char in numStr:
                digit = int(char)
                if digit == 0:
                    isValid = False
                    break
                if num % digit != 0:
                    isValid = False
            if isValid:
                output.append(num)
        return output


# Unit Tests
funcs = [Solution().selfDividingNumbers]


class TestSelfDividingNumbers(unittest.TestCase):
    def testSelfDividingNumbers1(self):
        for func in funcs:
            left = 1
            right = 22
            self.assertEqual(func(left=left, right=right), [
                             1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22])

    def testSelfDividingNumbers2(self):
        for func in funcs:
            left = 47
            right = 85
            self.assertEqual(func(left=left, right=right), [48, 55, 66, 77])


if __name__ == "__main__":
    unittest.main()
