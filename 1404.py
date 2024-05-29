"""
1404. Number of Steps to Reduce a Number in Binary Representation to One
description: https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/description/
"""

"""
Note:
1. Simulation: O(n) time | O(n) space - where n is the length of string s 
"""


import unittest
class Solution:
    def numSteps(self, s: str) -> int:
        bits = [0] * (len(s)+1)
        for i in range(1, len(s)+1):
            if s[i-1] == "1":
                bits[i] = 1

        steps = 0
        idx = len(s)
        while idx > 1:
            if bits[idx] == 1:
                bits[idx-1] += 1
                bits[idx] = 0
            else:
                idx -= 1
                bits[idx-1] += bits[idx] // 2
                bits[idx] %= 2
            steps += 1

        return steps if bits[:2] == [0, 1] else steps+1

# Unit Tests
funcs = [Solution().numSteps]


class TestNumSteps(unittest.TestCase):
    def testNumSteps1(self):
        for func in funcs:
            self.assertEqual(func(s="1101"), 6)

    def testNumSteps2(self):
        for func in funcs:
            self.assertEqual(func(s="10"), 1)

    def testNumSteps3(self):
        for func in funcs:
            self.assertEqual(func(s="1"), 0)


if __name__ == "__main__":
    unittest.main()
