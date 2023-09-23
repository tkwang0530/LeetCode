"""
863. All Nodes Distance K in Binary Tree
description: https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/description/
"""

"""
Note:
1. Build Graph + BFS: O(n) time | O(n) space - where n is the number of nodes in the tree
"""


from typing import List
import collections
import unittest
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not root:
            return []
    
        graph = collections.defaultdict(list)
        def buildGraph(root, parent):
            if not root:
                return
            
            if parent:
                graph[root].append(parent)

            if root.left:
                graph[root].append(root.left)
                buildGraph(root.left, root)

            if root.right:
                graph[root].append(root.right)
                buildGraph(root.right, root)

        buildGraph(root, None)

        currentNodes = [target]
        distance = 0
        visited = set(currentNodes)
        output = []
        while currentNodes:
            nextNodes = []
            for node in currentNodes:
                if distance == k:
                    output.append(node.val)
                    continue
                
                for neighbor in graph[node]:
                    if neighbor in visited:
                        continue
                    visited.add(neighbor)
                    nextNodes.append(neighbor)
            
            if distance == k:
                break

            currentNodes = nextNodes
            distance += 1

        return output


# Unit Tests
funcs = [Solution().distanceK]


class TestDistanceK(unittest.TestCase):
    def testDistanceK1(self):
        for distanceK in funcs:
            target = TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4)))
            root = TreeNode(3, target, TreeNode(1, TreeNode(0), TreeNode(8)))
            k = 2
            self.assertEqual(sorted(distanceK(root=root, target=target, k=k)), sorted([7, 4, 1]))

    def testDistanceK2(self):
        for distanceK in funcs:
            target = root = TreeNode(1)
            k = 3
            self.assertEqual(sorted(distanceK(root=root, target=target, k=k)), sorted([]))


if __name__ == "__main__":
    unittest.main()
