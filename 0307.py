"""
307. Range Sum Query - Mutable
description: https://leetcode.com/problems/range-sum-query-mutable/description/
"""

"""
Note:
1. Segment Tree
Space complexity: O(n)
Time complexity:
- __init__: O(n)
- update: O(logn)
- sumRange: O(logn)
ref: https://www.youtube.com/watch?v=rYBtViWXYeI

2. Binary Indexed Tree
Space complexity: O(n)
Time complexity:
- __init__: O(n)
- update: O(logn)
- sumRange: O(logn)
"""




import unittest
from typing import List
class Node:
    def __init__(self, start: int, end: int, val: int, left=None, right=None) -> None:
        self.start = start
        self.end = end
        self.left = left
        self.right = right
        self.val = val
        
class SegmentTree:
    def __init__(self, nums: List[int]):
        def buildTree(start: int, end: int) -> Node:
            if start == end:
                return Node(start, end, nums[start], start, start)

            mid = start + (end - start) // 2
            left = buildTree(start, mid)
            right = buildTree(mid+1, end)
            return Node(start, end, left.val + right.val, left, right)
        self.root = buildTree(0, len(nums)-1)

    def __update(self, root: Node, i: int, val: int) -> None:
        if root.start == i and root.end == i:
            root.val = val
            return

        mid = root.start + (root.end - root.start) // 2
        if i <= mid:
            self.__update(root.left, i, val)
        else:
            self.__update(root.right, i, val)
        root.val = root.left.val + root.right.val

    def update(self, i: int, val: int) -> None:
        return self.__update(self.root, i, val)

    def __query(self, root: Node, i: int, j: int) -> int:
        if i == root.start and j == root.end:
            return root.val

        mid = root.start + (root.end - root.start) // 2
        if j <= mid:
            return self.__query(root.left, i, j)
        elif i > mid:
            return self.__query(root.right, i, j)
        else:
            return self.__query(root.left, i, mid) + self.__query(root.right, mid+1, j)

    def query(self, i: int, j: int) -> int:
        return self.__query(self.root, i, j)


    
class NumArray:

    def __init__(self, nums: List[int]):
        self.tree = SegmentTree(nums)

    def update(self, index: int, val: int) -> None:
        self.tree.update(index, val)

    def sumRange(self, left: int, right: int) -> int:
        return self.tree.query(left, right)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)

class BIT:
    def __init__(self, n):
        # n+1 because BIT starts from 1
        self.arr = [0] * (n + 1)

    # return the last 1 bit of x
    def __lowbit(self, x):
        return x & -x

    # update the value of index i by delta
    def update(self, i, delta):
        while i < len(self.arr):
            self.arr[i] += delta
            i += self.__lowbit(i)

    # query the sum of [1, i]
    def query(self, i):
        ans = 0
        while i > 0:
            ans += self.arr[i]
            i -= self.__lowbit(i)
        return ans


class NumArray2:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.bit = BIT(len(nums))

        # initialize the BIT with nums
        for i, num in enumerate(nums):
            # BIT starts from 1, so we need to add 1 to i
            self.bit.update(i+1, num)

    def update(self, i: int, val: int) -> None:
        # the difference between the new value and the old value
        delta = val - self.nums[i]

        # update the BIT
        self.bit.update(i+1, delta)
        self.nums[i] = val

    def sumRange(self, left: int, right: int) -> int:
        return self.bit.query(right+1) - self.bit.query(left)


# Unit Tests
classes = [NumArray, NumArray2]


class TestNumArray(unittest.TestCase):
    def testNumArray1(self):
        for MyClass in classes:
            numArray = MyClass([1, 3, 5])
            self.assertEqual(numArray.sumRange(0, 2), 9)
            numArray.update(1, 2)
            self.assertEqual(numArray.sumRange(0, 2), 8)


if __name__ == "__main__":
    unittest.main()
