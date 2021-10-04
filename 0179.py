"""
179. Largest Number
Given a list of non-negative integers nums, arrange them such that they form the largest number.

Note: The result may be very large, so you need to return a string instead of an integer.

Example1:
Input: nums = [10,2]
Output: "210"

Example2:
Input: nums = [3,30,34,5,9]
Output: "9534330"

Example3:
Input: nums = [1]
Output: "1"

Example4:
Input: nums = [10]
Output: "10"

Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 10^9
"""

""" 
1. Built-in Sort: O(nlogn) time | O(n) space
2. Bubble Sort: O(n^2) time | O(1+n) space
3. Selection Sort: O(n^2) time | O(1+n) space
4. Insertion Sort: O(n^2) time | O(1+n) space
5. Merge Sort: O(nlogn) time | O(n) space
6. Quick Sort: O(nlogn) time | O(logn+n) space
"""

from typing import List
import functools
class Solution(object):
    def largestNumber(self, nums: List[int]) -> str:
        if not any(nums):
            return "0"
        numStrs = list(map(str, nums))    
        cmp = lambda str1, str2: -1 if str1+str2 > str2+str1 else (1 if str1+str2 < str2+str1 else 0)
        return "".join(sorted(numStrs, key=functools.cmp_to_key(cmp)))

    def compare(self, n1: str, n2: str):
        return str(n1) + str(n2) > str(n2) + str(n1)

    # Bubble Sort
    def largestNumber2(self, nums: List[int]) -> str:
        if not any(nums):
            return "0"
        for i in range(len(nums), 0, -1):
            for j in range(i-1):
                if not self.compare(nums[j], nums[j+1]):
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        return "".join(map(str, nums))

    # selection sort
    def largestNumber3(self, nums: List[int]) -> str:
        if not any(nums):
            return "0"
        for i in range(len(nums) - 1):
            maxNumIdx = i # initialize the index of the maxNum for largest number to i+1
            for j in range(i, len(nums)):
                if self.compare(nums[j], nums[maxNumIdx]):
                    # inside this condition, the nums[j] + nums[minNumIdx] > nums[minNumIdx]: update the maxNumIdx to j
                    maxNumIdx = j

            # after the iteration, we find the index of the maxNum for largest number from i to len(nums) - 1, swap the value of index i and maxNumIdx
            nums[i], nums[maxNumIdx] = nums[maxNumIdx], nums[i]
        return "".join(map(str, nums))

    # insertion sort
    def largestNumber4(self, nums: List[int]) -> str:
        if not any(nums):
            return "0"
        for i in range(len(nums)):
            idx, num = i, nums[i]
            while idx > 0 and not self.compare(nums[idx-1], num):
                nums[idx], nums[idx-1] = nums[idx-1], nums[idx]
                idx -= 1
        return "".join(map(str, nums))

    # Merge sort
    def largestNumber5(self, nums: List[int]) -> str:
        if not any(nums):
            return "0"
        nums = self.mergeSort(nums, 0, len(nums) - 1)
        return "".join(map(str, nums))
    
    def mergeSort(self, nums, start, end):
        if start > end:
            return
        if start == end:
            return [nums[start]]
        mid = start + (end - start) // 2
        left = self.mergeSort(nums, start, mid)
        right = self.mergeSort(nums, mid+1, end)
        return self.merge(left, right)

    def merge(self, l1, l2):
        result, i, j = [], 0, 0
        while i < len(l1) and j < len(l2):
            if not self.compare(l1[i], l2[j]):
                result.append(l2[j])
                j += 1
            else:
                result.append(l1[i])
                i += 1
        result.extend(l1[i:] or l2[j:])
        return result

    # quick sort, in-place
    def largestNumber6(self, nums):
        if not any(nums):
            return "0"
        self.quickSort(nums, 0, len(nums) - 1)
        return "".join(map(str, nums))

    def quickSort(self, nums, left, right):
        if left >= right:
            return
        pivotIndex = self.partition(nums, left, right)
        self.quickSort(nums, left, pivotIndex - 1)
        self.quickSort(nums, pivotIndex + 1, right)

    def partition(self, nums, left, right):
        pivot = right
        largeIdx = left
        while left < right:
            if self.compare(nums[left], nums[pivot]):
                nums[left], nums[largeIdx] = nums[largeIdx], nums[left]
                largeIdx += 1
            left += 1
        nums[largeIdx], nums[pivot] = nums[pivot], nums[largeIdx]
        return largeIdx
    
        

# Unit Tests
import unittest
funcs = [Solution().largestNumber, Solution().largestNumber2, Solution().largestNumber3, Solution().largestNumber4, Solution().largestNumber5, Solution().largestNumber6]

class TestLargestNumber(unittest.TestCase):
    def testLargestNumber1(self):
        for func in funcs:
            nums = [10,2]
            self.assertEqual(func(nums=nums), "210")

    def testLargestNumber2(self):
        for func in funcs:
            nums = [3,30,34,5,9]
            self.assertEqual(func(nums=nums), "9534330")
    
    def testLargestNumber3(self):
        for func in funcs:
            nums = [1]
            self.assertEqual(func(nums=nums), "1")

    def testLargestNumber4(self):
        for func in funcs:
            nums = [10]
            self.assertEqual(func(nums=nums), "10")

    def testLargestNumber5(self):
        for func in funcs:
            nums = [0, 0]
            self.assertEqual(func(nums=nums), "0")

if __name__ == "__main__":
    unittest.main()
