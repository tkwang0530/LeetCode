"""
590. N-ary Tree Postorder Traversal
Given the root of an n-ary tree, return the postorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)

Example1:
                        1
                 /       |       \
              3        2        4
            /    \
          5      6
Input: root = [1,null,3,2,4,null,5,6]
Output: [5,6,3,2,4,1]

Constraints:
The number of the nodes in the tree is in the range [0, 10^4].
0 <= Node.val <= 10^4

Follow up: Recursive solution is trival, could you do it iteratively?
"""

"""
Note:
1. Recursion: O(n) time | O(h) space
2. Iteration (PreOrder like traversal then reverse the result): O(n) time | O(h) space
"""




from typing import List
import unittest
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def postorder(self, root: Node) -> List[int]:
        if not root:
            return []
        result = []
        self.dfs(root, result)
        return result
    
    def dfs(self, root, result) -> None:
        if root.children:
            for child in root.children:
                self.dfs(child, result)
        result.append(root.val)

    def postorder2(self, root: Node) -> List[int]:
        if not root:
            return []
        result, stack = [], [root]
        while len(stack) > 0:
            node = stack.pop()
            result.append(node.val)
            if node.children:
                for child in node.children:
                    stack.append(child)
        result.reverse()
        return result

# Unit Tests
funcs = [Solution().postorder, Solution().postorder2]


class TestPostorder(unittest.TestCase):
    def testPostorder1(self):
        for func in funcs:
            root = Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])
            self.assertEqual(func(root=root), [5,6,3,2,4,1])

if __name__ == "__main__":
    unittest.main()
