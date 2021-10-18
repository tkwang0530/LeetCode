"""
993. Cousins in Binary Tree
Given the root of a binary tree with unique values and the values of two different nodes of the tree x and y, return true if the nodes corresponding to the values x and y in the tree are cousins, or false otherwise.

Two nodes of a binary tree are cousins if they have the same depth with different parents.

Note that in a binary tree, the root node is at the depth 0, and children of each depth k node are at the depth k + 1.

Example1:
            1
         /     \ 
       2       3 
     /
   4
Input: root = [1,2,3,4], x = 4, y = 3
Output: false

Example2:
            1
         /     \ 
       2       3 
          \        \
           4        5
Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true

Example3:
            1
         /     \ 
       2       3 
          \ 
           4 
Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false

Constraints:
The number of nodes in the tree is in the range [2, 100].
1 <= Node.val <= 100
Each node has a unique value.
x != y
x and y are exist in the tree
"""

"""
Note:
1. Iteration (BFS) : O(n) time | O(n) space
Find x and y first
"""

import collections
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        nodeXInfo = [None, None, None] # [node, parent, level]
        nodeYInfo = [None, None, None] # [node, parent, level]
        queue = collections.deque([(root, None, 0)])
        while queue:
            node, parent, level = queue.popleft()
            if node.val == x:
                nodeXInfo[0], nodeXInfo[1], nodeXInfo[2] = node, parent, level
            if node.val == y:
                nodeYInfo[0], nodeYInfo[1], nodeYInfo[2] = node, parent, level
            if nodeXInfo[0] and nodeYInfo[0]:
                return (nodeXInfo[1] != nodeYInfo[1]) and (nodeXInfo[2] == nodeYInfo[2])
            if node.left:
                queue.append((node.left, node, level+1))
            if node.right:
                queue.append((node.right, node, level+1))
        return False


# Unit Tests
import unittest
funcs = [Solution().isCousins]


class TestIsCousins(unittest.TestCase):
    def testIsCousins1(self):
        for func in funcs:
            root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))
            x = 4
            y = 3
            self.assertEqual(func(root=root, x=x, y=y), False)

    def testIsCousins2(self):
        for func in funcs:
            root = TreeNode(1, TreeNode(2, None, TreeNode(4)), TreeNode(3, None, TreeNode(5)))
            x = 5
            y = 4
            self.assertEqual(func(root=root, x=x, y=y), True)

    def testIsCousins3(self):
        for func in funcs:
            root = TreeNode(1, TreeNode(2, None, TreeNode(4)), TreeNode(3))
            x = 2
            y = 3
            self.assertEqual(func(root=root, x=x, y=y), False)


if __name__ == "__main__":
    unittest.main()
