"""
1985. Find the Kth Largest Integer in the Array
You are given an array of strings nums and an integer k. Each string in nums represents an integer without leading zeros.

Return the string that represents the kth largest integer in nums.

Note: Duplicate numbers should be counted distinctly. For example, if nums is
["1", "2", "2"], "2" is the first largest integer, "2" is the second-largest integer, and "1" is the third-largest integer.

Example1:
Input: nums = ["3","6","7","10"], k = 4
Output: "3"
Explanation:
The numbers in nums sorted in non-decreasing order are ["3","6","7","10"].
The 4th largest integer in nums is "3".

Example2:
Input: nums = ["2","21","12","1"], k = 3
Output: "2"
Explanation:
The numbers in nums sorted in non-decreasing order are ["1","2","12","21"].
The 3rd largest integer in nums is "2".

Example3:
Input: nums = ["0","0"], k = 2
Output: "0"
Explanation:
The numbers in nums sorted in non-decreasing order are ["0","0"].
The 2nd largest integer in nums is "0".

Constraints:
1 <= k <= nums.length <= 10^4
1 <= nums[i].length <= 100
nums[i] consists of only digits.
nums[i] will not have any leading zeros.
"""

"""
Note:
1. minHeap (will overflow if numStr is too long): O(nlogk) time | O(k) space
but it works in python

2. minHeap with tuple (len(numStr), numStr): O(nlogk) time | O(k) space
"""

import heapq
from typing import List
class Solution(object):
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        minHeap = []
        for numStr in nums:
            num = int(numStr)
            if len(minHeap) < k:
                heapq.heappush(minHeap, num)
            else:
                heapq.heappushpop(minHeap, num)
        return str(minHeap[0])

    def kthLargestNumber2(self, nums: List[str], k: int) -> str:
        minHeap = []
        for numStr in nums:
            if len(minHeap) < k:
                heapq.heappush(minHeap, (len(numStr), numStr))
            else:
                heapq.heappushpop(minHeap, (len(numStr), numStr))
        return minHeap[0][1]


# Unit Tests
import unittest
funcs = [Solution().kthLargestNumber, Solution().kthLargestNumber2]

class TestKthLargestNumber(unittest.TestCase):
    def testKthLargestNumber1(self):
        for func in funcs:
            nums = ["3","6","7","10"]
            k = 4
            self.assertEqual(func(nums=nums, k=k), "3")

    def testKthLargestNumber2(self):
        for func in funcs:
            nums = ["2","21","12","1"]
            k = 3
            self.assertEqual(func(nums=nums, k=k), "2")

    def testKthLargestNumber3(self):
        for func in funcs:
            nums = ["0","0"]
            k = 2
            self.assertEqual(func(nums=nums, k=k), "0")


if __name__ == "__main__":
    unittest.main()
