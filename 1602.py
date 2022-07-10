"""
1602. Find Nearest Right Node in Binary Tree
Given the root of a binary tree and a node u in the tree, return the nearest node on the same level that is to the right of u, or return null if u is the rightmost node in its level.

Example1:   
Input: root = [1,2,3,null,4,5,6], u = 4
Output: 5
Explanation: The nearest node on the same level to the right of node 4 is node 5.

Example2:
Input: root = [3,null,4,2], u = 2
Output: null
Explanation: There are no nodes to the right of 2.

Constraints:
The number of nodes in the tree is in the range [1, 10^5].
1 <= Node.val <= 10^5
All Node.val are distinct.
u is a node in the binary tree rooted at root.
"""

"""
Note:
1. BFS: O(n) time | O(n) space - where n is the number of nodes in the tree
2. DFS: O(n) time | O(h) space - where n is the number of nodes and h is the height of the tree
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import collections
from typing import Optional
class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> Optional[TreeNode]:
        queue = collections.deque([(root, 0)])
        hasFound = False
        uLevel = 0
        target = None
        while queue:
            node, level = queue.popleft()
            if hasFound:
                target = node if level == uLevel else None
                break
            if node == u:
                hasFound = True
                uLevel = level
            if node.left:
                queue.append((node.left, level+1))
            if node.right:
                queue.append((node.right, level+1))
        return target

    def findNearestRightNode2(self, root: TreeNode, u: TreeNode) -> Optional[TreeNode]:
        container = [-1]
        def dfs(node, level, container):
            if not node or len(container) > 1:
                return
            if node == u:
                container[0] = level
                return
            if level == container[0]:
                container.append(node)
                return
            
            dfs(node.left, level+1, container)
            dfs(node.right, level+1, container)
        dfs(root, 0, container)
        return container[1] if len(container) > 1 else None

# Unit Tests
import unittest
funcs = [Solution().findNearestRightNode, Solution().findNearestRightNode2]

class TestFindNearestRightNode(unittest.TestCase):
    def testFindNearestRightNode1(self):
        for func in funcs:
            target = TreeNode(5)
            u = TreeNode(4)
            root = TreeNode(1, TreeNode(2, None, u), TreeNode(3, target, TreeNode(6)))
            self.assertEqual(func(root, u), target)

    def testFindNearestRightNode2(self):
        for func in funcs:
            target = None
            u = TreeNode(2)
            root = TreeNode(3, None, TreeNode(4, u))
            self.assertEqual(func(root, u), target)

if __name__ == "__main__":
    unittest.main()
