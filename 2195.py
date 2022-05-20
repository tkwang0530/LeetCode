"""
2195. Append K Integers With Minimal Sum
You are given an integer array nums and an integer k. Append k unique positive integers that do not appear in nums to nums such that the resulting total sum is minimum.

Return the sum of the k integers appended to nums.

Example1:
Input: nums = [1,4,25,10,25], k = 2
Output: 5
Explanation: The two unique positive integers that do not appear in nums which we append are 2 and 3.
The resulting sum of nums is 1 + 4 + 25 + 10 + 25 + 2 + 3 = 70, which is the minimum.
The sum of the two integers appended is 2 + 3 = 5, so we return 5.

Example2:
Input: nums = [5,6], k = 6
Output: 25
Explanation: The six unique positive integers that do not appear in nums which we append are 1, 2, 3, 4, 7, and 8.
The resulting sum of nums is 5 + 6 + 1 + 2 + 3 + 4 + 7 + 8 = 36, which is the minimum. 
The sum of the six integers appended is 1 + 2 + 3 + 4 + 7 + 8 = 25, so we return 25.

Constraints:
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
1 <= k <= 10^8
"""

"""
Note:
1. Math + Sort: O(nlogn) time | O(1) space - where n is the length of array nums
"""

from typing import List
class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        nums.sort()
        preNum = 0
        used = 0
        currentSum = 0
        nums.append(float("inf"))
        for num in nums:
            if num - preNum <= 1:
                preNum = num
                continue
            
            space = num - preNum - 1
            if space + used >= k:
                n = k - used
                first = preNum+1
                last = preNum+n
                currentSum += (first+last) * n // 2
                return currentSum
            else:
                first = preNum+1
                last = num-1
                n = last-first+1
                currentSum += (first+last) * n // 2
                used += n
            preNum = num
        return currentSum


# Unit Tests
import unittest
funcs = [Solution().minimalKSum]

class TestMinimalKSum(unittest.TestCase):
    def testMinimalKSum1(self):
        for func in funcs:
            nums = [1,4,25,10,25]
            k = 2
            self.assertEqual(func(nums=nums, k=k), 5)

    def testMinimalKSum2(self):
        for func in funcs:
            nums = [5,6]
            k = 6
            self.assertEqual(func(nums=nums, k=k), 25)

if __name__ == "__main__":
    unittest.main()
