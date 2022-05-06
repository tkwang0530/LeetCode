"""
671. Second Minimum Node in a Binary Tree
Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes, then this node's value is the smaller value among its tow sub-nodes. More formally, the property root.val = min(root.left.val, root.right.val) always holds.

Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.

If no such second minimum value exists, output -1 instead.

Example1:
Input: root = [2,2,5,null,null,5,7]
Output: 5
Explanation: The smallest value is 2, the second smallest value is 5.

Example2:
Input: root = [2,2,2]
Output: -1
Explanation: The smallest value is 2, but there isn't any second smallest value.

Constraints:
The number of nodes in the tree is in the range [1, 25]
1 <= Node.val <= 2^31 - 1
root.val == min(root.left.val, root.right.val) for each internal node of the tree
"""

"""
Note:
1. Recursive DFS (PreOrder Traversal): O(n) time | O(h) space
2. Iterative DFS (PreOrder Traversal): O(n) time | O(h) space
"""

from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        container = [float("inf")]
        def dfs(root, container, target):
            if not root:
                return
            dfs(root.left, container, target)
            if root.val > target:
                container[0] = min(container[0], root.val)
            dfs(root.right, container, target)
        dfs(root, container, root.val)
        return container[0] if container[0] != float("inf") else -1

    def findSecondMinimumValue2(self, root: Optional[TreeNode]) -> int:
        result = float("inf")
        stack = [root]
        while stack:
            node = stack.pop()
            if node.val > root.val:
                result = min(result, node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result if result != float("inf") else -1

# Unit Tests
import unittest
funcs = [Solution().findSecondMinimumValue, Solution().findSecondMinimumValue2]

class TestFindSecondMinimumValue(unittest.TestCase):
    def testFindSecondMinimumValue1(self):
        for func in funcs:
            root = TreeNode(2, TreeNode(2), TreeNode(5, TreeNode(5), TreeNode(7)))
            self.assertEqual(func(root=root), 5)

    def testFindSecondMinimumValue2(self):
        for func in funcs:
            root = TreeNode(2, TreeNode(2), TreeNode(2))
            self.assertEqual(func(root=root), -1)

if __name__ == "__main__":
    unittest.main()
