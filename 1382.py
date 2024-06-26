"""
1382. Balance a Binary Search Tree
description: https://leetcode.com/problems/balance-a-binary-search-tree/description/
"""

"""
Note:
1. DFS inorder traverse + recursion: O(n) time | O(n+h) space - where n is the number of nodes in the tree and h is the height of the tree
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
        inorders = []
        def dfs(node):
            if node.left:
                dfs(node.left)
            inorders.append(node)
            if node.right:
                dfs(node.right)

        dfs(root)

        def build(left, right):
            if left > right:
                return None
            elif left == right:
                root = inorders[left]
                root.left = root.right = None
                return root
            else:
                mid = left + (right - left) // 2
                root = inorders[mid]
                leftSubTree = build(left, mid-1)
                rightSubTree = build(mid+1, right)
                root.left, root.right = leftSubTree, rightSubTree
                return root

        return build(0, len(inorders)-1)

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

    def inorder(self, root: TreeNode) -> List[int]:
        inorders = []
        def dfs(node):
            if node.left:
                dfs(node.left)
            inorders.append(node.val)
            if node.right:
                dfs(node.right)
        dfs(root)
        return inorders
# Unit Tests
funcs = [Solution().balanceBST]


class TestBalanceBST(unittest.TestCase):
    def testBalanceBST1(self):
        for func in funcs:
            root = TreeNode(1, None, TreeNode(2, None, TreeNode(3, None, TreeNode(4))))
            newRoot = func(root=root)
            self.assertEqual(Solution().inorder(root=newRoot), [1, 2, 3, 4])
            self.assertEqual(Solution().isBalanced(newRoot), True)

    def testBalanceBST2(self):
        for func in funcs:
            root = TreeNode(3, TreeNode(2, TreeNode(1)))
            newRoot = func(root=root)
            self.assertEqual(Solution().inorder(root=newRoot), [1, 2, 3])
            self.assertEqual(Solution().isBalanced(newRoot), True)

    def testBalanceBST3(self):
        for func in funcs:
            root = TreeNode(3, TreeNode(1, None,TreeNode(2)))
            newRoot = func(root=root)
            self.assertEqual(Solution().inorder(root=newRoot), [1, 2, 3])
            self.assertEqual(Solution().isBalanced(newRoot), True)


if __name__ == "__main__":
    unittest.main()
