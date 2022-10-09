"""
100. Same Tree
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Example1:   
Input: p = [1,2,3], q = [1,2,3]
Output: true

Example2:
Input: p = [1,2], q = [1,null,2]
Output: false

Example3:
Input: p = [1,2,1], q = [1,1,2]
Output: false
"""

"""
Note:
1. Recursion: O(n) time | O(n) space
2. Iteration (DFS PreOrder Traversal): O(n) time | O(n) space
3. Iteration (BFS) : O(n) time | O(n) space
"""




from collections import deque
import unittest
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        return all((p.val == q.val, self.isSameTree(p.left, q.left), self.isSameTree(p.right, q.right)))

    # DFS with stack
    def isSameTree2(self, p: TreeNode, q: TreeNode) -> bool:
        stack = [(p, q)]
        while stack:
            node1, node2 = stack.pop()
            if not node1 and not node2:
                continue
            elif None in [node1, node2]:
                return False
            else:
                if node1.val != node2.val:
                    return False
                stack.append((node1.right, node2.right))
                stack.append((node1.left, node2.left))
        return True

    # BFS with queue
    def isSameTree3(self, p: TreeNode, q: TreeNode) -> bool:
        queue = deque([(p, q)])
        while queue:
            node1, node2 = queue.popleft()
            if not node1 and not node2:
                continue
            elif None in [node1, node2]:
                return False
            else:
                if node1.val != node2.val:
                    return False
                queue.append((node1.left, node2.left))
                queue.append((node1.right, node2.right))
        return True


# Unit Tests
funcs = [Solution().isSameTree, Solution().isSameTree2, Solution().isSameTree3]


class TestIsSameTree(unittest.TestCase):
    def testIsSameTree1(self):
        for func in funcs:
            p = TreeNode(1, TreeNode(2), TreeNode(3))
            q = TreeNode(1, TreeNode(2), TreeNode(3))
            self.assertEqual(func(p=p, q=q), True)

    def testIsSameTree2(self):
        for func in funcs:
            p = TreeNode(1, TreeNode(2))
            q = TreeNode(1, None, TreeNode(2))
            self.assertEqual(func(p=p, q=q), False)

    def testIsSameTree3(self):
        for func in funcs:
            p = TreeNode(1, TreeNode(2), TreeNode(1))
            q = TreeNode(1, TreeNode(1), TreeNode(2))
            self.assertEqual(func(p=p, q=q), False)


if __name__ == "__main__":
    unittest.main()
