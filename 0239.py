"""
239. Sliding Window Maximum
You are given an array of integers nums, there is a sliding window of size k which is moving from the every left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

Example1:
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position            Max
---------------                   -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Example2:
Input: nums = [1], k = 1
Output: [1]

Example3:
Input: nums = [1,-1], k = 1
Output: [1,-1]

Example4:
Input: nums = [9,11], k = 2
Output: [11]

Example5:
Input: nums = [4,-2], k = 2
Output: [4]

Constraints:
1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
1 <= k <= nums.length
"""

"""
Note:
1. monotonically decreasing queue: O(n) time | O(k) space
2. max Heap: O(n * logn) time | O(n) space
3. max Heap (improve): O(n * logn) time | O(n) space
"""

import heapq
from collections import deque
from typing import List
class Solution(object):
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        queue = deque()
        left = right = 0
        while right < len(nums):
            # pop smaller values from queue
            while queue and nums[queue[-1]] < nums[right]:
                queue.pop()
            queue.append(right)

            # remove left val from window if its index is not in sliding window anymore
            if left > queue[0]:
                queue.popleft()
            
            if right + 1 >= k:
                result.append(nums[queue[0]])
                left += 1
            right += 1
        return result

    def maxSlidingWindow2(self, nums: List[int], k: int) -> List[int]:
        result = []
        maxHeap = []
        left = right = 0
        while right < len(nums):
            while maxHeap and maxHeap[0][1] < left:
                heapq.heappop(maxHeap)
            heapq.heappush(maxHeap, (-nums[right], right))
            
            if right + 1 >= k:
                result.append(-maxHeap[0][0])
                left += 1
            right += 1
        return result

    def maxSlidingWindow3(self, nums: List[int], k: int) -> List[int]:
        result = []
        maxHeap = [(-val, i) for i, val in enumerate(nums[:k])]
        heapq.heapify(maxHeap)
        result.append(-maxHeap[0][0])

        # right start from k because we already have the result for right = k-1
        for right in range(k, len(nums)):
            left = right - k + 1
            while maxHeap and maxHeap[0][1] <  left:
                heapq.heappop(maxHeap)
            heapq.heappush(maxHeap, (-nums[right], right))
            result.append(-maxHeap[0][0])
        return result


# Unit Tests
import unittest
funcs = [Solution().maxSlidingWindow, Solution().maxSlidingWindow2, Solution().maxSlidingWindow3]

class TestMaxSlidingWindow(unittest.TestCase):
    def testMaxSlidingWindow1(self):
        for func in funcs:
            nums = [1,3,-1,-3,5,3,6,7]
            k = 3
            self.assertEqual(func(nums=nums, k=k), [3,3,5,5,6,7])

    def testMaxSlidingWindow2(self):
        for func in funcs:
            nums = [1]
            k = 1
            self.assertEqual(func(nums=nums, k=k), [1])

    def testMaxSlidingWindow3(self):
        for func in funcs:
            nums = [1,-1]
            k = 1
            self.assertEqual(func(nums=nums, k=k), [1, -1])

    def testMaxSlidingWindow4(self):
        for func in funcs:
            nums = [9, 11]
            k = 2
            self.assertEqual(func(nums=nums, k=k), [11])

    def testMaxSlidingWindow5(self):
        for func in funcs:
            nums = [4, -2]
            k = 2
            self.assertEqual(func(nums=nums, k=k), [4])


if __name__ == "__main__":
    unittest.main()
