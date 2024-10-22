"""
2583. Kth Largest Sum in a Binary Tree
description: https://leetcode.com/problems/kth-largest-sum-in-a-binary-tree/description/ 
"""

"""
Note:
1. minHeap: O(nlogk) time | O(n+k) space - where n is the number of nodes in the tree
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import heapq
from typing import Optional
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        minHeap = []
        currentLayer = [root]
        while currentLayer:
            nextLayer = []
            levelSum = 0
            for node in currentLayer:
                levelSum += node.val
                if node.left:
                    nextLayer.append(node.left)
                if node.right:
                    nextLayer.append(node.right)
            
            if len(minHeap) < k:
                heapq.heappush(minHeap, levelSum)
            else:
                heapq.heappushpop(minHeap, levelSum)
            
            currentLayer = nextLayer

        return minHeap[0] if len(minHeap) == k else -1


import unittest
funcs = [Solution().kthLargestLevelSum]
class TestKthLargestLevelSum(unittest.TestCase):
    def testKthLargestLevelSum1(self):
        for func in funcs:
            root = TreeNode(5, TreeNode(8, TreeNode(2, TreeNode(4), TreeNode(6)), TreeNode(1)), TreeNode(9, TreeNode(3), TreeNode(7)))
            k = 2
            self.assertEqual(func(root=root, k=k), 13)

    def testKthLargestLevelSum2(self):
        for func in funcs:
            root = TreeNode(1, TreeNode(2, TreeNode(3), None), None)
            k = 1
            self.assertEqual(func(root=root, k=k), 3)

if __name__ == "__main__":
    unittest.main()
