"""
698. Partition to K Equal Sum Subsets
Given an integer array nums and an integer k, return true if it is possible to divide this array into k non-empty subsets whose sums are all equal.

Example1:
Input: nums = [4,3,2,3,5,2,1], k = 4
Output: true
Explanation: It is possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.

Example2:
Input: nums = [1,2,3,4], k = 3
Output: false

Constraints:
1 <= k <= <= nums.length <= 16
1 <= nums[i] <= 10^4
The frequency of each element is in the range [1, 4].
"""

"""
Note:
1. DFS (Top Down) + Backtracking: O(n * n!) time | O(n) space
2. DFS (Bottom Up) + Backtracking + memo: O(klogk * k**n) | O(kn) space
"""

from typing import List
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False

        target = total // k

        n = len(nums)
        visited = [False] * n

        nums.sort(reverse=True)
        def dfs(i, currentSum, k, visited) -> bool:
            if k == 1:
                return True
            for j in range(i, n):
                if visited[j]:
                    continue
                
                if currentSum + nums[j] > target:
                    break

                visited[j] = True
                if currentSum + nums[j] == target:
                    if dfs(0, 0, k-1, visited):
                        return True
                else:
                    if dfs(0, currentSum+nums[j], k, visited):
                        return True
                visited[j] = False

            return False
        return dfs(0, 0, k, visited)

    def canPartitionKSubsets2(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False
        
        buckets = [total // k] * k
        nums.sort(reverse=True)

        memo = {}
        def dfs(i, buckets, totalSum):
            key = (str(sorted(buckets)), i)
            if key in memo:
                return memo[key]
            if totalSum == 0:
                memo[key] = True
                return memo[key]

            num = nums[i]
            for j in range(k):
                if buckets[j] - num < 0:
                    continue
                buckets[j] -= num
                if dfs(i+1, buckets, totalSum - num):
                    memo[key] = True
                    return memo[key]
                buckets[j] += num

            memo[key] = False
            return memo[key]
        return dfs(0, buckets, total)

# Unit Tests
import unittest
funcs = [Solution().canPartitionKSubsets, Solution().canPartitionKSubsets2]

class TestCanPartitionKSubsets(unittest.TestCase):
    def testCanPartitionKSubsets1(self):
        for func in funcs:
            nums = [4,3,2,3,5,2,1]
            k = 4
            self.assertEqual(func(nums=nums, k=k), True)

    def testCanPartitionKSubsets2(self):
        for func in funcs:
            nums = [1,2,3,4]
            k = 3
            self.assertEqual(func(nums=nums, k=k), False)

    def testCanPartitionKSubsets3(self):
        for func in funcs:
            nums = [1,1,1,1,2,2,2,2]
            k = 4
            self.assertEqual(func(nums=nums, k=k), True)

if __name__ == "__main__":
    unittest.main()