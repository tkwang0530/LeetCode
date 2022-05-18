"""
1906. Minimum Absolute Difference Queries
The minimum absolute difference of an array a is defined as the minimum value of |a[i] - a[j]|, where 0 <= i < j < a.length and a[i] != a[j].

If all elements of a are the same, the minimum absolute difference is -1.
- For example, the minimum absolute difference of the array [5,2,3,7,2] is |2-3| = 1. Note that it is not 0 because a[i] and a[j] must be different.

You are given an integer array nums and the array queries where queries[i] = [li, ri]. For each query i, compute the minimum absolute difference of the subarray nums[li ... ri] containing the elements of nums between the 0-based indices li and ri (inclusive).

Return an array ans where ans[i] is the answer to the i-th query.

A subarray is a contiguous sequence of elements in an array.

The value of |x| is defined as:
- x if x >= 0.
- -x if x < 0.

Example1:
Input: nums = [1,3,4,8], queries = [[0,1],[1,2],[2,3],[0,3]]
Output: [2,1,4,1]
Explanation: The queries are processed as follows:
- queries[0] = [0,1]: The subarray is [1,3] and the minimum absolute difference is |1-3| = 2.
- queries[1] = [1,2]: The subarray is [3,4] and the minimum absolute difference is |3-4| = 1.
- queries[2] = [2,3]: The subarray is [4,8] and the minimum absolute difference is |4-8| = 4.
- queries[3] = [0,3]: The subarray is [1,3,4,8] and the minimum absolute difference is |3-4| = 1.

Example2:
Input: nums = [4,5,2,2,7,10], queries = [[2,3],[0,2],[0,5],[3,5]]
Output: [-1,1,1,3]
Explanation: The queries are processed as follows:
- queries[0] = [2,3]: The subarray is [2,2] and the minimum absolute difference is -1 because all the
  elements are the same.
- queries[1] = [0,2]: The subarray is [4,5,2] and the minimum absolute difference is |4-5| = 1.
- queries[2] = [0,5]: The subarray is [4,5,2,2,7,10] and the minimum absolute difference is |4-5| = 1.
- queries[3] = [3,5]: The subarray is [2,7,10] and the minimum absolute difference is |7-10| = 3.

Constraints:
2 <= nums.length <= 105
1 <= nums[i] <= 100
1 <= queries.length <= 2 * 104
0 <= li < ri < nums.length
"""

"""
Note:
1. preSum + HashTable: O(n + 100q) time | O(100n + q) space - where n is the length of array nums and q is the length of array queries
"""

from typing import List
class Solution:
    def minDifference(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        preNumCount = [0] * 101
        numCountArr = [preNumCount]
        for num in nums:
            numCount = preNumCount.copy()
            numCount[num] += 1
            numCountArr.append(numCount)
            preNumCount = numCount
        
        output = []
        for start, end in queries:
            minDiff = float("inf")
            preNum = -1
            for num, count in enumerate(numCountArr[end+1]):
                if num == 0:
                    continue
                if count - numCountArr[start][num] > 0:
                    if preNum != -1:
                        minDiff = min(minDiff, num - preNum)
                    preNum = num
                    
            output.append(-1 if minDiff == float("inf") else minDiff)
        return output

# Unit Tests
import unittest
funcs = [Solution().minDifference]

class TestMinDifference(unittest.TestCase):
    def testMinDifference1(self):
        for func in funcs:
            nums = [1,3,4,8]
            queries = [[0,1],[1,2],[2,3],[0,3]]
            self.assertEqual(func(nums=nums, queries=queries), [2,1,4,1])

    def testMinDifference2(self):
        for func in funcs:
            nums = [4,5,2,2,7,10]
            queries = [[2,3],[0,2],[0,5],[3,5]]
            self.assertEqual(func(nums=nums, queries=queries), [-1,1,1,3])

if __name__ == "__main__":
    unittest.main()