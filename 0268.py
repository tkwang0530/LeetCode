"""
268. Missing Number
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?

Example1:
Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

Example2:
Input: nums = [0,1]
Output: 2
Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

Example3:
Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.

Example4:
Input: nums = [0]
Output: 1
Explanation: n = 1 since there is 1 number, so all numbers are in the range [0,1]. 1 is the missing number in the range since it does not appear in nums.

Constraints:
n == nums.length
1 <= n <= 10^4
0 <= nums[i] <= n
All the numbers of nums are unique
"""

"""
Note:
1. xor + itertools.chain: O(n) time | O(1) space
2. Math: O(n) time | O(1) space
3. mod and divide as counter: O(n) time | O(1) space
4. mod and divide as counter 2: O(n) time | O(1) space
5. negative sign as marker: O(n) time | O(1) space
"""

from typing import List
import itertools
import functools
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return functools.reduce(lambda x, y: x ^ y, itertools.chain(nums, range(1, len(nums) + 1)))

    def missingNumber2(self, nums: List[int]) -> int:
        return (1+len(nums)) * len(nums) / 2 - sum(nums)

    def missingNumber3(self, nums: List[int]) -> int:
        n = len(nums) 
        for num in nums:
            remainder = num % (n+1)
            if remainder == 0:
                continue
            nums[remainder-1] += n+1
        for i, num in enumerate(nums):
            quotient = num // (n+1)
            if not quotient:
                return i+1
        return 0

    def missingNumber4(self, nums: List[int]) -> int:
        n = len(nums)
        nums.append(0)
        for i in range(n):
            remainder = nums[i] % (n+1)
            nums[remainder] += (n+1)
        
        for i, num in enumerate(nums):
            quotient = num // (n+1)
            if not quotient:
                return i

    def missingNumber5(self, nums: List[int]) -> int:
        offset = 1
        for i in range(len(nums)):
            nums[i] += offset
            
        nums.append(float("inf"))
        nums.append(float("inf"))
        
        for i in range(len(nums)-2):
            nums[abs(nums[i])] *= -1
            
        for i in range(1, len(nums)):
            if nums[i] > 0:
                return i-1

# Unit Tests
import unittest
funcs = [Solution().missingNumber, Solution().missingNumber2, Solution().missingNumber3, Solution().missingNumber4, Solution().missingNumber5]

class TestMissingNumber(unittest.TestCase):
    def testMissingNumber1(self):
        for func in funcs:
            nums = [3,0,1]
            self.assertEqual(func(nums=nums), 2)

    def testMissingNumber2(self):
        for func in funcs:
            nums = [0,1]
            self.assertEqual(func(nums=nums), 2)

    def testMissingNumber3(self):
        for func in funcs:
            nums = [9,6,4,2,3,5,7,0,1]
            self.assertEqual(func(nums=nums), 8)

    def testMissingNumber4(self):
        for func in funcs:
            nums = [0]
            self.assertEqual(func(nums=nums), 1)

if __name__ == "__main__":
    unittest.main()
