"""
228. Summary Ranges
You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive)

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:
- "a->b" if a != b
- "a" if a == b

Example1:
Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"

Example2:
Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"

Constraints:
0 <= nums.length <= 20
-2^31 <= nums[i] <= 2^31 - 1
All the values of nums are unique.
nums is sorted in ascending order.
"""

"""
Note:
1. Brute-Force: O(1) time | O(1) space
"""
from typing import List
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        pair = []
        output = []
        for num in nums:
            if len(pair) == 0:
                pair.append(num)
            elif len(pair) == 1 and num == pair[-1]+1:
                pair.append(num)
            elif len(pair) == 2 and num == pair[-1]+1:
                pair[-1] = num
            else:
                output.append("->".join(str(num) for num in pair))
                pair = [num]
        output.append("->".join(str(num) for num in pair))
        return output

# Unit Tests
import unittest
funcs = [Solution().summaryRanges]
class TestSummaryRanges(unittest.TestCase):
    def testSummaryRanges1(self):
        for func in funcs:
            nums = [0,1,2,4,5,7]
            self.assertEqual(func(nums=nums), ["0->2","4->5","7"])

    def testSummaryRanges2(self):
        for func in funcs:
            nums = [0,2,3,4,6,8,9]
            self.assertEqual(func(nums=nums), ["0","2->4","6","8->9"])

    def testSummaryRanges3(self):
        for func in funcs:
            nums = []
            self.assertEqual(func(nums=nums), [])

if __name__ == "__main__":
    unittest.main()
