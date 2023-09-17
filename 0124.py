"""
124. Binary Tree Maximum Path Sum
description: https://leetcode.com/problems/binary-tree-maximum-path-sum/description/
"""

"""
Note:
1. Recursion (DFS - PostOrder Traversal): O(n) time | O(n) space
(1) maxSum updates with two values: nonSplitSum, splitSum
(2) return the splitSum to its parent for further computation
Note that the nonSplitSum must include root.val

2. Iteration (DFS - PostOrder like Traversal): O(n) time | O(n) space
"""

from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # dfs returns the maximum non-split sum for tree with root
        # in the same time, tracing the max path sum using container
        def dfs(root, container):
            if not root:
                return 0

            leftNonSplitSum = max(0, dfs(root.left, container))
            rightNonSplitSum = max(0, dfs(root.right, container))
            
            # note: maxSplitSum must include root's val (a.k.a maxIncludeRootSum)
            maxSplitSum = root.val + leftNonSplitSum + rightNonSplitSum
            container[0] = max(container[0] , maxSplitSum)
            return root.val + max(leftNonSplitSum, rightNonSplitSum)

        container = [root.val]
        dfs(root, container)
        return container[0]

class Solution2:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = root.val
        nodeToValue = {None: 0}
        for node in self.getPostOrder(root):
            leftMax = max(0, nodeToValue.get(node.left, 0))
            rightMax = max(0, nodeToValue.get(node.right, 0))
            nodeToValue[node] = max(leftMax, rightMax) + node.val
            maxSum = max(maxSum, node.val + rightMax + leftMax)
        return maxSum

    def getPostOrder(self, root: TreeNode) -> List[TreeNode]:
        stack = [root]
        order = []
        while stack:
            node = stack.pop()
            order.append(node)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return order[::-1]



# Unit Tests
import unittest
funcs = [Solution().maxPathSum, Solution2().maxPathSum]


class TestMaxPathSum(unittest.TestCase):
    def testMaxPathSum1(self):
        for func in funcs:
            root = TreeNode(1, TreeNode(2), TreeNode(3))
            self.assertEqual(func(root=root), 6)

    def testMaxPathSum2(self):
        for func in funcs:
            root = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
            self.assertEqual(func(root=root), 42)

    def testMaxPathSum3(self):
        for func in funcs:
            root = TreeNode(-3)
            self.assertEqual(func(root=root), -3)

if __name__ == "__main__":
    unittest.main()
