"""
47. Permutations II
Given a collection of numbers, nums, that might contain duplicates,return all possible unique permutations in any order.

Example1:
    Input: [1, 1, 2]
    Output: [
        [1, 1, 2],
        [1, 2, 1],
        [2, 1, 1]
    ]
Example2:
    Input: [1, 2, 3]
    Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Constraints:
1 <= nums.length <= 8
-10 <= nums[i] <= 10
"""

"""
Note:
1. Recursion with concatenation: O(n*n!) time | O(n^2) space
2. Recursion (swap element + snapshot + set): O(n*n!) time | O(n) space
3. Recursion (number count + backtracking): O(n*n!) time | O(n) space
"""




import unittest
from typing import List
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answers = []
        self.helper(nums, [], answers)
        return answers

    def helper(self, nums: List[int], curr: List[int], answers: List[List[int]]):
        if len(nums) == 0:
            answers.append(curr.copy())
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            curr.append(nums[i])
            self.helper(nums[0:i] + nums[i + 1:], curr, answers)
            curr.pop()

    def permuteUnique2(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        self.helper2(nums, 0, permutations)
        return permutations

    def helper2(self, nums, i, permutations):
        if i == len(nums) - 1:
            permutations.append(nums[:])
        else:
            visited = set()
            for j in range(i, len(nums)):
                if nums[j] not in visited:
                    visited.add(nums[j])
                    self.swap(nums, i, j)
                    self.helper2(nums, i + 1, permutations)
                    self.swap(nums, i, j)

    def permuteUnique3(self, nums: List[int]) -> List[List[int]]:
        result = []
        count = {num: 0 for num in nums}
        for num in nums:
            count[num] += 1
        self.dfs(nums, [], result, count)
        return result

    def dfs(self, nums, current, result, count) -> None:
        if len(current) == len(nums):
            result.append(current[:])
            return
        for num in count:
            if count[num] > 0:
                current.append(num)
                count[num] -= 1
                self.dfs(nums, current, result, count)
                count[num] += 1
                current.pop()

    def swap(self, arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]


# Unit Tests
funcs = [Solution().permuteUnique, Solution().permuteUnique2, Solution().permuteUnique3]


class TestPermuteUnique(unittest.TestCase):
    def testPermuteUnique1(self):
        for func in funcs:
            self.assertEqual(
                func(nums=[1, 1, 2]).sort(),
                [[1, 1, 2], [1, 2, 1], [2, 1, 1]].sort(),
            )

    def testPermuteUnique2(self):
        for func in funcs:
            self.assertEqual(
                func(nums=[1, 2, 3]).sort(),
                [[1, 2, 3], [1, 3, 2], [2, 1, 3], [
                    2, 3, 1], [3, 1, 2], [3, 2, 1]].sort(),
            )


if __name__ == "__main__":
    unittest.main()
