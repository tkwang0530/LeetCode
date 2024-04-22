"""
752. Open the Lock
description: https://leetcode.com/problems/open-the-lock/description/
"""

"""
Note:
1. BFS (layer order traversal): O(8 * 10^4) time | O(10^4) space
"""

from typing import List
import unittest

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadendSet = set(deadends)
        if "0000" in deadendSet or target in deadendSet:
            return -1
        visited = set(["0000"])
        currentLocks = set(["0000"])
        turns = 0
        while currentLocks:
            nextLocks = set()
            for lock in currentLocks:
                if lock == target:
                    return turns
                
                for i in range(4):
                    digit = int(lock[i])
                    for direction in [-1, 1]:
                        newDigit = (digit+direction) % 10
                        newLock = lock[:i]+str(newDigit)+lock[i+1:]
                        if newLock in deadendSet or newLock in visited:
                            continue
                        nextLocks.add(newLock)
                        visited.add(newLock)

            currentLocks = nextLocks
            turns += 1
        return -1

# Unit Tests
funcs = [Solution().openLock]


class TestOpenLock(unittest.TestCase):
    def testOpenLock1(self):
        for func in funcs:
            deadends = ["0201", "0101", "0102", "1212", "2002"]
            target = "0202"
            self.assertEqual(func(deadends=deadends, target=target), 6)

    def testOpenLock2(self):
        for func in funcs:
            deadends = ["8888"]
            target = "0009"
            self.assertEqual(func(deadends=deadends, target=target), 1)

    def testOpenLock3(self):
        for func in funcs:
            deadends = ["8887", "8889", "8878",
                        "8898", "8788", "8988", "7888", "9888"]
            target = "8888"
            self.assertEqual(func(deadends=deadends, target=target), -1)


if __name__ == "__main__":
    unittest.main()
