"""
670. Maximum Swap
You are given an integer num. You can swap two digits at most once to get the maximum valued number.

Return the maximum valued number you can get.

Example1:
Input: num = 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.

Example2:
Input: num = 9973
Output: 9973
Explanation: No swap.

Constraints:
0 <= num <= 10^8
"""

"""
Note:
1. Greedy Algorithm: O(n) time | O(1) space
(1) store values' indices into a dictionary<number,index>
(2) traverse the numberStr list (transfer from input num)
- if the currNum in dict and its index is larger than the current index: swap and return new number
"""

import unittest
class Solution:
    def maximumSwap(self, num: int) -> int:
        indices = {}
        numList = list(str(num))
        for i, numStr in enumerate(numList):
            indices[numStr] = i
        for i, numStr in enumerate(numList):
            for digit in range(9, int(numStr), -1):
                digitStr = str(digit)
                if indices.get(digitStr, -1) > i:
                    numList[i], numList[indices[digitStr]] = numList[indices[digitStr]], numList[i]
                    return int("".join(numList))
        return num


# Unit Tests
funcs = [Solution().maximumSwap]


class TestMaximumSwap(unittest.TestCase):
    def testMaximumSwap1(self):
        for func in funcs:
            num = 2736
            self.assertEqual(func(num=num), 7236)

    def testMaximumSwap2(self):
        for func in funcs:
            num = 9973
            self.assertEqual(func(num=num), 9973)

if __name__ == "__main__":
    unittest.main()
