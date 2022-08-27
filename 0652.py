"""
652. Find Duplicate Subtrees
Given the root of a binary tree, return all duplicate subtrees.
For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with the same node values.

Example1:
Input: root = [1,2,3,4,null,2,4,null,null,4]
Output: [[2,4],[4]]

Example2:
Input: root = [2,1,1]
Output: [[1]]

Example3:
Input: root = [2,2,2,3,null,3,null]
Output: [[2,3],[3]]

Constraints:
The number of the nodes in the tree will be in the range [1, 10^4]
-200 <= Node.val <= 200
"""

"""
Note:
1. DFS + Serialization: O(n) time | O(n) space - where n is the number of nodes in the tree
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List, Optional
import collections
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        serialCount = collections.defaultdict(int)
        result = []
        def serialize(root):
            if not root:
                return "null"
            serial = str(root.val) + ";" + serialize(root.left) + ";" + serialize(root.right)
            serialCount[serial] += 1
            if serialCount[serial] == 2:
                result.append(root)
            return serial
        serialize(root)
        return result

# Unit Tests
import unittest
funcs = [Solution().findDuplicateSubtrees]
class TestfindDuplicateSubtrees(unittest.TestCase):
    def testfindDuplicateSubtrees1(self):
        for func in funcs:
            node1 = TreeNode(1)
            node2 = TreeNode(2)
            node3 = TreeNode(3)
            node4 = TreeNode(4)
            node5 = TreeNode(2)
            node6 = TreeNode(4)
            node7 = TreeNode(4)
            node1.left, node1.right = node2, node3
            node2.left = node4
            node3.left, node3.right = node5, node6
            node5.left = node7
            self.assertEqual(func(node1), [node7, node5])

    def testfindDuplicateSubtrees2(self):
        for func in funcs:
            node1 = TreeNode(2)
            node2 = TreeNode(1)
            node3 = TreeNode(1)
            node1.left, node1.right = node2, node3
            self.assertEqual(func(node1), [node3])

    def testfindDuplicateSubtrees3(self):
        for func in funcs:
            node1 = TreeNode(2)
            node2 = TreeNode(2)
            node3 = TreeNode(2)
            node4 = TreeNode(3)
            node5 = TreeNode(3)
            node1.left, node1.right = node2, node3
            node2.left = node4
            node3.left = node5
            self.assertEqual(func(node1), [node5, node3])

if __name__ == "__main__":
    unittest.main()
