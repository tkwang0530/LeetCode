"""
1530. Number of Good Leaf Nodes Pairs
description: https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/description/
"""

"""
Note:
1. DFS (PostOrder Traversal): O(distance^2 * n) time | O(distance * h) space - where n is the number of nodes, h is the height of the tree
2 BFS (LayerOrder Traversal): O(distance^2 * n) time | O(n) space - where n is the number of nodes
"""

from typing import List
import collections
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        container = [0]
        def dfs(root, container) -> List[int]:
            arr = [0] * (distance+1)
            if not root:
                return arr

            if not root.left and not root.right:
                arr[0] = 1
                return arr
            
            left = dfs(root.left, container)
            right = dfs(root.right, container)
            for disL in range(distance): # 0 ~ distance-1
                for disR in range(distance):
                    if (disL+1) + (disR+1) <= distance:
                        container[0] += left[disL]*right[disR]
            
            # shift by 1
            # arr[i+1] = left[i]+right[i]
            for i in range(distance):
                arr[i+1] = left[i]+right[i]
            
            return arr
        
        dfs(root, container)
        return container[0]

class Solution2:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        graph = collections.defaultdict(list)

        def findLeaves(node):
            if not node.left and not node.right:
                leaves.append(node)
            
            if node.left:
                findLeaves(node.left)
                graph[node].append(node.left)
                graph[node.left].append(node)

            if node.right:
                findLeaves(node.right)
                graph[node].append(node.right)
                graph[node.right].append(node)

        def bfs(start):
            currentNodes = [(start, None)]
            
            goods = 0
            steps = 0
            while currentNodes and steps <= distance:
                nextNodes = []
                for node, prev in currentNodes:
                    if not node.left and not node.right and steps > 0:
                        goods += 1
                    for neighbor in graph[node]:
                        if neighbor == prev:
                            continue
                        nextNodes.append((neighbor, node))
                
                currentNodes = nextNodes
                steps += 1
            return goods
        
        leaves = []
        findLeaves(root)
        total = 0
        for leaf in leaves:
            total += bfs(leaf)

        return total // 2
# Unit Tests
import unittest
funcs = [Solution().countPairs, Solution2().countPairs]
class TestCountPairs(unittest.TestCase):
    def testCountPairs1(self):
        for func in funcs:
            root = TreeNode(1, TreeNode(2, None, TreeNode(4)), TreeNode(3))
            distance = 3
            self.assertEqual(func(root=root, distance=distance), 1)

    def testCountPairs2(self):
        for func in funcs:
            root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
            distance = 3
            self.assertEqual(func(root=root, distance=distance), 2)

    def testCountPairs3(self):
        for func in funcs:
            root = TreeNode(7, TreeNode(1, TreeNode(6), None), TreeNode(4, TreeNode(5), TreeNode(3, None, TreeNode(2))), )
            distance = 3
            self.assertEqual(func(root=root, distance=distance), 1)

if __name__ == "__main__":
    unittest.main()
