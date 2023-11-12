"""
1630. Arithmetic Subarrays
description: https://leetcode.com/problems/arithmetic-subarrays/description/
"""

"""
Note:
1. Bucket: O(nm) time | O(n+m) space
2. Sort: O(mnlogn) time | O(n+m) space
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
    
class Solution2:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        n = len(l)
        def isArithmetic(i, j) -> bool:
            subArr = nums[i:j+1]
            subArr.sort()
            d = subArr[1] - subArr[0]
            for i in range(1, len(subArr)):
                if subArr[i] - subArr[i-1] != d:
                    return False
            return True


        output = [False] * n
        for i, (left, right) in enumerate(zip(l, r)):
            output[i] = isArithmetic(left, right)

        return output

# Unit Tests
import unittest
funcs = [Solution().checkArithmeticSubarrays, Solution2().checkArithmeticSubarrays]
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
