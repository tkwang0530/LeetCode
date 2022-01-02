"""
366. Find Leaves of Binary Tree
Given the root of a binary tree, collect a tree's nodes as if you were doing this:
- Collect all the leaf nodes.
- Remove all the leaf nodes.
- Repeat until the tree is empty

Example1:
Input: root = [1,2,3,4,5]
Output: [[4,5,3],[2],[1]]
Explanation:
[[3,5,4],[2],[1]] and [[3,4,5],[2],[1]] are also considered correct answers since per each level it does not matter the order on which elements are returned.

Example2:
Input: root = [1]
Output: [[1]]

Constraints:
The number of nodes in the tree is in the range [1, 100].
-100 <= Node.val <= 100
"""

"""
Note:
1. Preorder Traversal + HashMap: O(n) time | O(n) space
"""



from typing import Optional, List
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        # nodeChildren: <node, set<ListNode>>
        stack = [root]
        nodeChildren = collections.defaultdict(set)
        nodeParent = {root: None}
        leaves = []
        while stack:
            node = stack.pop()
            if node.right:
                nodeChildren[node].add(node.right)
                stack.append(node.right)
                nodeParent[node.right] = node
            if node.left:
                nodeChildren[node].add(node.left)
                stack.append(node.left)
                nodeParent[node.left] = node
            if not node.left and not node.right:
                leaves.append(node)
        
        result = []
        while leaves:
            nextLeaveSet = set()
            leaveValArr = []
            for leaveNode in leaves:
                parentNode = nodeParent[leaveNode]
                if parentNode:
                    nodeChildren[parentNode].remove(leaveNode)
                    if len(nodeChildren[parentNode]) == 0:
                        nextLeaveSet.add(parentNode)
                leaveValArr.append(leaveNode.val)
                
            result.append(leaveValArr)
            leaves = list(nextLeaveSet)
        return result

# Unit Tests
import unittest
funcs = [Solution().findLeaves]


class TestFindLeaves(unittest.TestCase):
    def testFindLeaves1(self):
        for func in funcs:
            root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
            self.assertEqual(func(root=root), [[4,5,3],[2],[1]])

    def testFindLeaves2(self):
        for func in funcs:
            root = TreeNode(1)
            self.assertEqual(func(root=root), [[1]])


if __name__ == "__main__":
    unittest.main()
