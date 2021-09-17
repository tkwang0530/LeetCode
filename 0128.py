"""
128. Longest Consecutive Sequence
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time

Example1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Constraints:
0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
"""

"""
Notes:
1. Hash Table: O(n) time | O(n) space
(1) build a set from the given array
(2) iterate through the input array by checking if the element has a left neighbor
    if has a left neighbor: means the element if not the start of the consecutive element sequence: continue
    if not has a left neighbor: means the element if the start of one consecutive element sequence, using a another while loop to calculate the sequence length
"""
from typing import List
class Solution(object):
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for num in nums:
            # check if its the start of a sequence
            if num - 1 not in numSet:
                length = 0
                while num + length in numSet:
                    length += 1
                longest = max(longest, length)
        return longest

# Unit Tests
import unittest
funcs = [Solution().longestConsecutive]

class TestLongestConsecutive(unittest.TestCase):
    def testLongestConsecutive1(self):
        for func in funcs:
            nums = [100,4,200,1,3,2]
            self.assertEqual(func(nums=nums), 4)

    def testLongestConsecutive2(self):
        for func in funcs:
            nums = [0,3,7,2,5,8,4,6,0,1]
            self.assertEqual(func(nums=nums), 9)

if __name__ == "__main__":
    unittest.main()