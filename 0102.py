"""
102. Binary Tree Level Order Traversal
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

Example1:
Input: root = [3, 9, 20, null, null, 15, 7]
            3
         /      \
      9          20
                  /   \
              15       7

Outputs:
[
    [3],
    [9, 20],
    [15, 7]
]
"""

"""
Note:
1. Iterative BFS: O(n) time | O(n) space
2. Recursive DFS (PreOrder Traversal): O(n) time | O(n) space
"""




from typing import List
import unittest
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        results = []
        if root is None:
            return results
        q = deque([root])
        while len(q) != 0:
            count = len(q)
            temp = []
            for _ in range(count):
                treeNode = q.popleft()
                temp.append(treeNode.val)
                if treeNode.left is not None:
                    q.append(treeNode.left)
                if treeNode.right is not None:
                    q.append(treeNode.right)
            results.append(temp)
        return results
    
    def levelOrder2(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        result = []
        self.dfs(root, 0, result)
        return result
    
    def dfs(self, root: TreeNode, level: int, result: List[int]) -> None:
        if len(result) < level+1:
            result.append([])
        result[level].append(root.val)
        if root.left:
            self.dfs(root.left, level+1, result)
        if root.right:
            self.dfs(root.right, level+1, result)


# Unit Tests

funcs = [Solution().levelOrder, Solution().levelOrder2]
class TestLevelOrder(unittest.TestCase):
    def testLevelOrder1(self):
        for func in funcs:
            root = TreeNode(3, TreeNode(9), TreeNode(
                20, TreeNode(15), TreeNode(7)))
            self.assertEqual(func(root=root), [[3], [9, 20], [15, 7]])

    def testLevelOrder2(self):
        for func in funcs:
            root = TreeNode(1)
            self.assertEqual(func(root=root), [[1]])

    def testLevelOrder3(self):
        for func in funcs:
            root = None
            self.assertEqual(func(root=root), [])


if __name__ == "__main__":
    unittest.main()
