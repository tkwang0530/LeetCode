"""
124. Binary Tree Maximum Path Sum
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can be only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any path.

Example1:
            1
         /     \
       2       3
Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

Example2:
        -10
       /      \
     9        20
             /     \
           15     7            
Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.

Constraints:
The number of nodes in the tree is in the range [1, 3 * 10^4].
-1000 <= Node.val <= 1000
"""

"""
Note:
1. Recursion (DFS - PostOrder Traversal): O(n) time | O(n) space
(1) maxSum updates with two values: nonSplitSum, splitSum
(2) return the splitSum to its parent for further computation
Note that the nonSplitSum must include root.val

2. Iteration (DFS - PreOrder like Traversal): O(n) time | O(n) space
"""

from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        result = [root.val] # [maxSum]
        self.dfs(root, result)
        return result[0]

    def dfs(self, root: Optional[TreeNode], result: List[int]) -> int:
        if not root:
            return 0

        leftNonSplitSum = self.dfs(root.left, result)
        rightNonSplitSum = self.dfs(root.right, result)
        
        leftNonSplitSum = max(0, leftNonSplitSum)
        rightNonSplitSum = max(0, rightNonSplitSum)
        maxSplitSum = root.val + leftNonSplitSum + rightNonSplitSum
        result[0] = max(result[0], maxSplitSum)
        return root.val + max(leftNonSplitSum, rightNonSplitSum)

    def maxPathSum2(self, root: Optional[TreeNode]) -> int:
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
funcs = [Solution().maxPathSum, Solution().maxPathSum2]


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
