"""
968. Binary Tree Cameras
description: https://leetcode.com/problems/binary-tree-cameras/description/
"""

"""
Note:
1. Greedy + DFS (post order traversal): O(n) time | O(h) space - where n is the number of nodes in the tree and h is the height of the tree
Set cameras on all leaves' parents, then remove all covered nodes.
Repeat step 1 until all nodes are covered.
ref: https://leetcode.com/problems/binary-tree-cameras/solutions/211180/java-c-python-greedy-dfs/
"""


from typing import Optional
import unittest
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        container = [0]
        # return
        # 2: it's covered
        # 1: it's a parent of a leaf, with a camera on this node
        # 0: it's a leaf.
        def dfs(root):
            if not root:
                return 2  
            left = dfs(root.left)
            right = dfs(root.right)
            if 0 in (left, right):
                container[0] += 1
                return 1
            
            
            return 0 if left == 2 and right == 2 else 2

        return (dfs(root) == 0) + container[0]

# Unit Tests

funcs = [Solution().minCameraCover]
class TestMinCameraCover(unittest.TestCase):
    def testMinCameraCover1(self):
        for minCameraCover in funcs:
            root = TreeNode(0, TreeNode(0, TreeNode(0), TreeNode(0)))
            self.assertEqual(minCameraCover(root=root), 1)

    def testMinCameraCover2(self):
        for minCameraCover in funcs:
            root = TreeNode(0, TreeNode(0, TreeNode(0, TreeNode(0, None, TreeNode(0)))))
            self.assertEqual(minCameraCover(root=root), 2)

if __name__ == "__main__":
    unittest.main()
