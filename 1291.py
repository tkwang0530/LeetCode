"""
1291. Sequential Digits
description: https://leetcode.com/problems/sequential-digits/description/
"""

"""
Note:
1. Brute-Force: O(1) time | O(1) space
"""

from typing import List
import unittest
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        def getDigits(digitCount):
            output = []
            for i in range(1, 10-digitCount+1):
                output.append(int("".join(str(j) for j in range(i, i+digitCount))))
            return output

        allDigits = []
        for digitCount in range(2, 9+1):
            allDigits.extend(getDigits(digitCount))
        
        return [digit for digit in allDigits if low <= digit <= high]

# Unit Tests
funcs = [Solution().sequentialDigits]


class TestSequentialDigits(unittest.TestCase):
    def testSequentialDigits1(self):
        for func in funcs:
            low = 100
            high = 300
            self.assertEqual(func(low=low, high=high), [123, 234])

    def testSequentialDigits2(self):
        for func in funcs:
            low = 1000
            high = 13000
            self.assertEqual(func(low=low, high=high), [1234,2345,3456,4567,5678,6789,12345])


if __name__ == "__main__":
    unittest.main()
