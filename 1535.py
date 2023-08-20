"""
1535. Find the Winner of an Array Game
description: https://leetcode.com/problems/find-the-winner-of-an-array-game/description/
"""

"""
Note:
1. Two Pointers + HashTable: O(n) time | O(n) space - where n is the length of array arr
"""

import collections
from typing import List
class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        n = len(arr)
        winCount = collections.defaultdict(int)
        maxNum = max(arr)
        i = 0
        j = 1
        while max(i,j) < n:
            numI = arr[i]
            numJ = arr[j]
            if maxNum in (numI, numJ):
                return maxNum
            if numI > numJ:
                j = max(i,j) + 1
                winCount[numI] += 1
                if winCount[numI] == k:
                    return numI
            else:
                i = max(i,j) + 1
                winCount[numJ] += 1
                if winCount[numJ] == k:
                    return numJ
        return maxNum

# Unit Tests
import unittest
funcs = [Solution().getWinner]
class TestGetWinner(unittest.TestCase):
    def testGetWinner1(self):
        for getWinner in funcs:
            arr = [2,1,3,5,4,6,7]
            k = 2
            self.assertEqual(getWinner(arr=arr, k=k), 5)

    def testGetWinner2(self):
        for getWinner in funcs:
            arr = [3,2,1]
            k = 10
            self.assertEqual(getWinner(arr=arr, k=k), 3)

if __name__ == "__main__":
    unittest.main()
