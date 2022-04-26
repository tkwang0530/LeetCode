"""
1506. Find Root of N-Ary Tree
You are given all the nodes of an N-ary tree as an array of Node objects, where each node has a unique value.

Example1:
Input: tree = [1,null,3,2,4,null,5,6]
Output: [1,null,3,2,4,null,5,6]
Explanation: The tree from the input data is shown above.
The driver code creates the tree and gives findRoot the Node objects in an arbitrary order.
For example, the passed array could be [Node(5),Node(4),Node(3),Node(6),Node(2),Node(1)] or [Node(2),Node(6),Node(1),Node(3),Node(5),Node(4)].
The findRoot function should return the root Node(1), and the driver code will serialize it and compare with the input data.
The input data and serialized Node(1) are the same, so the test passes.

Example2:
Input: tree = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]

Constraints:
- The total number of nodes is between [1, 5*10^4].
- Each node has a unique value.

Follw up:
Could you solve this problem in constant space complexity with a linear time algorithm?
"""

"""
Note:
1. HashTable: O(n) time | O(n) space
2. Use sign as marker: O(n) time | O(1) space
3. Bitwise Operation (XOR): O(n) time | O(1) space
"""


from typing import List
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

class Solution:
    def findRoot(self, tree: List[Node]) -> Node:
        nodeSet = set(tree)
        for node in tree:
            for child in node.children:
                if child in nodeSet:
                    nodeSet.remove(child)
        return nodeSet.pop()

    def findRoot2(self, tree: List[Node]) -> Node:
        for node in tree:
            for child in node.children:
                child.val *= -1
                
        root = None
        zeroNode = None
        for node in tree:
            if node.val > 0:
                root = node
            elif node.val == 0:
                zeroNode = node
            else:
                node.val *= -1
                
        return root if root else zeroNode

    def findRoot3(self, tree: List[Node]) -> Node:
        bitmask = 0
        for node in tree:
            bitmask ^= node.val
            for child in node.children:
                bitmask ^= child.val
        
        ans = None
        for node in tree:
            if node.val == bitmask:
                ans = node
        return ans


# Unit Tests
import unittest
funcs = [Solution().findRoot, Solution().findRoot2, Solution().findRoot3]


class TestFindRoot(unittest.TestCase):
    def testFindRoot1(self):
        for func in funcs:
            node4 = Node(4)
            node2 = Node(2)
            node5 = Node(5)
            node6 = Node(6)
            node3 = Node(3, [node5, node6])
            node1 = Node(1, [node3, node2, node4])
            self.assertEqual(func(tree=[node1, node2, node3, node4, node5, node6]), node1)

    def testFindRoot2(self):
        for func in funcs:
            node14 = Node(14)
            node12 = Node(12)
            node13 = Node(13)
            node2 = Node(2)
            node6 = Node(6)
            node10 = Node(10)
            node11 = Node(11, [node14])
            node8 = Node(8, [node12])
            node9 = Node(9, [node13])
            node5 = Node(5, [node9, node10])
            node4 = Node(4, [node8])
            node7 = Node(7, [node11])
            node3 = Node(3, [node6, node7])
            node1 = Node(1, [node2, node3, node4, node5])
            self.assertEqual(func(tree=[node1, node2, node3, node4, node5, node6, node7, node8, node9, node10, node11, node12, node13, node14]), node1)

if __name__ == "__main__":
    unittest.main()
