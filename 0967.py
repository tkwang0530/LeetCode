"""
967. Numbers With Same Consecutive Differences
Return all non-negative integers of length n such that the absolute difference between every two consecutive digits is k.

Note that every number in the answer must not have leading zeros. For example, 01 has one leading zero and is invalid.

You may return the answer in any order.

Example1:
Input: n = 3, k = 7
Output: [181,292,707,818,929]
Explanation: Note that 070 is not a valid number, because it has leading zeroes.

Example2:
Input: n = 2, k = 1
Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]

Constraints:
2 <= n <= 9
0 <= k <= 9
"""

"""
Note:
1. Iterative BFS: O(2^n) time | O(2^n) space
"""




import unittest
from typing import List
class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        currentNums = {i for i in range(1, 9+1)}
        for _ in range(n-1):
            nextNums = set()
            for num in currentNums:
                y = num % 10
                if y+k < 10:
                    nextNums.add(num*10 + y + k)
                if k > 0 and y-k >= 0:
                    nextNums.add(num*10 + y - k)
            currentNums = nextNums
        return list(currentNums)


# Unit Tests
funcs = [Solution().numsSameConsecDiff]


class TestNumsSameConsecDiff(unittest.TestCase):
    def testNumsSameConsecDiff1(self):
        for func in funcs:
            n = 3
            k = 7
            self.assertEqual(sorted(func(n=n, k=k)),
                             sorted([181, 292, 707, 818, 929]))

    def testNumsSameConsecDiff2(self):
        for func in funcs:
            n = 2
            k = 1
            self.assertEqual(sorted(func(n=n, k=k)), sorted(
                [10, 12, 21, 23, 32, 34, 43, 45, 54, 56, 65, 67, 76, 78, 87, 89, 98]))

    def testNumsSameConsecDiff3(self):
        for func in funcs:
            n = 4
            k = 1
            self.assertEqual(sorted(func(n=n, k=k)), sorted([1010, 1012, 1210, 1212, 1232, 1234, 2101, 2121, 2123, 2321, 2323, 2343, 2345, 3210, 3212, 3232, 3234, 3432, 3434, 3454, 3456, 4321, 4323, 4343, 4345, 4543, 4545,
                             4565, 4567, 5432, 5434, 5454, 5456, 5654, 5656, 5676, 5678, 6543, 6545, 6565, 6567, 6765, 6767, 6787, 6789, 7654, 7656, 7676, 7678, 7876, 7878, 7898, 8765, 8767, 8787, 8789, 8987, 8989, 9876, 9878, 9898]))


if __name__ == "__main__":
    unittest.main()
