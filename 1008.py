"""
1008. Construct Binary Search Tree from Preorder Traversal
Given an array of integers preorder, which represents the preorder traversal of a BST, construct the tree and return its root.

It is guaranteed that there is always possible to find a binary search tree with the given requirements for the given test cases.

A binary search tree is a binary tree where for every node, any descendant of Node.left has a value strictly less than Node.val, and any descendant of Node.right has a value strictly greater than Node.val.

Example1:
Input: preorder = [8, 5, 1, 7, 10, 12]
Output: [8, 5, 10, 1, 7, null, 12]
        8
      /    \
    5     10
   /  \        \
 1    7       12 

Example2:
Input: preorder = [1, 3]
Output: [1, null, 3]
        1
           \
            3
"""

"""
Note:
1. Binary Search: O(nlogn) time | O(h) space
2. Recursion (BST Definition): O(n) time | O(h) space
Give the function a bound the maximum number it will handle.
The left recursion will take the elements smaller than node.val
The right recursion will take the remaining elements smaller than bound

3. Linear Search with array slicing: O(n^2) time | O(n^2) space
4. Linear Search with array and indices: O(n^2) time | O(h) space
"""




from typing import List
import bisect
import unittest
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        return self.helper(preorder, 0, len(preorder) - 1)

    def helper(self, preorder: List[int], startIdx: int, endIdx: int) -> TreeNode:
        if startIdx > endIdx:
            return None
        root = TreeNode(preorder[startIdx])

        # bisect(a, x, lo=0, hi=len(a)) returns an insertion point which comes after (to the right of) any existing entries of x in a.
        # https://github.com/python/cpython/blob/main/Lib/bisect.py
        mid = bisect.bisect(
            preorder, preorder[startIdx], startIdx+1, endIdx + 1)

        # mid is the beginning of the right subtree
        root.left = self.helper(preorder, startIdx + 1, mid - 1)
        root.right = self.helper(preorder, mid, endIdx)
        return root

    def bstFromPreorder2(self, preorder: List[int]) -> TreeNode:
        return self.buildTree(preorder[::-1], float('inf'))

    def buildTree(self, arr: List[int], upper) -> TreeNode:
        if len(arr) == 0 or arr[-1] >= upper:
            return None
        root = TreeNode(arr.pop())
        root.left = self.buildTree(arr, root.val)
        root.right = self.buildTree(arr, upper)
        return root

    def bstFromPreorder3(self, preorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None
        root = TreeNode(preorder[0])
        i = 1
        while i < len(preorder) and preorder[i] < root.val:
            i += 1
        root.left = self.bstFromPreorder3(preorder[1:i])
        root.right = self.bstFromPreorder3(preorder[i:])
        return root

    def bstFromPreorder4(self, preorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None

        return self.construct(preorder, 0, len(preorder) - 1)

    def construct(self, preorder, startIdx, endIdx):
        if startIdx > endIdx:
            return None
        root = TreeNode(preorder[startIdx])
        i = startIdx + 1
        while i <= endIdx and preorder[i] < root.val:
            i += 1
        root.left = self.construct(preorder, startIdx + 1, i-1)
        root.right = self.construct(preorder, i, endIdx)
        return root


# Unit Tests

funcs = [Solution().bstFromPreorder, Solution().bstFromPreorder2,
         Solution().bstFromPreorder3, Solution().bstFromPreorder4]


class TestBstFromPreorder(unittest.TestCase):

    def testBstFromPreorder1(self):
        preorder = [8, 5, 1, 7, 10, 12]
        for func in funcs:
            root = func(preorder=preorder)
            self.assertEqual(root.val, 8)
            self.assertEqual(root.left.val, 5)
            self.assertEqual(root.left.left.val, 1)
            self.assertEqual(root.left.right.val, 7)
            self.assertEqual(root.right.val, 10)
            self.assertEqual(root.right.right.val, 12)

    def testBstFromPreorder2(self):
        preorder = [1, 3]
        for func in funcs:
            root = func(preorder=preorder)
            self.assertEqual(root.val, 1)
            self.assertEqual(root.left, None)
            self.assertEqual(root.right.val, 3)


if __name__ == "__main__":
    unittest.main()
