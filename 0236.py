"""
236. Lowest Common Ancestor of a Binary Tree
description: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/
"""

"""
Note:
1. DFS (postOrder Traversal): O(n) time | O(h) space - where n is the number of nodes in the tree and h is the height of the tree
2. iterative solution: O(n) time | O(n) space - where n is the number of nodes in the tree and h is the height of the tree
(1) traverse the entire tree and build a parent dictionary (node -> node's parent)
(2) build the p's ancestor set, which contains all the nodes that include p
(3) using the parent dict and ancestor set, move q upward until q exists in p's ancestor set
"""




import unittest
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root):
            if not root:
                return None

            if root in (p, q):
                return root

            left = dfs(root.left)
            right = dfs(root.right)
            return root if left and right else left or right

        return dfs(root)
class Solution2:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        stack = [root]
        parent = { root: None}
        # build the parent dictionary
        while p not in parent or q not in parent:
            node = stack.pop()
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)

        # build p ancestors set (like a path from p to root)
        ancestors = set()
        while p:
            ancestors.add(p)
            p = parent[p]

        # move q up until q in ancestors set
        while q not in ancestors:
            q = parent[q]
        return q

# Unit Tests
funcs = [Solution().lowestCommonAncestor, Solution2().lowestCommonAncestor]


class TestLowestCommonAncestor(unittest.TestCase):
    def testLowestCommonAncestor1(self):
        for func in funcs:
            p = TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4)))
            q = TreeNode(1, TreeNode(0), TreeNode(8))
            root = TreeNode(3, p, q)
            self.assertEqual(func(root=root, p=p, q=q), root)

    def testLowestCommonAncestor2(self):
        for func in funcs:
            q = TreeNode(4)
            expectLca = p = TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), q))
            root = TreeNode(3, p, TreeNode(1, TreeNode(0), TreeNode(8)))
            self.assertEqual(func(root=root, p=p, q=q), expectLca)

    def testLowestCommonAncestor3(self):
        for func in funcs:
            q = TreeNode(2)
            expectLca = root = p = TreeNode(1, q)
            self.assertEqual(func(root=root, p=p, q=q), expectLca)


if __name__ == "__main__":
    unittest.main()
