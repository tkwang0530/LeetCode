"""
1630. Arithmetic Subarrays
A sequence of numbers is called arithmetric if it consists of at least two elements, and the difference between every two consecutive elements is the same. More formally, a sequence s is arithmetic if and only if s[i+1] - s[i] == s[1] - s[0] for all valid i.

For example, these are arithmetic sequences:
1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9

The following sequence is not arithmetic:
1, 1, 2, 5, 7

You are given an array of n integers, nums, and two arrays of m integers each, l and r, representing the m range queries, where i-th query is the range [l[i], r[i]]. All the arrays are 0-indexed.

Return a list of boolean elements answer, where answer[i] is true if the subarray nums[l[i]], nums[l[i+1]], .... nums[r[i]] can be rearranged to form an arithmetic sequence, and false otherwise.

Example1:
Input: nums = [4,6,5,9,3,7], l = [0,0,2], r = [2,3,5]
Output: [true,false,true]
Explanation:
In the 0th query, the subarray is [4,6,5]. This can be rearranged as [6,5,4], which is an arithmetic sequence.
In the 1st query, the subarray is [4,6,5,9]. This cannot be rearranged as an arithmetic sequence.
In the 2nd query, the subarray is [5,9,3,7]. This can be rearranged as [3,5,7,9], which is an arithmetic sequence.

Example2:
Input: nums = [-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10], l = [0,1,6,4,8,7], r = [4,4,9,7,9,10]
Output: [false,true,false,false,true,true]

Constraints:
n == nums.length
m == l.length
m == r.length
2 <= n <= 500
1 <= m <= 500
0 <= l[i] < r[i] < n
-10^5 <= nums[i] <= 10^5
"""

"""
Note:
1. Bucket: O(nm) time | O(n+m) space
"""

from typing import List
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        n = len(nums)
        preSum = [0] * (n+1)
        for i in range(1, n+1):
            preSum[i] = preSum[i - 1] + nums[i - 1]
            
        def rangeCheck(nums, l, r) -> bool:
            m = len(nums)
            minVal, maxVal = min(nums), max(nums)

            # check total diff
            if (maxVal - minVal) % (m - 1) != 0:
                return False

            # check sum valid
            if (minVal + maxVal) * m != (preSum[r+1] - preSum[l]) * 2:
                return False
            
            diff = int((maxVal-minVal) / (m-1))
            if diff == 0:
                return nums == ([nums[0]] * m)
            
            check = [1] * m
            for num in nums:
                if (num-minVal) % diff != 0 or check[(num-minVal) // diff] == 0:
                    return False
                check[(num-minVal) // diff] = 0
            return True

        res = []
        for i, j in zip(l, r):
            res.append(rangeCheck(nums[i:j+1], i, j))
        return res

# Unit Tests
import unittest
funcs = [Solution().checkArithmeticSubarrays]
class TestCheckArithmeticSubarrays(unittest.TestCase):
    def testCheckArithmeticSubarrays1(self):
        for func in funcs:
            nums = [4,6,5,9,3,7]
            l = [0,0,2]
            r = [2,3,5]
            self.assertEqual(func(nums=nums, l=l, r=r), [True, False, True])

    def testCheckArithmeticSubarrays2(self):
        for func in funcs:
            nums = [-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10]
            l = [0,1,6,4,8,7]
            r = [4,4,9,7,9,10]
            self.assertEqual(func(nums=nums, l=l, r=r), [False, True, False, False, True, True])

    def testCheckArithmeticSubarrays3(self):
        for func in funcs:
            nums = [-3,-6,-8,-4,-2,-8,-6,0,0,0,0]
            l = [5,4,3,2,4,7,6,1,7]
            r = [6,5,6,3,7,10,7,4,10]
            self.assertEqual(func(nums=nums, l=l, r=r), [True, True, True, True, False, True, True, True, True])

if __name__ == "__main__":
    unittest.main()
