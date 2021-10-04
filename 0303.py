"""
303. Range Sum Query - Immutable
Given an integer array nums, handle multiple queries of the following type:
1. Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.

Implement the NumArray class:
- NumArray(int[] nums) Initializes the object with the integer array nums.
- int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left+1] + ... + nums[right]).

Example1:
Input
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
Output
[null, 1, -1, -3]

Explanation
NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3

Constraints:
1 <= nums.length <= 10^4
-10^5 <= nums[i] <= 10^5
0 <= left <= right < nums.length
At most 10^4 calls will be made to sumRange.
"""

""" 
1. Prefix Sum
O(n) time | O(n) space for __init__
O(1) time | O(1) space for sumRange
"""

from typing import List
class NumArray:

    def __init__(self, nums: List[int]):
        self.prefixSums = [0] + nums
        for i in range(1, len(self.prefixSums)):
            self.prefixSums[i] += self.prefixSums[i-1]

    def sumRange(self, left: int, right: int) -> int:
        return self.prefixSums[right+1] - self.prefixSums[left]

# Unit Tests
import unittest
class TestNumArray(unittest.TestCase):
    def testNumArray1(self):
        numArray = NumArray([-2, 0, 3, -5, 2, -1])
        self.assertEqual(numArray.sumRange(0, 2), 1)
        self.assertEqual(numArray.sumRange(2, 5), -1)
        self.assertEqual(numArray.sumRange(0, 5), -3)


if __name__ == "__main__":
    unittest.main()
