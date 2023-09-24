"""
297. Serialize and Deserialize Binary Tree
description: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/
"""

"""
Note:
1. preorder traversal
For serialize: O(n) time | O(n) space
(1) Recursive DFS (preorder traversal) to create a list "preorder", if not node, remember to append "None"
(2) return ",".join(preorder)
For deserialize: O(n) time | O(n) space
(1) preorder = data.split(",") and convert to a deque
(2) Recursively build the tree using the preorder deque

2. BFS (layer order traversal)
For serialize: O(n) time | O(n) space
For deserialize: O(n) time | O(n) space
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


class Codec2:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        outputArr = []
        currentNodes = [root]
        while currentNodes:
            nextNodes = []
            for node in currentNodes:
                nodeValStr = str(node.val) if node else "null"
                outputArr.append(nodeValStr)
                if node:
                    nextNodes.append(node.left)
                    nextNodes.append(node.right)
            currentNodes = nextNodes
        return ",".join(outputArr)



    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "":
            return None

        nodeValStrs = data.split(",")
        idxNodeMap = {}
        idxNodeMap[0] = TreeNode(int(nodeValStrs[0]))
        
        i = 0
        j = 1
        while j < len(nodeValStrs)-1:
            if j not in idxNodeMap:
                idxNodeMap[j] = None if nodeValStrs[j] == "null" else TreeNode(int(nodeValStrs[j]))
            if j+1 not in idxNodeMap:
                idxNodeMap[j+1] = None if nodeValStrs[j+1] == "null" else TreeNode(int(nodeValStrs[j+1]))

            currentRoot = idxNodeMap[i]
            left = idxNodeMap[j]
            right = idxNodeMap[j+1]

            currentRoot.left = left
            currentRoot.right = right
            j += 2
            i += 1
            while i < j and nodeValStrs[i] == "null":
                i += 1
        return idxNodeMap[0]

# TEST ONLY
def isSameTree(p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        return all((p.val == q.val, isSameTree(p.left, q.left), isSameTree(p.right, q.right)))

classes = [Codec, Codec2]
class TestCodec(unittest.TestCase):
    def testCodec1(self):
        for myclass in classes:
            ser = myclass()
            deser = myclass()
            tree = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
            tree2 = deser.deserialize(ser.serialize(tree))
            self.assertEqual(isSameTree(tree, tree2), True)

    def testCodec2(self):
        for myclass in classes:
            ser = myclass()
            deser = myclass()
            tree = None
            tree2 = deser.deserialize(ser.serialize(tree))
            self.assertEqual(isSameTree(tree, tree2), True)

    def testCodec3(self):
        for myclass in classes:
            ser = myclass()
            deser = myclass()
            tree = TreeNode(1)
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
