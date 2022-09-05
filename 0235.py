"""
235. Lowest Common Ancestor of a Binary Search Tree
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: "The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself)."

Example1:   
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

Example2:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

Example3:
Input: root = [2,1], p = 2, q = 1
Output: 2
"""

"""
Note:
1. Recursive DFS (Bottom-up): O(n) time | O(n) space - where n is the number of nodes in the tree
"""




import unittest
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        container = []
        nodeSet = {p, q}

        def dfs(node, p, q, container):
            score = 0
            if node in nodeSet:
                score += 1
            if node.left:
                score += dfs(node.left, p, q, container)
            if node.right:
                score += dfs(node.right, p, q, container)
            if score == 2 and not container:
                container.append(node)
            return score
        dfs(root, p, q, container)
        return container[0]


# Unit Tests
funcs = [Solution().lowestCommonAncestor]


class TestLowestCommonAncestor(unittest.TestCase):
    def testLowestCommonAncestor1(self):
        for func in funcs:
            root = node6 = TreeNode(6)
            node2 = TreeNode(2)
            node8 = TreeNode(8)
            node0 = TreeNode(0)
            node4 = TreeNode(4)
            node7 = TreeNode(7)
            node9 = TreeNode(9)
            node3 = TreeNode(3)
            node5 = TreeNode(5)

            node6.left, node6.right = node2, node8
            node2.left, node2.right = node0, node4
            node8.left, node8.right = node7, node9
            node4.left, node4.right = node3, node5
            self.assertEqual(func(root=root, p=node2, q=node4), node2)

    def testLowestCommonAncestor2(self):
        for func in funcs:
            root = node2 = TreeNode(2)
            node1 = TreeNode(1)
            node2.left = node1
            self.assertEqual(func(root=root, p=node2, q=node1), node2)


if __name__ == "__main__":
    unittest.main()
