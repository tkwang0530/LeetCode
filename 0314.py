"""
314. Binary Tree Vertical Order Traversal
description: https://leetcode.com/problems/binary-tree-vertical-order-traversal/description/
"""

"""
Note:
1. BFS (layerOrder Traversal) + HashMap: O(199) time | O(199) space
"""

from typing import List, Optional
import unittest
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        table = [[] for _ in range(199)]

        def getIdx(pos: int) -> int:
            return pos+99

        currentItems = [(root, 0)]
        while currentItems:
            nextItems = []
            for node, pos in currentItems:
                table[getIdx(pos)].append(node.val)
                if node.left:
                    nextItems.append((node.left, pos-1))
                if node.right:
                    nextItems.append((node.right, pos+1))
            currentItems = nextItems

        output = []
        for arr in table:
            if not arr:
                continue
            output.append(arr)
        return output

# Unit Tests
funcs = [Solution().verticalOrder]


class TestVerticalOrder(unittest.TestCase):
    def testVerticalOrder1(self):
        for verticalOrder in funcs:
            root = TreeNode(3, TreeNode(9), TreeNode(
                20, TreeNode(15), TreeNode(7)))
            self.assertEqual(verticalOrder(root=root), [[9], [3, 15], [20], [7]])

    def testVerticalOrder2(self):
        for verticalOrder in funcs:
            root = TreeNode(3, TreeNode(9, TreeNode(4), TreeNode(0)), TreeNode(8, TreeNode(1), TreeNode(7)))
            self.assertEqual(verticalOrder(root=root), [[4],[9],[3,0,1],[8],[7]])

    def testVerticalOrder3(self):
        for verticalOrder in funcs:
            root = TreeNode(3, TreeNode(9, TreeNode(4), TreeNode(0, None, TreeNode(2))), TreeNode(8, TreeNode(1, TreeNode(5)), TreeNode(7)))
            self.assertEqual(verticalOrder(root=root), [[4],[9,5],[3,0,1],[8,2],[7]])


if __name__ == "__main__":
    unittest.main()
