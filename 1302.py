"""
1302. Deepest Leaves Sum
Given the root of a binary tree, return the sum of values of its deepest leaves

Example1:
                1                                       
            /       \                            
         2           3                
      /     \           \
    4        5           6
   /                         \
  7                          8
Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15

Example2:
Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 19

Constraints:
The number of nodes in the tree is in the range [1, 10^4]
1 <= Node.val <= 100
"""

"""
Note:
1. Recursive DFS (preorder): O(n) time | O(h) space
track level
if level > maxLevel: reset the deepSum to node.val
if level == maxLevel: deepSum += node.val
2. Iterative DFS (preorder): O(n) time | O(h) space
"""


from typing import Optional, List
import unittest
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deepestLeaveSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        result = [1, 0] # [maxLevel, deepSum]
        self.dfs(root, 1, result)
        return result[1]

    def dfs(self, node: TreeNode, level: int, result: List[int]) -> None:
        if result[0] == level:
            result[1] += node.val
        elif result[0] < level:
            result[1] = node.val
            result[0] = level
        if node.left:
            self.dfs(node.left, level + 1, result)
        if node.right:
            self.dfs(node.right, level + 1, result)

    def deepestLeaveSum2(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        maxLevel, deepSum = 1, 0
        stack = [(root, 1)] # (node, level)
        while len(stack) > 0:
            node, level = stack.pop()
            if level == maxLevel:
                deepSum += node.val
            elif level > maxLevel:
                deepSum = node.val
                maxLevel = level
            if node.right:
                stack.append((node.right, level + 1))
            if node.left:
                stack.append((node.left, level + 1))
        return deepSum


# Unit Tests
funcs = [Solution().deepestLeaveSum, Solution().deepestLeaveSum2]


class TestDeepestLeaveSum(unittest.TestCase):
    def testDeepestLeaveSum1(self):
        for func in funcs:
            root = TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(7)), TreeNode(5)), TreeNode(3, None, TreeNode(6, None, TreeNode(8))))
            self.assertEqual(func(root=root), 15)

    def testDeepestLeaveSum2(self):
        for func in funcs:
            root = TreeNode(6, TreeNode(7, TreeNode(2, TreeNode(9), None), TreeNode(7, TreeNode(1), TreeNode(4))), TreeNode(8, TreeNode(1), TreeNode(3, None, TreeNode(5))))
            self.assertEqual(func(root=root), 19)


if __name__ == "__main__":
    unittest.main()
