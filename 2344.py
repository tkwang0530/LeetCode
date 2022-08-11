"""
2344. Minimum Deletions to Make Array Divisible
You are given two positive integer arrays nums and numsDivide. You can delete any number of elements from nums.

Return the minimum number of deletions such that the smallest element in nums divides all the elements of numsDivide. If this is not possible, return -1.

Note that an integer x divides y if y % x == 0.

Example1:
Input: nums = [2,3,2,4,3], numsDivide = [9,6,9,3,15]
Output: 2
Explanation: 
The smallest element in [2,3,2,4,3] is 2, which does not divide all the elements of numsDivide.
We use 2 deletions to delete the elements in nums that are equal to 2 which makes nums = [3,4,3].
The smallest element in [3,4,3] is 3, which divides all the elements of numsDivide.
It can be shown that 2 is the minimum number of deletions needed.

Example2:
Input: nums = [4,3,6], numsDivide = [8,2,6,10]
Output: -1
Explanation: 
We want the smallest element in nums to divide all the elements of numsDivide.
There is no way to delete elements from nums to allow this.

Constraints:
1 <= nums.length, numsDivide.length <= 10^5
1 <= nums[i], numsDivide[i] <= 10^9
"""

"""
Note:
1. HashTable: O(m*log(max/min)+m) + O(n) + O(log(m)) + O(n) time | O(n+log(m)) space
(1) find the greatest common factor (m) of all numbers in numsDivide
(2) find all factors of m sorted ascendingly (e.g. x1, x2, x3, ...)
(3) build numSet from array nums
(4) find the minimum x in numSet
(5) return how many number in nums that is smaller than x
"""
from typing import List
class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        def findMaxFactor(big, small) -> int:
            if big < small:
                big,small = small,big
            while (big%small) != 0:
                big, small = small,big%small
            return small
        
        def findFactors(number) -> List[int]:
            left = []
            right = []
            for i in range(1, int(number**0.5)+1):
                if number % i == 0:
                    left.append(i)
                    right.append(number//i)
            
            return left+right[::-1]
        
        maxFactor = max(numsDivide)
        for num in numsDivide:
            maxFactor = findMaxFactor(maxFactor, num)
        
        # maxFactor = 3
        factors = findFactors(maxFactor)
        
        
        numSet = set(nums)
        minFactor = -1
        for factor in factors:
            if factor in numSet:
                minFactor = factor
                break
        if minFactor == -1:
            return -1
        
        count = 0
        for num in nums:
            if num < minFactor:
                count += 1
        return count

# Unit Tests
import unittest
funcs = [Solution().minOperations]
class TestMinOperations(unittest.TestCase):
    def testMinOperations1(self):
        for func in funcs:
            nums = [2,3,2,4,3]
            numsDivide = [9,6,9,3,15]
            self.assertEqual(func(nums=nums, numsDivide=numsDivide), 2)

    def testMinOperations2(self):
        for func in funcs:
            nums = [4,3,6]
            numsDivide = [8,2,6,10]
            self.assertEqual(func(nums=nums, numsDivide=numsDivide), -1)


if __name__ == "__main__":
    unittest.main()
