"""
238. Product of Array Except Self
description: https://leetcode.com/problems/product-of-array-except-self/description
"""

"""
Note:
1. Brute Force: O(n^2) time | O(1) space
2. leftProducts + rightProducts: O(n) space | O(n) space
3. leftRunningProduct + rightRunningProduct: O(n) space | O(1) space
"""




import unittest
from  typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = [1 for _ in range(len(nums))]
        for i in range(len(nums)):
            runningProduct = 1
            for j in range(len(nums)):
                if i != j:
                    runningProduct *= nums[j]
            products[i] = runningProduct
        return products

    def productExceptSelf2(self, nums: List[int]) -> List[int]:
        products = [1] * len(nums)
        leftProducts, rightProducts = [1] * len(nums), [1] * len(nums)
        for i in range(1, len(nums)):
            leftProducts[i] = nums[i-1] * leftProducts[i-1]
        for i in range(len(nums) - 2, -1, -1):
            rightProducts[i] = nums[i+1] * rightProducts[i+1]
        for i in range(len(nums)):
            products[i] = leftProducts[i] * rightProducts[i]
        return products


    def productExceptSelf3(self, nums: List[int]) -> List[int]:
        products = [1 for _ in range(len(nums))]
        leftRunningProduct = rightRunningProduct = 1
        for i in range(len(nums)):
            products[i] *= leftRunningProduct
            leftRunningProduct *= nums[i]

        for i in reversed(range(len(nums))):
            products[i] *= rightRunningProduct
            rightRunningProduct *= nums[i]
        return products


# Unit Tests

funcs = [Solution().productExceptSelf, Solution().productExceptSelf2, Solution().productExceptSelf3]


class TestProductExceptSelf(unittest.TestCase):
    def testProductExceptSelf1(self):
        for func in funcs:
            nums = [1, 2, 3, 4]
            self.assertEqual(func(nums=nums), [24, 12, 8, 6])

    def testProductExceptSelf2(self):
        for func in funcs:
            nums = [-1, 1, 0, -3, 3]
            self.assertEqual(func(nums=nums), [0, 0, 9, 0, 0])


if __name__ == "__main__":
    unittest.main()
