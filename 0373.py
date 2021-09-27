"""
373. Find K Pairs with Smallest Sums
You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

Define a pair (u, v) which consists of one element from the first array and one element from the second array.

Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.

Example1:
Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]]
Explanation: The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]

Example2:
Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output: [[1,1],[1,1]]
Explanation: The first 2 pairs are returned from the sequence: [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]

Example3:
Input: nums1 = [1,2], nums2 = [3], k = 3
Output: [[1,3],[2,3]]
Explanation: All possible pairs are returned from the sequence: [1,3],[2,3]

Constraints:
1 <= nums1.length, nums2.length <= 10^5
-10^9 <= nums1[i], nums2[i] <= 10^9
nums1 and nums2 both are sorted in ascending order.
1 <= k <= 1000
"""

"""
Note:
1. min Heap + Hash Table: O(klogk) time | O(k) space
(1) create a minHeap, and push (nums1[0] + nums2[0], 0, 0) into the heap
(2) pop the root element and push two elements (nums1[1] + nums2[0], 1, 0) and (nums1[0] + nums2[1], 0, 1)
(3) use a hash set to store the position we have already visited {(0, 0), (1, 0), (0, 1)}
"""

import heapq
from typing import List
class Solution(object):
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        result = []
        if not nums1 or not nums2 or not k:
            return result
        minHeap = []
        visited = set()

        heapq.heappush(minHeap, (nums1[0] + nums2[0], 0, 0))
        visited.add((0, 0))
        while len(result) < k and len(minHeap) > 0:
            _, i, j = heapq.heappop(minHeap)
            result.append([nums1[i], nums2[j]])

            if i+1 < len(nums1) and (i+1, j) not in visited:
                heapq.heappush(minHeap, (nums1[i+1] + nums2[j], i+1, j))
                visited.add((i+1, j))
            
            if j+1 < len(nums2) and (i, j+1) not in visited:
                heapq.heappush(minHeap, (nums1[i] + nums2[j+1], i, j+1))
                visited.add((i, j+1))
        return result


# Unit Tests
import unittest
funcs = [Solution().kSmallestPairs]

class TestKSmallestPairs(unittest.TestCase):
    def testKSmallestPairs1(self):
        for func in funcs:
            nums1 = [1,7,11]
            nums2 = [2,4,6]
            k = 3
            self.assertEqual(func(nums1=nums1, nums2=nums2, k=k), [[1,2],[1,4],[1,6]])

    def testKSmallestPairs2(self):
        for func in funcs:
            nums1 = [1,1,2]
            nums2 = [1,2,3]
            k = 2
            self.assertEqual(func(nums1=nums1, nums2=nums2, k=k), [[1,1],[1,1]])

    def testKSmallestPairs3(self):
        for func in funcs:
            nums1 = [1,2]
            nums2 = [3]
            k = 3
            self.assertEqual(func(nums1=nums1, nums2=nums2, k=k), [[1,3],[2,3]])

if __name__ == "__main__":
    unittest.main()
