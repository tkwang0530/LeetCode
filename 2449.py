"""
2449. Minimum Number of Operations to Make Arrays Similar
You are given two positive integer arrays nums and target, of the same length.

In one operation, you can choose any two distinct indices i and j where 0 <= i, j < nums.length and:
- set nums[i] = nums[i] + 2 and 
- set nums[j] = nums[j] - 2

Two arrays are considered to be similar if the frequency of each element is the same.

Return the minimum number of operations required to make nums similar to target. The test cases are generated such that nums can always be similar to target.

Example1:
Input: nums = [8,12,6], target = [2,14,10]
Output: 2
Explanation: It is possible to make nums similar to target in two operations:
- Choose i = 0 and j = 2, nums = [10,12,4].
- Choose i = 1 and j = 2, nums = [10,14,2].
It can be shown that 2 is the minimum number of operations needed.

Example2:
Input: nums = [1,2,5], target = [4,1,3]
Output: 1
Explanation: We can make nums similar to target in one operation:
- Choose i = 1 and j = 2, nums = [1,4,3].

Example3:
Input: nums = [1,1,1,1,1], target = [1,1,1,1,1]
Output: 0
Explanation: The array nums is already similiar to target.

Constraints:
n == nums.length == target.length
1 <= n <= 10^5
1 <= nums[i], target[i] <= 10^6
It is possible to make nums similar to target.
"""

"""
Note:
1. Greedy + Sort: O(nlogn) time | O(n) space - where n is the length of array nums
"""




import unittest
from typing import List
class Solution:
    def makeSimilar(self, nums: List[int], targets: List[int]) -> int:
        nums.sort()
        targets.sort()
        evens = []
        odds = []
        evenT = []
        oddT = []
        for num, target in zip(nums, targets):
            if num % 2 == 0:
                evens.append(num)
            else:
                odds.append(num)

            if target % 2 == 0:
                evenT.append(target)
            else:
                oddT.append(target)

        def helper(nums, targets):
            add = minus = 0
            for num, target in zip(nums, targets):
                diff = (target - num) // 2
                if diff < 0:
                    add += abs(diff)
                else:
                    minus += diff
            return min(add, minus), abs(add-minus)

        return sum(helper(evens, evenT)) + helper(odds, oddT)[0]


# Unit Tests
funcs = [Solution().makeSimilar]


class TestMakeSimilar(unittest.TestCase):
    def testMakeSimilar1(self):
        for func in funcs:
            nums = [8, 12, 6]
            targets = [2, 14, 10]
            self.assertEqual(func(nums=nums, targets=targets), 2)

    def testMakeSimilar2(self):
        for func in funcs:
            nums = [1, 2, 5]
            targets = [4, 1, 3]
            self.assertEqual(func(nums=nums, targets=targets), 1)

    def testMakeSimilar3(self):
        for func in funcs:
            nums = [1, 1, 1, 1, 1]
            targets = [1, 1, 1, 1, 1]
            self.assertEqual(func(nums=nums, targets=targets), 0)


if __name__ == "__main__":
    unittest.main()
