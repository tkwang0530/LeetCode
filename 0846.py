"""
846. Hand of Straights
description: https://leetcode.com/problems/hand-of-straights/description/
"""

""" 
Note:
1. sort the numberCount: O(nlogn + nm) time | O(n) space - where n is the length of hand and m is the groupSize
2. SortedList: O(nlogn) time | O(n) space - where n is the length of hand
"""

from sortedcontainers import SortedList
import collections
from typing import List
class Solution(object):
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        numberCount = collections.Counter(hand)
        if len(numberCount) < groupSize:
            return False
        
        sortedNumberCount = [[num, count] for num, count in sorted(numberCount.items())]
        for i, numberCount in enumerate(sortedNumberCount):
            number, times = numberCount
            if times == 0: continue
            for j in range(groupSize - 1):
                idx = i+j+1
                if idx >= len(sortedNumberCount): return False
                diff = sortedNumberCount[idx][0] - number
                if diff != j+1:
                    return False
                sortedNumberCount[idx][1] -= times
                if sortedNumberCount[idx][1] < 0:
                    return False
        return True


class Solution2:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize > 0:
            return False

        bst = SortedList()
        for h in hand:
            bst.add(h)

        while bst:
            first = bst[0]
            for i in range(groupSize):
                if first+i not in bst:
                    return False
                bst.remove(first+i)
        return True
# Unit Tests
import unittest
funcs = [Solution().isNStraightHand, Solution2().isNStraightHand]

class TestIsNStraightHand(unittest.TestCase):
    def testIsNStraightHand1(self):
        for func in funcs:
            hand = [1,2,3,6,2,3,4,7,8]
            groupSize = 3
            self.assertEqual(func(hand=hand, groupSize=groupSize), True)

    def testIsNStraightHand2(self):
        for func in funcs:
            hand = [1,2,3,4,5]
            groupSize = 4
            self.assertEqual(func(hand=hand, groupSize=groupSize), False)

if __name__ == "__main__":
    unittest.main()
