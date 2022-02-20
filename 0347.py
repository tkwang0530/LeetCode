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
1. minHeap + Hash Table: O(n + klogk) time | O(n+k) space
2. bucket sort: O(n) time | O(n+k) space
3. quickselect: O(n) time | O(n) space
"""

import heapq
from typing import List
import collections, random
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
        counter = collections.Counter(nums)
        maxFreq = float("-inf")
        for num, count in counter.items():
            buckets[count].append(num)
            maxFreq = max(maxFreq, count)
        flatList = []

        for i in range(maxFreq , -1, -1):
            numbers = buckets[i]
            flatList.extend(numbers)
            if len(flatList) >= k:
                break
        return flatList[:k]

    def topKFrequent3(self, nums: List[int], k: int) -> List[int]:

        counter = collections.Counter(nums)
        def quickselect(nums, k):
            if not nums:
                return []
            pivotIndex = random.randint(0, len(nums) - 1)
            nums[pivotIndex], nums[-1] = nums[-1], nums[pivotIndex]
            pivot = counter[nums[-1]]

            i = 0
            for j in range(len(nums)):
                if counter[nums[j]] < pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            
            nums[i], nums[-1] = nums[-1], nums[i]

            target = len(nums) - i
            if target == k:
                return nums[i:]
            elif target < k: # go left
                return quickselect(nums[:i], k-target) + nums[i:]
            else: # go right
                return quickselect(nums[i:], k)
        nums = list(counter.keys())
        return quickselect(nums, k)
            


# Unit Tests
import unittest
funcs = [Solution().topKFrequent, Solution().topKFrequent2, Solution().topKFrequent3]

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
