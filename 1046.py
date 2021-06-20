"""
1046. Last Stone Weight
We have a collection of stones, each stone has a positive integer weight.

Each turn, we choose the two heaviest stones and smash them together. Suppose the stones have weights x and y with x <= y. The result of this smash is:
- If x == y, both stones are totally destroyed
- If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y - x.

At the end, there is at most 1 stone left. Return the weight of this stone (or 0 if there are no stones left.)

Example1:
Input: [2,7,4,1,8,1]
Output: 1
Explanation: 
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of last stone.
"""

"""
Note:
1. 
"""




from typing import List
import unittest
import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)  # max heap
        while len(heap) > 1:
            result = heapq.heappop(heap) - heapq.heappop(heap)
            if result != 0:
                heapq.heappush(heap, result)
        return 0 if len(heap) == 0 else -heap[0]


# Unit Tests

funcs = [Solution().lastStoneWeight]


class TestLastStoneWeight(unittest.TestCase):

    def testLastStoneWeight1(self):
        stones = [2, 7, 4, 1, 8, 1]
        for func in funcs:
            self.assertEqual(func(stones=stones), 1)


if __name__ == "__main__":
    unittest.main()
