"""
2448. Minimum Cost to Make Array Equal
You are given two 0-indexed arrays nums and cost consisting each of n positive integers.
You can do the following operation any number of times:
    - Increase or decrease any element of the array nums by 1.
The cost of doing one operation on the i-th element is cost[i].

Return the minimum total cost such that all the elements of the array nums become equal.

Example1:
Input: nums = [1,3,5,2], cost = [2,3,1,14]
Output: 8
Explanation: We can make all the elements equal to 2 in the following way:
- Increase the 0th element one time. The cost is 2.
- Decrease the 1st element one time. The cost is 3.
- Decrease the 2nd element three times. The cost is 1 + 1 + 1 = 3.
The total cost is 2 + 3 + 3 = 8.
It can be shown that we cannot make the array equal with a smaller cost.

Example2:
Input: nums = [2,2,2,2,2], cost = [4,2,8,1,3]
Output: 0
Explanation: All the elements are already equal, so no operations are needed.

Constraints:
n == nums.length == cost.length
1 <= n <= 10^5
1 <= nums[i], cost[i] <= 10^6
"""

"""
Note:
1. Trinary Search: O(nlog(a)) time | O(1) space - where n is the length of array nums, and a is the range of nums[i]
Assume the final equal values are x
the total cost function y = f(x) is a convex function

To find the minimum value of f(x),
we can binary search x by comparing f(mid) and f(mid + 1).
if f(mid) <= f(mid+1),
the minimum f(x) is on the left of mid, where x <= mid

if f(mid) >= f(mid+1),
the minimum f(x) is on the right of mid+1, where x >= mid

Repeatly doing this while left < right, until we find the minimum value and return it.
"""




import unittest
from typing import List
class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        def f(x):
            return sum(abs(num-x) * c for num, c in zip(nums, cost))

        left, right = min(nums), max(nums)
        output = f(left)
        while left < right:
            mid = left + (right - left) // 2
            y1, y2 = f(mid), f(mid+1)
            output = min(output, y1, y2)
            if y1 < y2:
                right = mid
            else:
                left = mid+1
        return output


# Unit Tests
funcs = [Solution().minCost]


class TestMinCost(unittest.TestCase):
    def testMinCost1(self):
        for func in funcs:
            nums = [1, 3, 5, 2]
            cost = [2, 3, 1, 14]
            self.assertEqual(func(nums=nums, cost=cost), 8)

    def testMinCost2(self):
        for func in funcs:
            nums = [2, 2, 2, 2, 2]
            cost = [4, 2, 8, 1, 3]
            self.assertEqual(func(nums=nums, cost=cost), 0)


if __name__ == "__main__":
    unittest.main()
