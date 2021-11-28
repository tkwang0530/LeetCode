"""
846. Hand of Straights
Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, and consists of groupSize consecutive cards.

Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, return true if she can rearrange the cards, or false otherwise.

Example1:
Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
Output: true
Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]

Example2:
Input: hand = [1,2,3,4,5], groupSize = 4
Output: false
Explanation: Alice's hand can not be rearranged into groups of 4.

Constraints:
1 <= hand.length <= 10^4
0 <= hand[i] <= 10^9
1 <= groupSize <= hand.length

Note: This question is the same as 1296
"""

""" 
Note:
1. sort the numberCount: O(nlogn + nm) time | O(n) space - where n is the length of hand and m is the groupSize
"""

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


# Unit Tests
import unittest
funcs = [Solution().isNStraightHand]

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
