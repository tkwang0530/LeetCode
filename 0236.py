"""
236. Lowest Common Ancestor of a Binary Tree
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: "The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself)."

Example1:
Input: root = [3, 5, 1, 6, 2, 0, 8, null, null, 7 ,4], p = 5, q = 1
            3
         /      \
      5          1
    /   \        /   \
 6     2     0      8
      /   \
    7      4

Output: 3

Example2:
Input: root = [3, 5, 1, 6, 2, 0, 8, null, null, 7 ,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

Example3:
Input: root = [1, 2], p = 1, q = 2
Output: 1

Constraints:
All Node.val are unique
p != q
p and q will exist in the tree.
"""

"""
Note:
1. recursive solution (stop at None): O(n) time | O(n) space
3 cases
If the current (sub)tree contains both p and q, then the function result is their LCA. 
If only one of them is in that subtree, then the result is that one of them. 
If neither are in that subtree, the result is null/None/nil.
2. iterative solution: O(n) time | O(n) space
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
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root in (None, p, q):
            return root
        lcaFromLeft = self.lowestCommonAncestor(root.left, p, q)
        lcaFromRight = self.lowestCommonAncestor(root.right, p, q)
        return root if lcaFromLeft and lcaFromRight else lcaFromLeft or lcaFromRight

    def lowestCommonAncestor2(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
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
funcs = [Solution().lowestCommonAncestor, Solution().lowestCommonAncestor2]


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
