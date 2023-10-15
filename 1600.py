"""
1600. Throne Inheritance
description: https://leetcode.com/problems/throne-inheritance/description/
"""

"""
Note:
1. n-ary Tree + Preorder traversal:
__init__: O(1) time | O(1) space
birth: O(1) time | O(1) space
death: O(1) time | O(1) space
getInheritanceOrder: O(n) time | O(n) space
where n is the total number of people
"""

import unittest
from typing import List
class TreeNode:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.isDeath = False
    
class ThroneInheritance:

    def __init__(self, kingName: str):
        self.tree = TreeNode(kingName)
        self.nodeMap = {kingName: self.tree}

    def birth(self, parentName: str, childName: str) -> None:
        childNode = TreeNode(childName)
        self.nodeMap[childName] = childNode
        self.nodeMap[parentName].children.append(childNode)

    def death(self, name: str) -> None:
        self.nodeMap[name].isDeath = True

    def getInheritanceOrder(self) -> List[str]:
        output = []
        def dfs(node):
            if not node:
                return
            
            if not node.isDeath:
                output.append(node.name)
            
            for child in node.children:
                dfs(child)
        dfs(self.tree)
        return output

# Unit Tests
classes = [ThroneInheritance]

class TestThroneInheritance(unittest.TestCase):
    def testThroneInheritance1(self):
        for myclass in classes:
            t = myclass("king")
            t.birth("king", "andy")
            t.birth("king", "bob")
            t.birth("king", "catherine")
            t.birth("andy", "matthew")
            t.birth("bob", "alex")
            t.birth("bob", "asha")
            self.assertEqual(t.getInheritanceOrder(), ["king", "andy", "matthew", "bob", "alex", "asha", "catherine"])
            t.death("bob")
            self.assertEqual(t.getInheritanceOrder(), ["king", "andy", "matthew", "alex", "asha", "catherine"])
        


if __name__ == "__main__":
    unittest.main()
