"""
1650. Lowest Common Ancestor of a Binary Tree III
Given two nodes of a binary tree p and q, return their lowest common ancestor (LCA).

Each node will have a reference to its parent node. The definition for Node is below:
class Node {
    public int val;
    public Node left;
    public Node right;
    public Node parent;
}

According to the definition of LCA on Wikipedia: "The lowest common ancestor of two nodes p and q in a tree T is the lowest node that has both p and q as descendants (where we allow a node to be a descendant of itself)."

Example1:
                3
             /      \
           5         1
        /     \      /   \
      6      2    0    8
             /  \
           7    4       
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Example2:
                3
             /      \
           5         1
        /     \      /   \
      6      2    0    8
             /  \
           7    4       
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 3
Explanation: The LCA of nodes 5 and 4 is 5 since a node can be a descendant of itself according to the LCA definition.

Example3:
Input: root = [1, 2], p = 1, q = 2
Output: 1

Constraints:
The number of nodes in the tree is in the range [2, 10^5]
-10^9 <= Node.val <= 10^9
All Node.val are unique.
p != q
p and q exist in the tree.
"""

"""
Note:
1. Two Pointers: O(n) time | O(1) space
one pointer start from p and the other start from q
move to each parent until they meet
if pointerP is None: pointerP = q
if pointerQ is None: pointerQ = p
"""


import unittest
class Node:
    def __init__(self, val=0, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent


class Solution:
    def lowestCommonAncestor(self, p: Node, q: Node) -> Node:
        pointerP = p
        pointerQ = q
        while pointerP != pointerQ:
            pointerP = pointerP.parent
            pointerQ = pointerQ.parent
            if not pointerP:
                pointerP = q
            elif not pointerQ:
                pointerQ = p
        return pointerP
        

# Unit Tests
funcs = [Solution().lowestCommonAncestor]


class TestLowestCommonAncestor(unittest.TestCase):
    def testLowestCommonAncestor1(self):
        for func in funcs:
            node0 = Node(0)
            q =node1 = Node(1)
            node2 = Node(2)
            node3 = Node(3)
            node4= Node(4)
            p = node5 = Node(5)
            node6 = Node(6)
            node7 = Node(7)
            node8 = Node(8)

            node3.left, node3.right, node3.parent = node5, node1, None
            node5.left, node5.right, node5.parent = node6, node2, node3
            node1.left, node1.right, node1.parent = node0, node8, node3
            node6.left, node6.right, node6.parent = None, None, node5
            node2.left, node2.right, node2.parent = node7, node4, node5
            node0.left, node0.right, node0.parent = None, None, node1
            node8.left, node8.right, node8.parent = None, None, node1
            node7.left, node7.right, node7.parent = None, None, node2
            node4.left, node4.right, node4.parent = None, None, node2

            self.assertEqual(func(p=p, q=q), node3)

    def testLowestCommonAncestor2(self):
        for func in funcs:
            node0 = Node(0)
            node1 = Node(1)
            node2 = Node(2)
            node3 = Node(3)
            q = node4= Node(4)
            p = node5 = Node(5)
            node6 = Node(6)
            node7 = Node(7)
            node8 = Node(8)

            node3.left, node3.right, node3.parent = node5, node1, None
            node5.left, node5.right, node5.parent = node6, node2, node3
            node1.left, node1.right, node1.parent = node0, node8, node3
            node6.left, node6.right, node6.parent = None, None, node5
            node2.left, node2.right, node2.parent = node7, node4, node5
            node0.left, node0.right, node0.parent = None, None, node1
            node8.left, node8.right, node8.parent = None, None, node1
            node7.left, node7.right, node7.parent = None, None, node2
            node4.left, node4.right, node4.parent = None, None, node2

            self.assertEqual(func(p=p, q=q), node5)

    def testLowestCommonAncestor1(self):
        for func in funcs:
            p = node1 = Node(1)
            q= node2 = Node(2)
            node1.left, node1.right, node1.parent = None, node2, None
            node2.left, node2.right, node2.parent = None, None, node1

            self.assertEqual(func(p=p, q=q), node1)



if __name__ == "__main__":
    unittest.main()
