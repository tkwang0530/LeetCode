"""
315. Count of Smaller Numbers After Self
You are given an integer array nums and you have to return a new counts array.
The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i]

Example1:
Input: nums = [5,2,6,1]
Output: [2,1,1,0]
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.

Example2:
Input: nums = [-1]
Output: [0]

Example3:
Input: nums = [-1,-1]
Output: [0,0]

Constraints:
1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
"""

""" 
1. Segment Tree: O(nlogn) time | O(n) space
2. Merge sort: O(nlognlogn) time | O(n) space
bisect_left(arr, x, ...) returns Locate the inertion point for x in arr to maintain sorted order
The returned insertion point i partitions the array arr into two halves so that all(val < x for val in arr[lo:i]) for the left side and all(val >= x for val in a[i:hi]) for the right side.
3. Binary Indexed Tree: O(nlogn) time | O(n) space
"""

import bisect
from typing import List
class Node:
    def __init__(self, val, start, end) -> None:
        self.val = val
        self.start = start
        self.end = end
        self.children = []

class SegmentTree:
    def __init__(self, n):
        self.root = self.build(0, n-1)

    def build(self, start, end):
        if start > end:
            return
        
        root = Node(0, start, end)
        if start == end:
            return root
        
        mid = start + (end - start) // 2
        root.children.append(self.build(start, mid))
        root.children.append(self.build(mid+1, end))
        return root

    # add value to the node's and its children's val and return the node's updated val
    def update(self, i, val, node=None):
        node = node or self.root
        if i < node.start or i > node.end:
            return node.val

        if i == node.start == node.end:
            node.val += val
            return node.val
        
        node.val = sum([self.update(i, val, child) for child in node.children])
        return node.val
    
    def query(self, start, end, node=None):
        node = node or self.root
        if end < node.start or start > node.end:
            return 0
        
        # e.g. node(50, 100), start = 40, end = 110
        if start <= node.start and end >= node.end:
            return node.val

        return sum([self.query(start, end, child) for child in node.children])

class BIT: # aka Fenwick Tree
    def __init__(self, n):
        self.arr = [0] * (n+1)
    
    def update(self, i, delta=1):
        while i < len(self.arr):
            self.arr[i] += delta
            i += i & -i

    def query(self, i):
        result = 0
        while i > 0:
            result += self.arr[i]
            i -= i & -i
        return result

class Solution(object):
    def countSmaller(self, nums: List[int]) -> List[int]:
        indexDict = {num: i for i, num in enumerate(sorted(set(nums)))}
        tree = SegmentTree(len(indexDict))
        result = []

        for i in range(len(nums) - 1, -1, -1):
            result.append(tree.query(0, indexDict[nums[i]] - 1))
            tree.update(indexDict[nums[i]], 1)
        result.reverse()
        return result

    def countSmaller2(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        nums = [(n, i) for i, n in enumerate(nums)]

        def mergeTwoArray(leftArr, rightArr):
            n, m = len(leftArr), len(rightArr)
            for numIndex in leftArr:
                index = numIndex[1] # (num, i)[1] = i
                result[index] += bisect.bisect_left(rightArr, numIndex)

            # merge leftArr and rightArr into a sorted arr
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

        def countSmallerHelper(nums):
            if len(nums) <= 1:
                return nums
            
            mid = len(nums) // 2
            leftArr = countSmallerHelper(nums[:mid])
            rightArr = countSmallerHelper(nums[mid:])
            return mergeTwoArray(leftArr, rightArr)
            
        countSmallerHelper(nums)
        return result
            
    def countSmaller3(self, nums: List[int]) -> List[int]:
        # index (dict) stores the index of each num
        index = {}
        for i, num in enumerate(sorted(list(set(nums)))):
            index[num] = i
        
        tree = BIT(len(index))
        ans = [0] * len(nums)
        for i in range(len(nums)-1, -1, -1):
            num = nums[i]
            ans[i] = tree.query(index[num])
            tree.update(index[num]+1)
        return ans


# Unit Tests
import unittest
funcs = [Solution().countSmaller, Solution().countSmaller2, Solution().countSmaller3]

class TestCountSmaller(unittest.TestCase):
    def testCountSmaller1(self):
        for func in funcs:
            nums = [5,2,6,1]
            self.assertEqual(func(nums=nums), [2, 1, 1, 0])

    def testCountSmaller2(self):
        for func in funcs:
            nums = [-1]
            self.assertEqual(func(nums=nums), [0])

    def testCountSmaller3(self):
        for func in funcs:
            nums = [-1, -1]
            self.assertEqual(func(nums=nums), [0, 0])

    def testCountSmaller4(self):
        for func in funcs:
            nums = [26,78,27,100,33,67,90,23,66,5,38,7,35,23,52,22,83,51,98,69,81,32,78,28,94,13,2,97,3,76,99,51,9,21,84,66,65,36,100,41]
            self.assertEqual(func(nums=nums), [10,27,10,35,12,22,28,8,19,2,12,2,9,6,12,5,17,9,19,12,14,6,12,5,12,3,0,10,0,7,8,4,0,0,4,3,2,0,1,0])

if __name__ == "__main__":
    unittest.main()
