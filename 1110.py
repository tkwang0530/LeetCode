"""
1110. Delete Nodes And Return Forest
description: https://leetcode.com/problems/delete-nodes-and-return-forest/description/
"""

"""
Note:
1. DFS (PostOrder Traversal Twice) + HashTable: O(n) time | O(n+h) space - where n is the number of nodes, h is the height of the tree
"""

from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        toDeleteSet = set(to_delete)
        parents = {root.val: -1}
        valueToNode = {}
        def dfs(root):
            if not root:
                return
            
            valueToNode[root.val] = root
            if root.left:
                parents[root.left.val] = root.val
                dfs(root.left)
            
            if root.right:
                parents[root.right.val] = root.val
                dfs(root.right)
        
        dfs(root)

        def removeNodesHelper(root):
            if not root:
                return

            if root.left:
                removeNodesHelper(root.left)

            if root.right:
                removeNodesHelper(root.right)

            if root.val in toDeleteSet:
                if root.left:
                    parents[root.left.val] = -1
                if root.right:
                    parents[root.right.val] = -1
                
                root.left = None
                root.right = None

                if parents[root.val] != -1:
                    parent = valueToNode[parents[root.val]]
                    if parent.left == root:
                        parent.left = None
                    elif parent.right == root:
                        parent.right = None
        removeNodesHelper(root)

        output = []
        for nodeVal, parentVal in parents.items():
            if parentVal == -1 and nodeVal not in toDeleteSet:
                output.append(valueToNode[nodeVal])

        return output

# Unit Tests
import unittest
funcs = [Solution().delNodes]
class TestDelNodes(unittest.TestCase):
    def testDelNodes1(self):
        for delNodes in funcs:
            node6 = TreeNode(6)
            node7 = TreeNode(7)
            root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, node6, node7))
            to_delete = [3,5]
            self.assertEqual(delNodes(root=root, to_delete=to_delete), [root, node6, node7])

    def testDelNodes2(self):
        for delNodes in funcs:
            root = TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(4))
            to_delete = [3]
            self.assertEqual(delNodes(root=root, to_delete=to_delete), [root])

if __name__ == "__main__":
    unittest.main()
