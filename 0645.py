"""
645. Set Mismatch
You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.

Example1:
Input: nums = [1,2,2,4]
Output: [2,3]

Example2:
Input: nums = [1,1]
Output: [1,2]

Constraints:
2 <= nums.length <= 10^4
1 <= nums[i] <= 10^4
"""

"""
Note:
1. Brute-Force: O(n) time | O(n) space - where n is the length of array nums
"""




import unittest
from typing import List
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        numCount = [0] * (n+1)
        for num in nums:
            numCount[num] += 1

        output = [-1, -1]
        for num in range(1, n+1):
            if numCount[num] == 2:
                output[0] = num
            elif numCount[num] == 0:
                output[1] = num

        return output


# Unit Tests
funcs = [Solution().findErrorNums]


class TestFindErrorNums(unittest.TestCase):
    def testFindErrorNums1(self):
        for func in funcs:
            nums = [1, 2, 2, 4]
            self.assertEqual(func(nums=nums), [2, 3])

    def testFindErrorNums2(self):
        for func in funcs:
            nums = [1, 1]
            self.assertEqual(func(nums=nums), [1, 2])


if __name__ == "__main__":
    unittest.main()
