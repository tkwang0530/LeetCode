"""
1008. Construct Binary Search Tree from Preorder Traversal
description: https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/description/
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
5. monotonic stack+recursion: O(n) time | O(n) space
"""




from typing import List, Optional
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

class Solution2:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        return self.buildTree(preorder[::-1], float('inf'))

    def buildTree(self, arr: List[int], upper) -> TreeNode:
        if len(arr) == 0 or arr[-1] >= upper:
            return None
        root = TreeNode(arr.pop())
        root.left = self.buildTree(arr, root.val)
        root.right = self.buildTree(arr, upper)
        return root

class Solution3:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None
        root = TreeNode(preorder[0])
        i = 1
        while i < len(preorder) and preorder[i] < root.val:
            i += 1
        root.left = self.bstFromPreorder(preorder[1:i])
        root.right = self.bstFromPreorder(preorder[i:])
        return root

class Solution4:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
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

class Solution5:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        n = len(preorder)
        nextLargerIndice = {} #<currentIdx, nextLargetIndex>  右邊第一個比自己的值大的element的index
        stack = [] #[(num, i)]
        for i, num in enumerate(preorder):
            while stack and stack[-1][0] < num:
                _, idx = stack.pop()
                nextLargerIndice[idx] = i
            stack.append((num, i))
        
        def dfs(left, right):
            if left > right:
                return None
            if left == right:
                return TreeNode(preorder[left])

            root = TreeNode(preorder[left])
            if left in nextLargerIndice:
                root.right = dfs(nextLargerIndice[left], right)
            
            if left in nextLargerIndice:
                root.left = dfs(left+1, nextLargerIndice[left]-1)
            else:
                root.left = dfs(left+1, right)

            return root

        return dfs(0, n-1)
    
# Unit Tests
funcs = [Solution().bstFromPreorder, Solution2().bstFromPreorder,
         Solution3().bstFromPreorder, Solution4().bstFromPreorder, Solution5().bstFromPreorder]
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
