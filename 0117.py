"""
117. Populating Next Right Pointers in Each Node II
Given a  binary tree
struct Node {
    int val;
    Node *left;
    Node *right;
    Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
Initially, all next pointers are set to NULL.

Example1:
Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]
Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.

Example2:
Input: root = []
Output: []
"""

"""
Note:
1. Iteration (BFS): O(n) time | O(n) space
keep track the startNode
2. Iteration: O(n) time | O(1) space
using dummy node in each level
"""

from collections import deque
import unittest
class Node:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Node) -> Node:
        if not root:
            return root
        queue = deque([root])
        while queue:
            queueLength = len(queue)
            for i in range(queueLength):
                node = queue.popleft()
                if i < queueLength - 1:
                    node.next = queue[0]
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root

    def connect2(self, root: Node) -> Node:
        if not root:
            return root
        next = dummy = Node(0)
        startNode = root
        while startNode:
            current = startNode
            
            # while current level pointer is not None
            while current:
                # if current Level Pointer has left child, next Level Pointer points to it and move forward
                if current.left:
                    next.next = current.left
                    next = next.next
                # if current Level Pointer has right child, next Level Pointer points to it and move forward
                if current.right:
                    next.next = current.right
                    next = next.next
                # current move forward
                current = current.next
            # change startNode to the start of the next level
            startNode = dummy.next
            
            # cut down the dummy.next because we will reuse the dummy node in the next run
            dummy.next = None
            next = dummy
        return root



    

# Unit Tests
funcs = [Solution().connect, Solution().connect2]


class TestConnect(unittest.TestCase):
    def testConnect1(self):
        for func in funcs:
            root = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))
            root = func(root)
            self.assertEqual(root.next, None)
            self.assertEqual(root.left.next, root.right)
            self.assertEqual(root.right.next, None)
            self.assertEqual(root.left.left.next, root.left.right)
            self.assertEqual(root.left.right.next, root.right.left)
            self.assertEqual(root.right.left.next, root.right.right)
            self.assertEqual(root.right.right.next, None)

    def testConnect2(self):
        for func in funcs:
            root = None
            root = func(root)
            self.assertEqual(root, None)

if __name__ == "__main__":
    unittest.main()
