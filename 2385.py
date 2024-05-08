
"""
2385. Amount of Time for Binary Tree to Be Infected
description: https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/description/
"""

"""
Note:
1. BFS (layer order traversal): O(n) time | O(n) space - where n is the number of nodes in tree
"""

from typing import Optional
import collections
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        graph = collections.defaultdict(list)
        stack = [root]
        while stack:
            current = stack.pop()
            if current.right:
                graph[current.val].append(current.right.val)
                graph[current.right.val].append(current.val)
                stack.append(current.right)
            if current.left:
                graph[current.val].append(current.left.val)
                graph[current.left.val].append(current.val)
                stack.append(current.left)            

        visited = set([start])
        currentNodes = [start]
        minutes = -1
        while currentNodes:
            nextNodes = []
            for node in currentNodes:
                for neighbor in graph[node]:
                    if neighbor in visited:
                        continue
                    visited.add(neighbor)
                    nextNodes.append(neighbor)
            currentNodes = nextNodes
            minutes += 1
        return minutes

# Unit Tests
import unittest
funcs = [Solution().amountOfTime]

class TestAmountOfTime(unittest.TestCase):
    def testAmountOfTime1(self):
        for amountOfTime in funcs:
            root = TreeNode(1, TreeNode(5, None, TreeNode(4, TreeNode(9), TreeNode(2))), TreeNode(3, TreeNode(10), TreeNode(6)))
            start = 3
            self.assertEqual(amountOfTime(root=root, start=start), 4)


    def testAmountOfTime2(self):
        for amountOfTime in funcs:
            root = TreeNode(1)
            start = 1
            self.assertEqual(amountOfTime(root=root, start=start), 0)

if __name__ == "__main__":
    unittest.main()