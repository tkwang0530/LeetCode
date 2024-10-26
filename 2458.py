"""
2458. Height of Binary Tree After Subtree Removal Queries
description: https://leetcode.com/problems/height-of-binary-tree-after-subtree-removal-queries/description/ 
"""

"""
Note:
1. dfs (Post Order Traversal): O(n) time | O(n) space - where n is the number of nodes in the tree
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import collections
from typing import Optional, List

from sortedcontainers import SortedList
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        nodeLevelMap = {} # <node.val, level>
        nodeHeightMap = {} # <node.val, height>
        levelTreeMap = collections.defaultdict(SortedList)
        # dfs(node, level) returns the height of specific node
        def dfs(node, level) -> int:
            nodeLevelMap[node.val] = level
            height = level
            if node.left:
                height = max(height, dfs(node.left, level+1))
            
            if node.right:
                height = max(height, dfs(node.right, level+1))

            levelTreeMap[level].add(height)
            nodeHeightMap[node.val] = height
            return height

        dfs(root, 0)

        output = []
        for removeNodeVal in queries:
            level = nodeLevelMap[removeNodeVal]
            height = nodeHeightMap[removeNodeVal]
            levelTreeMap[level].remove(height)
            if not levelTreeMap[level]:
                output.append(level-1)
            else:
                output.append(levelTreeMap[level][-1])
            
            levelTreeMap[level].add(height)

        return output

import unittest
funcs = [Solution().treeQueries]
class TestTreeQueries(unittest.TestCase):
    def testTreeQueries1(self):
        for func in funcs:
            root = TreeNode(1, TreeNode(3, TreeNode(2)), TreeNode(4, TreeNode(6), TreeNode(5, None, TreeNode(7))))
            queries = [4]
            self.assertEqual(func(root=root, queries=queries), [2])

    def testTreeQueries2(self):
        for func in funcs:
            root = TreeNode(5, TreeNode(8, TreeNode(2, TreeNode(4), TreeNode(6)), TreeNode(1)), TreeNode(9, TreeNode(3), TreeNode(7)))
            queries = [3,2,4,8]
            self.assertEqual(func(root=root, queries=queries), [3,2,3,2])

if __name__ == "__main__":
    unittest.main()
