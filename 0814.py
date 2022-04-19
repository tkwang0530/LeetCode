"""
814. Binary Tree Pruning
Given the root of a binary tree, return the same tree where every subtree (of the given tree) not containing a 1 has been removed.

A subtree of a node is node plus every node that is a decendant of node.

Example1:   
Input: root = [1,null,0,0,1]
Output: [1,null,0,null,1]
Explanation: 
Only the red nodes satisfy the property "every subtree not containing a 1".
The diagram on the right represents the answer.

Example2:
Input: root = [1,0,1,0,0,0,1]
Output: [1,null,1,null,1]

Example3:
Input: root = [1,1,0,1,1,0,1,0]
Output: [1,1,0,1,1,null,1]
"""

"""
Note:
1. Recursion: O(n) time | O(h) space - where n is the number of nodes and h is the height of the tree
2. Iterative: O(n) time | O(h) space - where n is the number of nodes and h is the height of the tree
"""

from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        left = self.pruneTree(root.left)
        right = self.pruneTree(root.right)

        if not left and not right and root.val == 0:
            return None

        root.left = left
        root.right = right

        return root

    def pruneTree2(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = []
        preNode = None
        parent = None
        dummy = TreeNode(0)
        dummy.right = root
        while root or stack:
            if root:
                stack.append((root, parent))
                parent = root
                root = root.left
            else:
                root, parent = stack[-1] if stack else (None, None)
                if not root.right or root.right == preNode:
                    # do stuff
                    if not root.left and not root.right and root.val == 0:
                        if not parent:
                            return None
                        elif parent.right == root:
                            parent.right = None
                        elif parent.left == root:
                            parent.left = None
                    stack.pop()
                    preNode, root = root, None
                else:
                    parent = root
                    root = root.right
        return dummy.right




# Unit Tests
import unittest
funcs = [Solution().pruneTree, Solution().pruneTree2]

class TestPruneTree(unittest.TestCase):
    def testPruneTree1(self):
        for func in funcs:
            root = TreeNode(1, None, TreeNode(0, TreeNode(0), TreeNode(1)))
            root = func(root=root)
            self.assertEqual(root.val, 1)
            self.assertEqual(root.left, None)
            self.assertEqual(root.right.val, 0)
            self.assertEqual(root.right.left, None)
            self.assertEqual(root.right.right.val, 1)

    def testPruneTree2(self):
        for func in funcs:
            root = TreeNode(1, TreeNode(0, TreeNode(0), TreeNode(0)), TreeNode(1, TreeNode(0), TreeNode(1)))
            root = func(root=root)
            self.assertEqual(root.val, 1)
            self.assertEqual(root.left, None)
            self.assertEqual(root.right.val, 1)
            self.assertEqual(root.right.left, None)
            self.assertEqual(root.right.right.val, 1)

    def testPruneTree3(self):
        for func in funcs:
            root = TreeNode(1, TreeNode(1, TreeNode(1, TreeNode(0), None), TreeNode(1)), TreeNode(0, TreeNode(0), TreeNode(1)))
            root = func(root=root)
            self.assertEqual(root.val, 1)
            self.assertEqual(root.left.val, 1)
            self.assertEqual(root.left.left.val, 1)
            self.assertEqual(root.left.right.val, 1)
            self.assertEqual(root.right.val, 0)
            self.assertEqual(root.right.left, None)
            self.assertEqual(root.right.right.val, 1)

    def testPruneTree4(self):
        for func in funcs:
            root = TreeNode(0, None, TreeNode(0, TreeNode(0), TreeNode(0)))
            root = func(root=root)
            self.assertEqual(root, None)

if __name__ == "__main__":
    unittest.main()
