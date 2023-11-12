"""
1629. Slowest Key
description: https://leetcode.com/problems/slowest-key/description/
"""

"""
Note:
1. one pass: O(n) time | O(1) space - where n is the length of array releaseTimes
"""

from typing import List
class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        candidate = keysPressed[0]
        longest = releaseTimes[0]
        for i in range(1, len(releaseTimes)):
            duration = releaseTimes[i] - releaseTimes[i-1]
            if duration > longest:
                longest = duration
                candidate = keysPressed[i]
            elif duration == longest and keysPressed[i] > candidate:
                candidate = keysPressed[i]
        return candidate

# Unit Tests
import unittest
funcs = [Solution().slowestKey]

class TestSlowestKey(unittest.TestCase):
    def testSlowestKey1(self):
        for slowestKey in funcs:
            releaseTimes = [9,29,49,50]
            keysPressed = "cbcd"
            self.assertEqual(slowestKey(releaseTimes=releaseTimes, keysPressed=keysPressed), "c")

    def testSlowestKey2(self):
        for slowestKey in funcs:
            releaseTimes = [12,23,36,46,62]
            keysPressed = "spuda"
            self.assertEqual(slowestKey(releaseTimes=releaseTimes, keysPressed=keysPressed), "a")

if __name__ == "__main__":
    unittest.main()