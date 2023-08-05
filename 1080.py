"""
1080. Insufficient Nodes in Root to Leaf Paths
Given the root of a binary tree and an integer limit, delete all insufficient nodes in the tree simultaneously, and return the root of the resulting binary tree.

A node is insufficient if every root to leaf path intersecting this node has a sum strictly less than limit.

A leaf is a node with no children.

Example1:
Input: root = [1,2,3,4,-99,-99,7,8,9,-99,-99,12,13,-99,14], limit = 1
Output: [1,2,3,4,null,null,7,8,9,null,14]

Example2:
Input: root = [5,4,8,11,null,17,4,7,1,null,null,5,3], limit = 22
Output: [5,4,8,11,null,17,4,7,null,null,null,5]

Example3:
Input: root = [1,2,-3,-5,null,4,null], limit = -1
Output: [1,null,-3,4]

Constraints:
The number of nodes in the tree is in the range [1, 5000]
-10^5 <= Node.val <= 10^5
-10^9 <= limit <= 10^9
"""

"""
Note:
1. DFS: O(n) time | O(h) space - where n is the number of nodes in the tree, and h is the height of the tree
"""

from typing import Optional
import unittest
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        def dfs(node, preSum):
            if not node:
                return False

            newPreSum = preSum + node.val
            drop = True

            if not node.right and not node.left:
                if newPreSum >= limit:
                    drop = False

            if node.right:
                keepRight = dfs(node.right, newPreSum)
                if keepRight:
                    drop = False
                if not keepRight:
                    node.right = None
        
            if node.left:
                keepLeft = dfs(node.left, newPreSum)
                if keepLeft:
                    drop = False
                if not keepLeft:
                    node.left = None
 
            return not drop

        keep = dfs(root, 0)
        return root if keep else None


# Unit Tests
funcs = [Solution().sufficientSubset]


class TestSufficientSubset(unittest.TestCase):
    def testSufficientSubset1(self):
        for func in funcs:
            limit = 1
            node1 = TreeNode(1)
            node2 = TreeNode(2)
            node3 = TreeNode(3)
            node4 = TreeNode(4)
            node7 = TreeNode(7)
            node8 = TreeNode(8)
            node9 = TreeNode(9)
            node12 = TreeNode(12)
            node13 = TreeNode(13)
            node14 = TreeNode(14)
            nodeN99_1 = TreeNode(-99)
            nodeN99_2 = TreeNode(-99)
            nodeN99_3 = TreeNode(-99)
            nodeN99_4 = TreeNode(-99)
            nodeN99_5 = TreeNode(-99)
            node1.left, node1.right = node2, node3
            node2.left, node2.right = node4, nodeN99_1
            node4.left, node4.right = node8, node9
            nodeN99_1.left, nodeN99_1.right = nodeN99_2, nodeN99_3
            node3.left, node3.right = nodeN99_4, node7
            nodeN99_4.left, nodeN99_4.right = node12, node13
            node7.left, node7.right = nodeN99_5, node14


            root = func(root=node1, limit=limit)
            self.assertEqual(root, node1)
            self.assertEqual(root.left, node2)
            self.assertEqual(root.right, node3)
            self.assertEqual(root.left.left, node4)
            self.assertEqual(root.left.right, None)
            self.assertEqual(root.right.left, None)
            self.assertEqual(root.right.right, node7)
            self.assertEqual(root.right.right.right, node14)
            self.assertEqual(root.right.right.left, None)
            self.assertEqual(root.left.left.left, node8)
            self.assertEqual(root.left.left.right, node9)

    def testSufficientSubset12(self):
        for func in funcs:
            limit = 22
            node1 = TreeNode(1)
            node3 = TreeNode(3)
            node4_1 = TreeNode(4)
            node4_2 = TreeNode(4)
            node5_1 = TreeNode(5)
            node5_2 = TreeNode(5)
            node7 = TreeNode(7)
            node8 = TreeNode(8)
            node11 = TreeNode(11)
            node17 = TreeNode(17)
           
            node5_1.left, node5_1.right = node4_1, node8
            node4_1.left, node4_1.right = node11, None
            node11.left, node11.right = node7, node1
            node8.left, node8.right = node17, node4_2
            node4_2.left, node4_2.right = node5_2, node3


            root = func(root=node5_1, limit=limit)
            self.assertEqual(root, node5_1)
            self.assertEqual(root.left, node4_1)
            self.assertEqual(root.right, node8)
            self.assertEqual(root.left.left, node11)
            self.assertEqual(root.left.right, None)
            self.assertEqual(root.right.left, node17)
            self.assertEqual(root.right.right, node4_2)
            self.assertEqual(root.left.left.left, node7)
            self.assertEqual(root.left.left.right, None)
            self.assertEqual(root.right.right.left, node5_2)
            self.assertEqual(root.right.right.right, None)

    def testSufficientSubset13(self):
        for func in funcs:
            limit = -1
            node1 = TreeNode(1)
            node2 = TreeNode(2)
            nodeN3 = TreeNode(-3)
            node4 = TreeNode(4)
            nodeN5 = TreeNode(-5)
            
            node1.left, node1.right = node2, nodeN3
            node2.left, node2.right = nodeN5, None
            nodeN3.left, nodeN3.right = node4, None


            root = func(root=node1, limit=limit)
            self.assertEqual(root, node1)
            self.assertEqual(root.left, None)
            self.assertEqual(root.right, nodeN3)
            self.assertEqual(root.right.left, node4)
            self.assertEqual(root.right.right, None)
if __name__ == "__main__":
    unittest.main()
