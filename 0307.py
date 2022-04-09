"""
307. Range Sum Query - Mutable
Given an integer array nums, handle multiple queries of the following types:
1. Update the value of an element in nums.
2. Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.

Implement the NumArray class:
- NumArray(int[] nums) Initializes the object with the integer array nums.
- void update(int index, int val) Updates the value of nums[index] to be val.
- int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).

Example1:
Input
["NumArray", "sumRange", "update", "sumRange"]
[[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
Output
[null, 9, null, 8]

Explanation
NumArray numArray = new NumArray([1, 3, 5]);
numArray.sumRange(0, 2); // return 1 + 3 + 5 = 9
numArray.update(1, 2);   // nums = [1, 2, 5]
numArray.sumRange(0, 2); // return 1 + 2 + 5 = 8

Constraints:
1 <= nums.length <= 3 * 10^5
-100 <= nums[i] <= 100
0 <= index < nums.length
-100 <= val <= 100
0 <= left <= right < nums.length
At most 3 * 10^4 calls will be made to update and sumRange.
"""

"""
Note:
1. Segment Tree
Space complexity: O(n)
Time complexity:
- __init__: O(n) 
- update: O(logn)
- sumRange: O(logn)

2. Binary Indexed Tree
Space complexity: O(n)
Time complexity: 
- __init__: O(n) 
- update: O(logn)
- sumRange: O(logn)
"""
from typing import List

class TreeNode:
    def __init__(self, start, end) -> None:
        self.left = None
        self.right = None
        self.start = start
        self.end = end
        self.sum = 0

class NumArray:

    def __init__(self, nums: List[int]):
        def buildTree(nums: List[int], start: int, end: int) -> TreeNode:
            if start > end:
                return None
            root = TreeNode(start, end)
            if start == end:
                root.sum = nums[start]
            else:
                mid = start + (end - start) // 2
                root.left = buildTree(nums, start, mid)
                root.right = buildTree(nums, mid+1, end)
                root.sum = root.left.sum + root.right.sum
            return root

        self.root = buildTree(nums, 0, len(nums) - 1)


    def update(self, index: int, val: int) -> None:
        def updateHelper(root: TreeNode, index: int, val: int) -> None:
            if root.start == root.end:
                root.sum = val
            else:
                mid = root.start + (root.end - root.start) // 2
                if index <= mid:
                    updateHelper(root.left, index, val)
                else:
                    updateHelper(root.right, index, val)
                root.sum  = root.left.sum + root.right.sum
        updateHelper(self.root, index, val)
        


    def sumRange(self, left: int, right: int) -> int:
        def query(root: TreeNode, i: int, j: int) -> int:
            if root.start == i and root.end == j:
                return root.sum
            mid = root.start + (root.end - root.start) // 2
            if j <= mid:
                return query(root.left, i, j)
            elif i >= mid + 1:
                return query(root.right, i, j)
            else:
                return query(root.left, i, mid) + query(root.right, mid+1, j)
        
        return query(self.root, left, right)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)

class BIT:
    def __init__(self, n):
        self.arr = [0] * (n+1)

    def update(self, i, delta):
        while i < len(self.arr):
            self.arr[i] += delta
            i += i & -i
    
    def query(self, i):
        ans = 0
        while i > 0:
            ans += self.arr[i]
            i -= i & -i
        return ans


class NumArray2:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.bit = BIT(len(nums))
        for i, num in enumerate(nums):
            self.bit.update(i+1, num)
        
    def update(self, index: int, val: int) -> None:
        delta = val - self.nums[index]
        self.bit.update(index+1, delta)
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        return self.bit.query(right+1) - self.bit.query(left)

# Unit Tests
import unittest
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