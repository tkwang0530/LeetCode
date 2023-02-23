"""
2031. Count Subarrays With More Ones Than Zeros
You are given a binary array nums containing only the integers 0 and 1. Return the number of subarrays in nums that have more 1's than 0's. Since the answer may be very large, return it modulo 10^9 + 7.

A subarray is a contiguous sequence of elements within an array.

Example1:
Input: nums = [0,1,1,0,1]
Output: 9
Explanation:
The subarrays of size 1 that have more ones than zeros are: [1], [1], [1]
The subarrays of size 2 that have more ones than zeros are: [1,1]
The subarrays of size 3 that have more ones than zeros are: [0,1,1], [1,1,0], [1,0,1]
The subarrays of size 4 that have more ones than zeros are: [1,1,0,1]
The subarrays of size 5 that have more ones than zeros are: [0,1,1,0,1]

Example2:
Input: nums = [0]
Output: 0
Explanation:
No subarrays have more ones than zeros.

Example3:
Input: nums = [1]
Output: 1
Explanation:
The subarrays of size 1 that have more ones than zeros are: [1]

Constraints:
1 <= nums.length <= 10^5
0 <= nums[i] <= 1
"""

"""
Note:
1. preSum: O(n^2) time | O(n) space - where n is the length of nums array
2. preSum: O(n^2) time | O(n) space - where n is the length of nums array
3. preSum + BST: O(nlogn) time | O(n) space - where n is the length of nums array
4. preSum + BIT: O(nlogn) time | O(n) space - where n is the length of nums array
"""




import unittest
from typing import List
import collections
from sortedcontainers import SortedList
class BIT:

    """
    for preSum use case, n is the length of the array
    if the target array is arr = [1,2,3]
    then the BIT array is arr = [0,1,2,3]
    so the BIT array is 1-indexed, when you call update, you should pass in the index+1
    and query(i) returns the sum of the sum of the target arr from 0 to i-1, similar to the preSum array

    for counter use case, you should
    1. find the max value (maxValue), min value (minValue) of the keyes in the counter
    2. if the minValue is less than 1, shift all the keys by abs(minValue)+1 (offset)
    3. set n = maxValue + offset for building the BIT
    4. for query, use the key+offset, returns the sum of all the keys' values that are less than or equal to the key+offset
    """

    def __init__(self, n):
        # n+1 because BIT starts from 1
        # arr[0] is not used
        self.arr = [0] * (n+1)

    # lowbit(x) = x & (-x)
    # x = 5=0110
    # -x = ~x + 1 = 1001+1=1010
    def __lowbit(self, i: int) -> int:
        return i & -i

    # update the value of index i by delta
    def update(self, i, delta=1):
        while i < len(self.arr):
            self.arr[i] += delta
            i += self.__lowbit(i)
    # query returns the sum of the first i elements

    def query(self, i) -> int:
        res = 0
        while i > 0:
            res += self.arr[i]
            i -= self.__lowbit(i)
        return res


class Solution:
    def subarraysWithMoreZerosThanOnes(self, nums: List[int]) -> int:
        n = len(nums)
        modifiedNums = []
        for num in nums:
            if num == 0:
                modifiedNums.append(-1)
            else:
                modifiedNums.append(1)

        preSum = [0] * (n+1)
        for i in range(1, n+1):
            preSum[i] = preSum[i-1] + modifiedNums[i-1]

        count = 0
        for i in range(n+1):
            for j in range(i, n+1):
                if preSum[i] < preSum[j]:
                    count += 1
        return count % (10**9 + 7)

    def subarraysWithMoreZerosThanOnes2(self, nums: List[int]) -> int:
        MOD = pow(10, 9) + 7
        n = len(nums)

        # preSum
        preSum = [0] * (n+1)
        for i in range(1, n+1):
            preSum[i] = preSum[i-1] + (1 if nums[i-1] == 1 else -1)

        # O: number of ones
        # Z: number of zeros
        # counter stores the val={possible subarrays} for each key={O-Z}
        counter = collections.Counter()
        total = 0

        # input = [0, 1, 1, 0, 1]
        # shift = [-1, 1, 1, -1, 1]
        # preSum = [0, -1, 0, 1, 0, 1]

        # counter = {0:3, -1:1, 1:2}
        # total = 1+3+1+4
        for val in preSum:
            counter[val] += 1

            for num, count in counter.items():
                if num < val:
                    total = (total + count) % MOD

        return total

    def subarraysWithMoreZerosThanOnes3(self, nums: List[int]) -> int:
        MOD = pow(10, 9) + 7
        n = len(nums)

        # preSum
        preSum = [0] * (n+1)
        for i in range(1, n+1):
            preSum[i] = preSum[i-1] + (1 if nums[i-1] == 1 else -1)

        bst = SortedList([])
        total = 0

        for num in preSum:
            bst.add(num)
            total += bst.bisect_left(num)
        return total % MOD

    def subarraysWithMoreZerosThanOnes4(self, nums: List[int]) -> int:
        MOD = pow(10, 9) + 7
        n = len(nums)

        # preSum
        preSum = [0] * (n+1)
        for i in range(1, n+1):
            preSum[i] = preSum[i-1] + (1 if nums[i-1] == 1 else -1)

        minPreSum = min(preSum)
        offset = abs(minPreSum)+1 if minPreSum < 1 else 0
        tree = BIT(max(preSum) + offset)
        total = 0
        for num in preSum:
            tree.update(num+offset)
            total += tree.query(num+offset-1)
        return total % MOD


# Unit Tests
funcs = [Solution().subarraysWithMoreZerosThanOnes,
         Solution().subarraysWithMoreZerosThanOnes2, Solution().subarraysWithMoreZerosThanOnes3, Solution().subarraysWithMoreZerosThanOnes4]


class TestSubarraysWithMoreZerosThanOnes(unittest.TestCase):
    def testSubarraysWithMoreZerosThanOnes1(self):
        for func in funcs:
            nums = [0, 1, 1, 0, 1]
            self.assertEqual(func(nums=nums), 9)

    def testSubarraysWithMoreZerosThanOnes2(self):
        for func in funcs:
            nums = [0]
            self.assertEqual(func(nums=nums), 0)

    def testSubarraysWithMoreZerosThanOnes3(self):
        for func in funcs:
            nums = [1]
            self.assertEqual(func(nums=nums), 1)

    def testSubarraysWithMoreZerosThanOnes4(self):
        for func in funcs:
            nums = [1, 1, 1, 1, 1]
            self.assertEqual(func(nums=nums), 15)


if __name__ == "__main__":
    unittest.main()
