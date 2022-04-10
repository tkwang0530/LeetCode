"""
1498. Number of Subsequences That Satisfy the Given Sum Condition
You are given an array of integers nums and an integer target.

Return the number of non-empty subsequences of nums such that the sum of the minimum and maximum element on it is less or equal to target. Since the answer may be too large, return it modulo 10**9 + 7.

Example1:
Input: nums = [3,5,6,7], target = 9
Output: 4
Explanation: There are 4 subsequences that satisfy the condition.
[3] -> Min value + max value <= target (3 + 3 <= 9)
[3,5] -> (3 + 5 <= 9)
[3,5,6] -> (3 + 6 <= 9)
[3,6] -> (3 + 6 <= 9)

Example2:
Input: nums = [3,3,6,8], target = 10
Output: 6
Explanation: There are 6 subsequences that satisfy the condition. (nums can have repeated numbers).
[3] , [3] , [3,3], [3,6] , [3,6] , [3,3,6]

Example3:
Input: nums = [2,3,3,4,6,7], target = 12
Output: 61
Explanation: There are 63 non-empty subsequences, two of them do not satisfy the condition ([6,7], [7]).
Number of valid subsequences (63 - 2 = 61).

Constraints:
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^6
1 <= target <= 10^6
"""

""" 
1. Sort + Binary Search: O(nlogn) time | O(n) space
2. Sort + Two Pointers: O(nlogn) time | O(n) space
"""
import bisect
from typing import List
class Solution(object):
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10**9+7
        nums = [num for num in nums if num <= target]
        nums.sort()
        
        count = 0
        for i, num in enumerate(nums):
            if target-num < num:
                continue
            j = bisect.bisect_right(nums, target-num, i, len(nums))
            count = (count + pow(2, j-i-1, MOD)) % MOD
            
        return count

    def numSubseq2(self, nums: List[int], target: int) -> int:
        memo = {}
        def myPow(x, n, M):
            if n == 0:
                return 1
            if (x, n, M) in memo:
                return memo[(x, n, M)]
            ans = x
            times = 1
            while times * 2 < n:
                ans *= ans
                ans %= M
                times *= 2
            
            memo[(x, n, M)] = ans * myPow(x, n - times, M)
            return memo[(x, n, M)]

        M = 10 ** 9 + 7
        n = len(nums)
        nums.sort()
        ans = 0
        left, right = 0, n-1
        while left <= right:
            if nums[left] + nums[right] <= target:
                ans += myPow(2, (right-left), M)
                left += 1
            else:
                right -= 1
        return ans % M

# Unit Tests
import unittest
funcs = [Solution().numSubseq, Solution().numSubseq2]


class TestNumSubseq(unittest.TestCase):
    def testNumSubseq1(self):
        for func in funcs:
            nums = [3,5,6,7]
            target = 9
            self.assertEqual(func(nums=nums, target=target), 4)

    def testNumSubseq2(self):
        for func in funcs:
            nums = [3,3,6,8]
            target = 10
            self.assertEqual(func(nums=nums, target=target), 6)
    
    def testNumSubseq3(self):
        for func in funcs:
            nums = [2,3,3,4,6,7]
            target = 12
            self.assertEqual(func(nums=nums, target=target), 61)

if __name__ == "__main__":
    unittest.main()
