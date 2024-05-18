"""
979. Distribute Coins in Binary Tree
description: https://leetcode.com/problems/distribute-coins-in-binary-tree/description/
"""

"""
Note:
1. DFS (PostOrder Traversal): O(n) time | O(h) space
return the number of coins given to the parent

2. DFS with preNode (PostOrder Traversal): O(n) time | o(h) space
give the parent node so we can move the coins to the parent directly

3. DFS (PostOrder Traversal): O(n) time | O(h) space
"""

from typing import Optional, Tuple
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

class Solution2:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        preNode = None
        def dfs(root, preNode):
            if not root:
                return 0
            left, right = dfs(root.left, root), dfs(root.right, root)
            if preNode:
                preNode.val += (root.val - 1)
            return left + right + abs(root.val - 1)
        return dfs(root, preNode)
    
class Solution3:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        def dfs(node) -> Tuple[int, int]: # subtree sum, number of nodes, moves
            if not node.left and not node.right:
                return node.val, 1, abs(node.val-1)

            subtreeSum = node.val
            moves = 0
            count = 1
            if node.left:
                val, c, subMoves = dfs(node.left)
                subtreeSum += val
                count += c
                moves += subMoves
            
            if node.right:
                val, c, subMoves = dfs(node.right)
                subtreeSum += val
                count += c
                moves += subMoves

            return subtreeSum, count, abs(subtreeSum-count)+moves
        return dfs(root)[2]

# Unit Tests
import unittest
funcs = [Solution().distributeCoins, Solution2().distributeCoins, Solution3().distributeCoins]


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
