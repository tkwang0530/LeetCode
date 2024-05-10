
"""
948. Bag of Tokens
description: https://leetcode.com/problems/bag-of-tokens/description/
"""

"""
Note:
1. Greedy + Two Pointers: O(nlogn) time | O(1) space
"""

from typing import List
class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        left, right = 0, len(tokens)-1
        maxScore = 0
        runningPower = power
        runningScore = 0
        while left <= right:
            canFaceUp = runningPower >= tokens[left]
            if canFaceUp:
                runningScore += 1
                runningPower -= tokens[left]
                maxScore = max(maxScore, runningScore)
                left += 1
            elif runningScore >= 1:
                runningScore -= 1
                runningPower += tokens[right]
                right -= 1
            else:
                break
        return maxScore
# Unit Tests
import unittest
funcs = [Solution().bagOfTokensScore]

class TestBagOfTokensScore(unittest.TestCase):
    def testBagOfTokensScore1(self):
        for bagOfTokensScore in funcs:
            tokens = [100]
            power = 50
            self.assertEqual(bagOfTokensScore(tokens=tokens, power=power), 0)

    def testBagOfTokensScore2(self):
        for bagOfTokensScore in funcs:
            tokens = [100, 200]
            power = 150
            self.assertEqual(bagOfTokensScore(tokens=tokens, power=power), 1)

    def testBagOfTokensScore3(self):
        for bagOfTokensScore in funcs:
            tokens = [100, 200, 300, 400]
            power = 200
            self.assertEqual(bagOfTokensScore(tokens=tokens, power=power), 2)


if __name__ == "__main__":
    unittest.main()