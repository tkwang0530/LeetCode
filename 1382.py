"""
1382. Balance a Binary Search Tree
Given a binary search tree, return a balanced binary search tree with the same node values.

A binary search tree is balanced if and only if the depth of the two subtrees of every node never differ by more than 1.

If there is more than one answer, return any of them.

Example1:
1                              2
  \                           /    \
   2                       1       3
      \                                \
        3                              4
          \
           4
Input: root = [1,null,2,null,3,null,4,null,null]
Output: [2,1,3,null,null,null,4]
Explanation: This is not the only correct answer, [3,1,4,null,2,null,null] is also correct.
"""

"""
Note:
1. DFS inorder traverse + binary search: O(n) time | O(n) space
"""


from typing import List
import unittest
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class TreeInfo:
    def __init__(self, isBalanced: bool, height: int) -> None:
        self.isBalanced = isBalanced
        self.height = height

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nums = []
        self.dfs(root, nums)
        return self.buildTree(nums, 0, len(nums) - 1)

    def dfs(self, root: TreeNode, nums: List[int]):
        if not root:
            return
        self.dfs(root.left, nums)
        nums.append(root.val)
        self.dfs(root.right, nums)
    
    def buildTree(self, nums: List[int], left: int, right: int):
        if left > right:
            return
        mid = left + (right - left) // 2
        root = TreeNode(nums[mid])
        root.left = self.buildTree(nums, left, mid - 1)
        root.right = self.buildTree(nums, mid + 1, right)
        return root

    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        stack, heights = [(root, False)], {}
        while stack:
            node, visited = stack.pop()
            if visited:
                leftHeight, rightHeight = heights.get(node.left, 0), heights.get(node.right, 0)
                if abs(leftHeight - rightHeight) > 1:
                    return False
                heights[node] = 1 + max(leftHeight, rightHeight)
            else:
                stack.append((node, True))
                if node.right:
                    stack.append((node.right, False))
                if node.left:
                    stack.append((node.left, False))
        return True

# Unit Tests
funcs = [Solution().balanceBST]


class TestBalanceBST(unittest.TestCase):
    def testBalanceBST1(self):
        for func in funcs:
            root = TreeNode(1, None, TreeNode(2, None, TreeNode(3, None, TreeNode(4))))
            inorder = []
            Solution().dfs(root, inorder)
            self.assertEqual(inorder, [1, 2, 3, 4])
            isBalanced = Solution().isBalanced(func(root=root))
            self.assertEqual(isBalanced, True)

    def testBalanceBST2(self):
        for func in funcs:
            root = TreeNode(3, TreeNode(2, TreeNode(1)))
            inorder = []
            Solution().dfs(root, inorder)
            self.assertEqual(inorder, [1, 2, 3])
            isBalanced = Solution().isBalanced(func(root=root))
            self.assertEqual(isBalanced, True)

    def testBalanceBST3(self):
        for func in funcs:
            root = TreeNode(3, TreeNode(1, None,TreeNode(2)))
            inorder = []
            Solution().dfs(root, inorder)
            self.assertEqual(inorder, [1, 2, 3])
            isBalanced = Solution().isBalanced(func(root=root))
            self.assertEqual(isBalanced, True)


if __name__ == "__main__":
    unittest.main()
