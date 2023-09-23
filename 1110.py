"""
1110. Delete Nodes And Return Forest
description: https://leetcode.com/problems/delete-nodes-and-return-forest/description/
"""

"""
Note:
1. DFS (PostOrder Traversal) + HashTable: O(n) time | O(n+h) space - where n is the number of nodes, h is the height of the tree
ref: https://leetcode.com/problems/delete-nodes-and-return-forest/solutions/328853/java-c-python-recursion-solution/
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
        output = []
        def dfs(root, hasParent):
            if not root:
                return None

            rootDeleted = root.val in toDeleteSet
            if not hasParent and not rootDeleted:
                output.append(root)
            
            root.left = dfs(root.left, not rootDeleted)
            root.right = dfs(root.right, not rootDeleted)
            return None if rootDeleted else root

        dfs(root, False)
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
