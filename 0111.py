"""
111. Minimum Depth of Binary Tree
Given a binary tree, find its minimum depth

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children

Example1:
            3
         /      \
      9          20
                 /   \
              15    7
Input: root = [3,9,20,null,null,15,7]
Output: 2

Example2:
Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5
"""

"""
Note:
1. DFS: O(n) time | O(n) space 
2. BFS: O(n) time | O(n) space
"""




from collections import deque
import unittest
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if None in [root.left, root.right]:
            return max(self.minDepth(root.left), self.minDepth(root.right)) + 1
        else:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

    def minDepth2(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = deque([(root, 1)])
        while queue:
            node, level = queue.popleft()
            if not node.left and not node.right:
                return level
            else:
                if node.left:
                    queue.append((node.left, level + 1))
                if node.right:
                    queue.append((node.right, level + 1))


# Unit Tests
funcs = [Solution().minDepth, Solution().minDepth2]


class TestMinDepth(unittest.TestCase):
    def testMinDepth1(self):
        for func in funcs:
            root = TreeNode(3, TreeNode(9), TreeNode(
                20, TreeNode(15), TreeNode(7)))
            self.assertEqual(func(root=root), 2)

    def testMinDepth2(self):
        for func in funcs:
            root = TreeNode(2, None, TreeNode(3, None, TreeNode(
                4, None, TreeNode(5, None, TreeNode(6)))))
            self.assertEqual(func(root=root), 5)

    def testMinDepth3(self):
        for func in funcs:
            root = TreeNode(1, TreeNode(2), TreeNode(3))
            self.assertEqual(func(root=root), 2)


if __name__ == "__main__":
    unittest.main()
