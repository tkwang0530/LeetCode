"""
951. Flip Equivalent Binary Trees
description: https://leetcode.com/problems/flip-equivalent-binary-trees/description/
"""

"""
Note:
1. BFS (PreOrder Traversal: O(n) time | O(n) space - where n is the number of nodes in the tree
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import collections
from typing import Optional
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2:
            return True
        
        if (not root1 and root2) or (root1 and not root2):
            return False

        if root1.val != root2.val:
            return False

        queue = collections.deque([(root1, root2)])
        while queue:
            node1, node2 = queue.popleft()

            # node1
            leftVal1 = node1.left.val if node1.left else None
            rightVal1 = node1.right.val if node1.right else None

            # node2
            leftVal2 = node2.left.val if node2.left else None
            rightVal2 = node2.right.val if node2.right else None

            if (leftVal1 == leftVal2) and (rightVal1 == rightVal2):
                if leftVal1:
                    queue.append((node1.left, node2.left))
                if rightVal1:
                    queue.append((node1.right, node2.right))
            elif (leftVal1 == rightVal2) and (rightVal1 == leftVal2):
                if leftVal1:
                    queue.append((node1.left, node2.right))
                if rightVal1:
                    queue.append((node1.right, node2.left))
            else:
                return False
        
        return True

funcs = [Solution().flipEquiv]

import unittest
class TestFlipEquiv(unittest.TestCase):
    def testFlipEquiv1(self):
        for func in funcs:
            root1 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5, TreeNode(7), TreeNode(8))), TreeNode(3, TreeNode(6)))
            root2 = TreeNode(1, TreeNode(3, None, TreeNode(6)), TreeNode(2, TreeNode(4), TreeNode(5, TreeNode(8), TreeNode(7))))
            self.assertEqual(func(root1=root1, root2=root2), True)

    def testFlipEquiv2(self):
        for func in funcs:
            root1 = None
            root2 = None
            self.assertEqual(func(root1=root1, root2=root2), True)

    def testFlipEquiv3(self):
        for func in funcs:
            root1 = None
            root2 = TreeNode(1)
            self.assertEqual(func(root1=root1, root2=root2), False)

if __name__ == "__main__":
    unittest.main()
