"""
257. Binary Tree Paths
Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.

Example1:
        1
     /      \
   2         3
      \
        5
Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]

Example2:
Input: root = [1]
Output: ["1"]

Constraints:
The number of nodes in the tree is in the range [1, 100].
-100 <= Node.val <= 100
"""

"""
Note:
1. Recursion (DFS - PreOrder Traversal): O(n) time | O(n) space
"""


from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        result = []
        self.dfs(root, [], result)
        return result
    
    def dfs(self, root, current, result) -> None:
        current.append(str(root.val))
        if not root.left and not root.right:
            result.append("->".join(current))
        
        if root.left:
            self.dfs(root.left, current, result)
        if root.right:
            self.dfs(root.right, current, result)
        current.pop()


# Unit Tests
import unittest
funcs = [Solution().binaryTreePaths]

class TestBinaryTreePaths(unittest.TestCase):
    def testBinaryTreePaths1(self):
        for func in funcs:
            root = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3))
            self.assertEqual(func(root=root), ["1->2->5", "1->3"])

    def testBinaryTreePaths2(self):
        for func in funcs:
            root = TreeNode(1)
            self.assertEqual(func(root=root), ["1"])


if __name__ == "__main__":
    unittest.main()
