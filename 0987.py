"""
987. Vertical Order Traversal of a Binary Tree
description: https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/description/
"""

"""
Note:
1. BFS + HashMap + Sort: O(nlogn) time | O(n) - where n is the number of nodes in the tree
2. BFS (layerOrder Traversal) + HashMap: O(n) time | O(n) space - where n is the number of nodes in the tree
"""

from typing import List, Optional
import unittest, collections
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        result = []
        dict = collections.defaultdict(list)
        if not root:
            return result
        queue = collections.deque([(root, 0, 0)])
        while queue:
            node, row, col = queue.popleft()
            dict[col].append((row, node.val))
            if node.left:
                queue.append((node.left, row + 1, col - 1))
            if node.right:
                queue.append((node.right, row + 1, col + 1))
        for col in sorted(dict):
            temp = []
            for item in sorted(dict[col]):
                temp.append(item[1])
            result.append(temp)
        return result

class Solution2:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        table = [[] for _ in range(1999)]
        currentItems = [(root, 0)]

        def getIdx(pos: int) -> int:
            return pos+999

        while currentItems:
            nextItems = []
            tempTable = collections.defaultdict(list)
            for node, pos in currentItems:
                tempTable[getIdx(pos)].append(node.val)
                if node.left:
                    nextItems.append((node.left, pos-1))
                if node.right:
                    nextItems.append((node.right, pos+1))
            for pos, arr in tempTable.items():
                table[pos].extend(sorted(arr))
            currentItems = nextItems
        output = []
        for arr in table:
            if not arr:
                continue
            output.append(arr)
        return output

# Unit Tests
funcs = [Solution().verticalTraversal, Solution2().verticalTraversal]


class TestVerticalTraversal(unittest.TestCase):
    def testVerticalTraversal1(self):
        for func in funcs:
            root = TreeNode(3, TreeNode(9), TreeNode(
                20, TreeNode(15), TreeNode(7)))
            self.assertEqual(func(root=root), [[9], [3, 15], [20], [7]])

    def testVerticalTraversal2(self):
        for func in funcs:
            root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(
                5)), TreeNode(3, TreeNode(6), TreeNode(7)))
            self.assertEqual(func(root=root), [[4], [2], [1, 5, 6], [3], [7]])

    def testVerticalTraversal3(self):
        for func in funcs:
            root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(
                6)), TreeNode(3, TreeNode(5), TreeNode(7)))
            self.assertEqual(func(root=root), [[4], [2], [1, 5, 6], [3], [7]])


if __name__ == "__main__":
    unittest.main()
