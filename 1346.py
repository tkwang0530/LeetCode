"""
1346. Check If N and Its Double Exist
Given an array arr of integers, check if there exists two integers N and M such that N is the double of M (i.e. N = 2 * M)

More formally check if there exists two indices i and j such that:
- i != j
- 0 <= i, j < arr.length
- arr[i] == 2 * arr[j]

Example1:
Input: arr = [10,2,5,3]
Output: true
Explanation: N = 10 is the double of M = 5,that is, 10 = 2 * 5.

Example2:
Input: arr = [7,1,14,11]
Output: true
Explanation: N = 14 is the double of M = 7,that is, 14 = 2 * 7.

Example3:
Input: arr = [3,1,7,11]
Output: false
Explanation: In this case does not exist N and M, such that N = 2 * M.

Constraints:
2 <= nums.length <= 500
-100 <= nums[i] <= 100
nums is sorted in non-decreasing order.
"""

"""
Note:
1. Brute-Force: O(n^2) time | O(1) space
2. Use Hash Table: O(n) time | O(n) space
"""

from typing import List
import unittest
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i in range(len(arr) - 1):
            for j in range(i+1, len(arr)):
                if arr[i] == arr[j] * 2 or arr[i] * 2 == arr[j]:
                    return True
        return False

    def checkIfExist2(self, arr: List[int]) -> bool:
        nums = set()
        for num in arr:
            if num * 2 in nums or num / 2 in nums:
                return True
            nums.add(num)
        return False




# Unit Tests
funcs = [Solution().checkIfExist, Solution().checkIfExist2]


class TestCheckIfExist(unittest.TestCase):
    def testCheckIfExist1(self):
        for func in funcs:
            arr = [10,2,5,3]
            self.assertEqual(func(arr=arr), True)

    def testCheckIfExist2(self):
        for func in funcs:
            arr = [7,1,14,11]
            self.assertEqual(func(arr=arr), True)

    def testCheckIfExist3(self):
        for func in funcs:
            arr = [3,1,7,11]
            self.assertEqual(func(arr=arr), False)

if __name__ == "__main__":
    unittest.main()
