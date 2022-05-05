"""
226. Invert Binary Tree
Given the root of a binary tree, invert the tree, and return its root.

Example1:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Example2:
Input: root = [2,1,3]
Output: [2,3,1]

Example3:
Input: root = []
Output: []

Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""

"""
Note:
1. Recursive DFS (PostOrder Traversal): O(n) time | O(h) space
2. Iterative DFS (PreOrder Traversal): O(n) time | O(h) space
3. Iterative BFS: O(n) time | O(n) space
"""

from typing import Optional, List
import collections
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        self.invertTree(root.left)
        self.invertTree(root.right)
        root.left, root.right = root.right, root.left
        return root

    def invertTree2(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        stack = [root]
        while stack:
            node = stack.pop()
            node.left, node.right = node.right, node.left
            if node.right:
                stack.append(node.right)

            if node.left:
                stack.append(node.left)
        return root

    def invertTree3(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
            node.left, node.right = node.right, node.left
            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)
        return root

# Unit Tests
import unittest
funcs = [Solution().invertTree, Solution().invertTree2, Solution().invertTree3]

def inorder(root: TreeNode) -> List[int]:
    result = []
    if not root:
        return result
    inorderHelper(root, result)
    return result

def inorderHelper(root, result) -> None:
    if root.left:
        inorderHelper(root.left, result)
    result.append(root.val)
    if root.right:
        inorderHelper(root.right, result)

class TestInvertTree(unittest.TestCase):
    def testInvertTree1(self):
        for func in funcs:
            root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
            self.assertEqual(inorder(func(root=root)), [9, 7, 6, 4, 3, 2, 1])

    def testInvertTree2(self):
        for func in funcs:
            root = TreeNode(2, TreeNode(1), TreeNode(3))
            self.assertEqual(inorder(func(root=root)), [3, 2, 1])

    def testInvertTree3(self):
        for func in funcs:
            root = None
            self.assertEqual(inorder(func(root=root)), [])

if __name__ == "__main__":
    unittest.main()
