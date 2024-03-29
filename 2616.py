"""
2616. Minimize the Maximum Difference of Pairs
You are given a 0-indexed integer array nums and an integer p. Find p pairs of indices of nums such that the maximum difference amongst all the pairs is minimized. Also, ensure no index appears more than once amongst the p pairs.

Note that for a pair of elements at the index i and j, the difference of this pair is |nums[i] - nums[j]|, where |x| represents the absolute value of x.

Return the minimum maximum difference among all p pairs. We define the maximum of an empty set to be zero.

Example1:
Input: nums = [10,1,2,7,1,3], p = 2
Output: 1
Explanation: The first pair is formed from the indices 1 and 4, and the second pair is formed from the indices 2 and 5. 
The maximum difference is max(|nums[1] - nums[4]|, |nums[2] - nums[5]|) = max(0, 1) = 1. Therefore, we return 1.

Example2:
Input: nums = [4,2,1,2], p = 1
Output: 0
Explanation: Let the indices 1 and 3 form a pair. The difference of that pair is |2 - 2| = 0, which is the minimum we can attain.

Constraints:
1 <= nums.length <= 10^5
0 <= nums[i] <= 10^9
0 <= p <= (nums.length)/2
"""

"""
Note:
1. Binary Search + Sort: O(nlog(r)) time | O(1) space - where n is the length of array nums, r is the range of nums[i]
2. dfs + memo + Sort: O(nlogn + np) time | O(np) space  - where n is the length of array nums
"""




from typing import List
import unittest, functools
class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        left, right = 0, 10**9+1

        def condition(mid, p):
            count = 0
            i = 0
            while i < len(nums) - 1:
                first, second = nums[i], nums[i+1]
                if second - first <= mid:
                    count += 1
                    if count == p:
                        return True
                    i += 2
                else:
                    i += 1
            return count >= p

        while left < right:
            mid = left + (right - left) // 2
            if condition(mid, p):
                right = mid
            else:
                left = mid + 1
        return left

    def minimizeMax2(self, nums: List[int], p: int) -> int:
        nums.sort()

        @functools.lru_cache(None)
        def dfs(i, p):
            if i >= len(nums)-1 or p == 0:
                if p > 0:
                    return float("inf")
                return float("-inf")

            maxVal1 = max(abs(nums[i]-nums[i+1]), dfs(i+2, p-1))
            maxVal2 = dfs(i+1, p)
            return min(maxVal1, maxVal2)

        if p == 0:
            return 0
        return dfs(0, p)


# Unit Tests
funcs = [Solution().minimizeMax, Solution().minimizeMax2]


class TestMinimizeMax(unittest.TestCase):
    def testMinimizeMax1(self):
        for func in funcs:
            nums = [10, 1, 2, 7, 1, 3]
            p = 2
            self.assertEqual(func(nums=nums, p=p), 1)

    def testMinimizeMax2(self):
        for func in funcs:
            nums = [4, 2, 1, 2]
            p = 1
            self.assertEqual(func(nums=nums, p=p), 0)


if __name__ == "__main__":
    unittest.main()
