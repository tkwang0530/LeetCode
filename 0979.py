"""
979. Distribute Coins in Binary Tree
You are given the root of a binary tree with n nodes where each node in the tree has node.val coins. There are n coins in total throughout the whole tree.

In one move, we may choose two adjacent nodes and move one coin from one node to another. A move may be from parent to child, or from child to parent.

Return the minimum number of moves required to make every node have exactly one coin.

Example1:   
Input: root = [3,0,0]
Output: 2
Explanation: From the root of the tree, we move one coin to its left child, and one coin to its right child.

Example2:
Input: root = [0,3,0]
Output: 3
Explanation: From the left child of the root, we move two coins to the root [taking two moves]. Then, we move one coin from the root of the tree to the right child.

Constraints:
The number of coins in the tree is n.
1 <= n <= 100
0 <= Node.val <= n
The sum of all Node.val is n.
"""

"""
Note:
1. DFS (PostOrder Traversal): O(n) time | O(h) space
return the number of coins given to the parent

2. DFS with preNode (PostOrder Traversal): O(n) time | o(h) space
give the parent node so we can move the coins to the parent directly
"""

from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        container = [0]
        def dfs(root, container):
            if not root:
                return 0
            left, right = dfs(root.left, container), dfs(root.right, container)
            container[0] += abs(left) + abs(right)
            return root.val + left + right - 1
        dfs(root, container)
        return container[0]

    def distributeCoins2(self, root: Optional[TreeNode]) -> int:
        preNode = None
        def dfs(root, preNode):
            if not root:
                return 0
            left, right = dfs(root.left, root), dfs(root.right, root)
            if preNode:
                preNode.val += (root.val - 1)
            return left + right + abs(root.val - 1)
        return dfs(root, preNode)

# Unit Tests
import unittest
funcs = [Solution().distributeCoins, Solution().distributeCoins2]


class TestDistributeCoins(unittest.TestCase):
    def testDistributeCoins1(self):
        for func in funcs:
            root = TreeNode(3, TreeNode(0), TreeNode(0))
            self.assertEqual(func(root=root), 2)

    def testDistributeCoins2(self):
        for func in funcs:
            root = TreeNode(0, TreeNode(3), TreeNode(0))
            self.assertEqual(func(root=root), 3)

if __name__ == "__main__":
    unittest.main()
