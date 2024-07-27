"""
2611. Mice and Cheese
description: https://leetcode.com/problems/mice-and-cheese/description/
"""

"""
Note:
1. Sorting: O(nlogn) time | O(1) space - where n is the length of array reward1
2. minHeap: O(nlogk) time | O(k) space - where n is the length of array reward1
"""

import unittest, heapq
from typing import List
class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        n = len(reward1)
        diffs = [reward1[i]-reward2[i] for i in range(n)]

        output = sum(reward2)
        diffs.sort(reverse=True)
        for i in range(k):
            output += diffs[i]
        return output
    
class Solution2:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        n = len(reward1)
        minHeap = []
        output = sum(reward1)
        for i in range(n):
            diff = reward1[i]-reward2[i]
            if len(minHeap) < k:
                heapq.heappush(minHeap, diff)
            else:
                output -= heapq.heappushpop(minHeap, diff)

        return output


# Unit Tests
funcs = [Solution().miceAndCheese, Solution2().miceAndCheese]


class TestMiceAndCheese(unittest.TestCase):
    def testMiceAndCheese1(self):
        for func in funcs:
            reward1 = [1, 1, 3, 4]
            reward2 = [4, 4, 1, 1]
            k = 2
            self.assertEqual(func(reward1=reward1, reward2=reward2, k=k), 15)

    def testMiceAndCheese2(self):
        for func in funcs:
            reward1 = [1, 1]
            reward2 = [1, 1]
            k = 2
            self.assertEqual(func(reward1=reward1, reward2=reward2, k=k), 2)


if __name__ == "__main__":
    unittest.main()
