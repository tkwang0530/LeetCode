"""
347. Top K Frequent Elements
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example2:
Input: nums = [1], k = 1
Output: [1]

Constraints:
1 <= nums.length <= 10^5
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
"""

"""
Note:
1. minHeap + Hash Table: O(n + klogk) time | O(n) space
"""

import heapq
from typing import List
from collections import Counter
class Solution(object):
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCount = {} # <num, count>
        for num in nums:
            numCount[num] = numCount.get(num, 0) + 1
        
        minHeap = []
        for num in numCount:
            if len(minHeap) < k:
                heapq.heappush(minHeap, (numCount[num], num))
            else:
                heapq.heappushpop(minHeap, (numCount[num], num))
        return [num for _, num in minHeap]

    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums) + 1)]
        counter = Counter(nums)
        for num, count in counter.items():
            buckets[count].append(num)
        flatList = []
        for numbers in buckets: # or flatList = list(itertools.chain(*buckets))
            flatList += numbers
        return flatList[::-1][:k]


# Unit Tests
import unittest
funcs = [Solution().topKFrequent, Solution().topKFrequent2]

class TestTopKFrequent(unittest.TestCase):
    def testTopKFrequent1(self):
        for func in funcs:
            nums = [1,1,1,2,2,3]
            k = 2
            self.assertEqual(sorted(func(nums=nums, k=k)), sorted([1, 2]))

    def testTopKFrequent2(self):
        for func in funcs:
            nums = [1]
            k = 1
            self.assertEqual(sorted(func(nums=nums, k=k)), sorted([1]))


if __name__ == "__main__":
    unittest.main()
