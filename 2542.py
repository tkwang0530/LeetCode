"""
2542. Maximum Subsequence Score
description: https://leetcode.com/problems/maximum-subsequence-score/description/
"""

"""
Note:
1. minHeap + Sort: O(nlogn+nlogk) time | O(k) space - where n is the length of nums
ref: https://www.youtube.com/watch?v=ax1DKi5lJwk
"""

from typing import List
import unittest, heapq
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = [(n1, n2) for n1, n2 in zip(nums1, nums2)]
        pairs.sort(key=lambda p: p[1], reverse=True)

        minHeap = []
        n1Sum = 0
        maxScore = 0

        for n1, n2 in pairs:
            n1Sum += n1
            if len(minHeap) < k:
                heapq.heappush(minHeap, n1)
            else:
                n1Sum -= heapq.heappushpop(minHeap, n1)
            
            if len(minHeap) == k:
                maxScore = max(maxScore, n1Sum * n2)
            
        return maxScore

# Unit Tests
funcs = [Solution().maxScore]


class TestMaxScore(unittest.TestCase):
    def testMaxScore1(self):
        for func in funcs:
            nums1 = [1,3,3,2]
            nums2 = [2,1,3,4]
            k = 3
            self.assertEqual(func(nums1=nums1, nums2=nums2, k=k), 12)

    def testMaxScore2(self):
        for func in funcs:
            nums1 = [4,2,3,1,1]
            nums2 = [7,5,10,9,6]
            k = 1
            self.assertEqual(func(nums1=nums1, nums2=nums2, k=k), 30)

if __name__ == "__main__":
    unittest.main()
