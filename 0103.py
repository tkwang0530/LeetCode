"""
103. Binary Tree Zigzag Level Order Traversal
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values.
(i.e. from left to right, then right to left for the next level and alternate between).

Example1:
Input: root = [3, 9, 20, null, null, 15, 7]
            3
         /      \
      9          20
                  /   \
              15       7

Output: [[3],[20,9],[15,7]]

Example2:
Input: root = [1]
Output: [[1]]

Example3:
Input: root = []
Output: []
"""

"""
Note:
1. Iterative BFS: O(n) time | O(n) space
"""

from typing import List, Optional
import unittest
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagZigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        goRight = True
        result = []
        while len(queue) > 0:
            levelLength = len(queue)
            current = []
            
            for i in range(levelLength):
                node = queue.popleft() if goRight else queue.pop()
                current.append(node.val)
                if goRight:
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                else:
                    if node.right:
                        queue.appendleft(node.right)
                    if node.left:
                        queue.appendleft(node.left)
                    
            result.append(current[:])
            goRight = not goRight
        return result


# Unit Tests

funcs = [Solution().zigzagZigzagLevelOrder]
class TestZigzagLevelOrder(unittest.TestCase):
    def testZigzagLevelOrder1(self):
        for func in funcs:
            root = TreeNode(3, TreeNode(9), TreeNode(
                20, TreeNode(15), TreeNode(7)))
            self.assertEqual(func(root=root), [[3], [20, 9], [15, 7]])

    def testZigzagLevelOrder2(self):
        for func in funcs:
            root = TreeNode(1)
            self.assertEqual(func(root=root), [[1]])

    def testZigzagLevelOrder3(self):
        for func in funcs:
            root = None
            self.assertEqual(func(root=root), [])


if __name__ == "__main__":
    unittest.main()
