"""
297. Serialize and Deserialize Binary Tree
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how Leetcode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

Example1:
        1
      /   \
    2     3 
         /    \
       4      5    
Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]

Example2:
Input: root = []
Output: []

Example3:
Input: root = [1]
Output: [1]

Example4:
Input: root = [1,2]
Output: [1,2]

Constraints:
The number of nodes in the tree is in the range [0, 10^4]
-1000 <= Node.val <= 1000
"""

"""
Note:
For serialize: O(n) time | O(n) space
(1) Recursive DFS (preorder traversal) to create a list "preorder", if not node, remember to append "None"
(2) return ",".join(preorder)
For deserialize: O(n) time | O(n) space
(1) preorder = data.split(",") and convert to a deque
(2) Recursively build the tree using the preorder deque
"""



from collections import deque
from typing import List
import unittest
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:
    def serialize(self, root):
        result = []
        self.dfs(root, result)
        return ",".join(result)
    
    def deserialize(self, data):
        dataList = data.split(",")
        preorder = deque(dataList)
        return self.buildTree(preorder)

    def dfs(self, node: TreeNode, result: List[str]) -> None:
        if not node:
            result.append("None")
            return
        result.append(str(node.val))
        self.dfs(node.left, result)  
        self.dfs(node.right, result)

    def buildTree(self, preorder: List[str]) -> TreeNode:
        str = preorder.popleft()
        if str == "None":
            return None
        root = TreeNode(int(str))
        root.left = self.buildTree(preorder)
        root.right = self.buildTree(preorder)
        return root


# TEST ONLY
def isSameTree(p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        return all((p.val == q.val, isSameTree(p.left, q.left), isSameTree(p.right, q.right)))

class TestCodec(unittest.TestCase):
    def testCodec1(self):
        tree = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
        ser = Codec()
        deser = Codec()
        tree2 = deser.deserialize(ser.serialize(tree))
        self.assertEqual(isSameTree(tree, tree2), True)

    def testCodec2(self):
        tree = None
        ser = Codec()
        deser = Codec()
        tree2 = deser.deserialize(ser.serialize(tree))
        self.assertEqual(isSameTree(tree, tree2), True)

    def testCodec3(self):
        tree = TreeNode(1)
        ser = Codec()
        deser = Codec()
        tree2 = deser.deserialize(ser.serialize(tree))
        self.assertEqual(isSameTree(tree, tree2), True)

    def testCodec4(self):
        tree = TreeNode(1, TreeNode(2))
        ser = Codec()
        deser = Codec()
        tree2 = deser.deserialize(ser.serialize(tree))
        self.assertEqual(isSameTree(tree, tree2), True)


if __name__ == "__main__":
    unittest.main()
