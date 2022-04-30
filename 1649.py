"""
1649. Create Sorted Array through Instructions
Given an integer array instructions, you are asked to create a sorted array from the elements in instructions. You start with an empty container nums. For each element from left to right in instructions, insert it into nums. The cost of each insertion is the minimum of the following:
- The number of elements currently in nums that are strictly less than instructions[i].
- The number of elements currently in nums that are strictly greater than instructions[i].

For example, if inserting element 3 into nums = [1,2,3,5], the cost of insertion is min(2, 1) (elements 1 and 2 are less than 3, element 5 is greater than 3) and nums will become [1,2,3,3,5].

Return the total cost to insert all elements from instructions into nums.
Since the answer may be large, return it modulo 10^9 + 7

Example1:
Input: instructions = [1,5,6,2]
Output: 1
Explanation: Begin with nums = [].
Insert 1 with cost min(0, 0) = 0, now nums = [1].
Insert 5 with cost min(1, 0) = 0, now nums = [1,5].
Insert 6 with cost min(2, 0) = 0, now nums = [1,5,6].
Insert 2 with cost min(1, 2) = 1, now nums = [1,2,5,6].
The total cost is 0 + 0 + 0 + 1 = 1.

Example2:
Input: instructions = [1,2,3,6,5,4]
Output: 3
Explanation: Begin with nums = [].
Insert 1 with cost min(0, 0) = 0, now nums = [1].
Insert 2 with cost min(1, 0) = 0, now nums = [1,2].
Insert 3 with cost min(2, 0) = 0, now nums = [1,2,3].
Insert 6 with cost min(3, 0) = 0, now nums = [1,2,3,6].
Insert 5 with cost min(3, 1) = 1, now nums = [1,2,3,5,6].
Insert 4 with cost min(3, 2) = 2, now nums = [1,2,3,4,5,6].
The total cost is 0 + 0 + 0 + 0 + 1 + 2 = 3.

Example3:
Input: instructions = [1,3,3,3,2,4,2,1,2]
Output: 4
Explanation: Begin with nums = [].
Insert 1 with cost min(0, 0) = 0, now nums = [1].
Insert 3 with cost min(1, 0) = 0, now nums = [1,3].
Insert 3 with cost min(1, 0) = 0, now nums = [1,3,3].
Insert 3 with cost min(1, 0) = 0, now nums = [1,3,3,3].
Insert 2 with cost min(1, 3) = 1, now nums = [1,2,3,3,3].
Insert 4 with cost min(5, 0) = 0, now nums = [1,2,3,3,3,4].
Insert 2 with cost min(1, 4) = 1, now nums = [1,2,2,3,3,3,4].
Insert 1 with cost min(0, 6) = 0, now nums = [1,1,2,2,3,3,3,4].
Insert 2 with cost min(2, 4) = 2, now nums = [1,1,2,2,2,3,3,3,4].
The total cost is 0 + 0 + 0 + 0 + 1 + 0 + 1 + 0 + 2 = 4.

Constraints:
1 <= instructions.length <= 10^5
1 <= instructions[i] <= 10^5
"""

"""
Note 
1. Merge Sort: O(nlogn) time | O(nlogn) space - where n is the length of instructions
2. SortedList: O(nlogn) time | O(n) space - where n is the length of instructions
"""
from typing import List
from sortedcontainers import SortedList
class Solution(object):
    def createSortedArray(self, instructions: List[int]) -> int:
        n = len(instructions)
        cost = [[0, 0] for _ in range(n)]
        nums = [(num, i) for i, num in enumerate(instructions)]

        def mergeTwoArray(leftArr, rightArr):
            n, m = len(leftArr), len(rightArr)

            # count left smaller
            i = j = leftCountSmaller = 0
            while i < n and j < m:
                leftNum, _ = leftArr[i]
                rightNum, rightIndex = rightArr[j]
                if leftNum < rightNum:
                    leftCountSmaller += 1
                    i += 1
                else:
                    cost[rightIndex][0] += leftCountSmaller
                    j += 1

            while j < m:
                _, rightIndex = rightArr[j]
                cost[rightIndex][0] += leftCountSmaller
                j += 1

            # count left bigger
            i, j = n-1, m-1
            leftCountBigger = 0
            while i >= 0 and j >= 0:
                leftNum, _ = leftArr[i]
                rightNum, rightIndex = rightArr[j]
                if leftNum > rightNum:
                    leftCountBigger += 1
                    i -= 1
                else:
                    cost[rightIndex][1] += leftCountBigger
                    j -= 1

            while j >= 0:
                _, rightIndex = rightArr[j]
                cost[rightIndex][1] += leftCountBigger
                j -= 1

            # merge leftArr and rightArr into sorted arr
            arr = []
            i = j = 0
            while i < n and j < m:
                if leftArr[i] <= rightArr[j]:
                    arr.append(leftArr[i])
                    i += 1
                else:
                    arr.append(rightArr[j])
                    j += 1
            arr.extend(leftArr[i:]) if i < n else arr.extend(rightArr[j:])
            return arr

        def createSortedArrayHelper(left, right):
            if left == right:
                return [nums[left]]
            
            mid = left + (right - left) // 2
            leftArr = createSortedArrayHelper(left, mid)
            rightArr = createSortedArrayHelper(mid+1, right)
            return mergeTwoArray(leftArr, rightArr)

        createSortedArrayHelper(0, n-1)
        return sum([min(smaller, bigger) for smaller, bigger in cost]) % (10**9 + 7)
    
    def createSortedArray2(self, instructions: List[int]) -> int:
        sList = SortedList()
        result = 0
        for num in instructions:
            countSmaller = sList.bisect_left(num)
            countBigger = len(sList) - sList.bisect_right(num)
            result = (result + min(countSmaller, countBigger)) % (10**9 + 7)
            sList.add(num)
        return result

# Unit Tests
import unittest
funcs = [Solution().createSortedArray, Solution().createSortedArray2]

class TestCreateSortedArray(unittest.TestCase):
    def testCreateSortedArray1(self):
        for func in funcs:
            instructions = [1,5,6,2]
            self.assertEqual(func(instructions=instructions), 1)

    def testCreateSortedArray2(self):
        for func in funcs:
            instructions = [1,2,3,6,5,4]
            self.assertEqual(func(instructions=instructions), 3)

    def testCreateSortedArray3(self):
        for func in funcs:
            instructions = [1,3,3,3,2,4,2,1,2]
            self.assertEqual(func(instructions=instructions), 4)

    def testCreateSortedArray4(self):
        for func in funcs:
            instructions = [1,2,1,2,1,2,1,2,1,2,1,2]
            self.assertEqual(func(instructions=instructions), 0)

if __name__ == "__main__":
    unittest.main()
