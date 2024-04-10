"""
950. Reveal Cards In Increasing Order
description: https://leetcode.com/problems/reveal-cards-in-increasing-order/description/
"""

"""
Note:
1. Sort + queue: O(nlogn) time | O(n) space - where n is the length of deck
ref: https://www.youtube.com/watch?v=i2QrUdwWlak
"""

import collections
from typing import List

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        output = [0] * len(deck)
        queue = collections.deque(range(len(deck)))
        for n in deck:
            i = queue.popleft()
            output[i] = n

            if queue:
                queue.append(queue.popleft())
        return output

# Unit Tests
import unittest
funcs = [Solution().deckRevealedIncreasing]


class TestDeckRevealedIncreasing(unittest.TestCase):
    def testDeckRevealedIncreasing1(self):
        for func in funcs:
            deck = [17,13,11,2,3,5,7]
            self.assertEqual(func(deck=deck), [2,13,3,11,5,17,7])

    def testDeckRevealedIncreasing2(self):
        for func in funcs:
            deck = [1,1000]
            self.assertEqual(func(deck=deck), [1,1000])

if __name__ == "__main__":
    unittest.main()
