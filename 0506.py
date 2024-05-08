"""
506. Relative Ranks
description: https://leetcode.com/problems/relative-ranks/description/
"""

"""
Note:
1. Sort: O(nlogn) time | O(n) space - where n is the length of array score
"""

from typing import List
import unittest
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        pair = [(sc, i) for i, sc in enumerate(score)]
        pair.sort(reverse=True)
        output = [""] * len(score)
        for i in range(len(pair)):
            idx = pair[i][1]
            if i == 0:
                output[idx] = "Gold Medal"
            elif i == 1:
                output[idx] = "Silver Medal"
            elif i == 2:
                output[idx] = "Bronze Medal"
            else:
                output[idx] = str(i+1)

        return output

# Unit Tests
funcs = [Solution().findRelativeRanks]


class TestFindRelativeRanks(unittest.TestCase):
    def testFindRelativeRanks1(self):
        for func in funcs:
            score = [5,4,3,2,1]
            self.assertEqual(func(score=score), ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"])

    def testFindRelativeRanks2(self):
        for func in funcs:
            score = [10,3,8,9,4]
            self.assertEqual(func(score=score), ["Gold Medal", "5", "Bronze Medal", "Silver Medal", "4"])


if __name__ == "__main__":
    unittest.main()
