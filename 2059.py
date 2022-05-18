"""
2059. Minimum Operations to Convert Number
You are given a 0-indexed integer array nums containing distinct numbers, an integer start, and an integer goal. There is an integer x that is initially set to start, and you want to perform operations on x such that it is converted to goal. You can perform the following operation repeatedly on the number x:

if 0 <= x <= 1000, then for any index i in the array (0 <= i < nums.length), you can set x to any of the following:
    - x + nums[i]
    - x - nums[i]
    - x ^ nums[i] (bitwise-XOR)

Note that you can use each nums[i] any number of times in any order.
Operations that set x to be out of the range 0 <= x <= 1000 are valid, but no more operations can be done afterward.

Return the minimum number of operations needed to convert x = start into goal, and -1 if it is not possible.

Example1:
Input: nums = [2,4,12], start = 2, goal = 12
Output: 2
Explanation: We can go from 2 → 14 → 12 with the following 2 operations.
- 2 + 12 = 14
- 14 - 2 = 12

Example2:
Input: nums = [3,5,7], start = 0, goal = -4
Output: 2
Explanation: We can go from 0 → 3 → -4 with the following 2 operations. 
- 0 + 3 = 3
- 3 - 7 = -4
Note that the last operation sets x out of the range 0 <= x <= 1000, which is valid.

Example3:
Input: nums = [2,8,16], start = 0, goal = 1
Output: -1
Explanation: There is no way to convert 0 into 1.

Constraints:
1 <= nums.length <= 1000
-10^9 <= nums[i], goal <= 10^9
0 <= start <= 1000
start != goal
All the integers in nums are distinct.
"""

"""
Note:
1. BFS + HashTable: O(3000n) time | O(1000) space
2. BFS + HashTable + preprocess: O(3000n) time | O(1000) space
"""

from typing import List
class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        operations = 0
        currentSet = set([start])
        visited = set([start])
        while currentSet:
            nextSet = set()
            for currNum in currentSet:
                if currNum == goal:
                    return operations
                if not 0 <= currNum <= 1000:
                    continue
                for num in nums:
                    for nextNum in [currNum+num, currNum-num, currNum^num]:
                        if nextNum in visited:
                            continue
                        visited.add(nextNum)
                        nextSet.add(nextNum)
            operations += 1
            currentSet = nextSet
        return -1

    def minimumOperations2(self, nums: List[int], start: int, goal: int) -> int:
        smalls = [num for num in nums if -1000 <= num <= 1000]
        bigs = [num for num in nums if not -1000 <= num <= 1000]
        almostThere = {goal - b for b in bigs} | {goal + b for b in bigs} | {goal ^ b for b in bigs}

        operations = 0
        currentSet = set([start])
        visited = set([start])
        
        while currentSet:
            nextSet = set()
            for currNum in currentSet:
                if currNum == goal:
                    return operations
                if currNum in almostThere:
                    return operations + 1
                if not 0 <= currNum <= 1000:
                    continue
                for num in smalls:
                    for nextNum in [currNum+num, currNum-num, currNum^num]:
                        if nextNum in visited:
                            continue
                        visited.add(nextNum)
                        nextSet.add(nextNum)
            operations += 1
            currentSet = nextSet
        return -1

# Unit Tests
import unittest
funcs = [Solution().minimumOperations, Solution().minimumOperations2]

class TestMinimumOperations(unittest.TestCase):
    def testMinimumOperations1(self):
        for func in funcs:
            nums = [2,4,12]
            start = 2
            goal = 12
            self.assertEqual(func(nums=nums, start=start, goal=goal), 2)

    def testMinimumOperations2(self):
        for func in funcs:
            nums = [3,5,7]
            start = 0
            goal = -4
            self.assertEqual(func(nums=nums, start=start, goal=goal), 2)

    def testMinimumOperations2(self):
        for func in funcs:
            nums = [2,8,16]
            start = 0
            goal = 1
            self.assertEqual(func(nums=nums, start=start, goal=goal), -1)

if __name__ == "__main__":
    unittest.main()