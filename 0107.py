"""
107. Binary Tree Level Order Traversal II
Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values. (i.e., from left to right, level by level from leaf to root).

Example1:
Input: root = [3, 9, 20, null, null, 15, 7]
            3
         /      \
      9          20
                  /   \
              15       7

Output: [[15,7],[9,20],[3]]

Example2:
Input: root = [1]
Output: [[1]]

Example3:
Input: root = []
Output: []

Constraints:
The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
"""

"""
Note:
1. Iterative BFS: O(n) time | O(n) space
"""

from typing import List
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        result = []
        queue = deque([root])
        while len(queue) > 0:
            currentLength = len(queue)
            current = []
            for i in range(currentLength):
                node = queue.popleft()
                current.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(current[:])
        result.reverse()
        return result

# Unit Tests
import unittest
funcs = [Solution().levelOrderBottom]

class TestLevelOrderBottom(unittest.TestCase):
    def testLevelOrderBottom1(self):
        for func in funcs:
            root = TreeNode(3, TreeNode(9), TreeNode(
                20, TreeNode(15), TreeNode(7)))
            self.assertEqual(func(root=root), [[15,7],[9,20],[3]])

    def testLevelOrderBottom2(self):
        for func in funcs:
            root = TreeNode(1)
            self.assertEqual(func(root=root), [[1]])

    def testLevelOrderBottom3(self):
        for func in funcs:
            root = None
            self.assertEqual(func(root=root), [])


if __name__ == "__main__":
    unittest.main()
