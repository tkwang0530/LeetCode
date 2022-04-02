"""
331. Verify Preorder Serialization of a Binary Tree
One way to serialize a binary tree is to use preorder traversal. When we encounter a non-null node, we record the node's value. If it's a null node, we record using a sentinel value such as '#'.

Given a string of comma-separated values preorder, return true if it is a correct preorder traversal serialization of a binary tree.

It is guaranteed that each comma-separated value in the string must be either an integer or a character '#' representing null pointer.

You may assume that the input format is always valid.
- for example, it could never contain two consecutive commas, such as "1,,3".
Note: You are not allowed to reconstruct the tree.

Example1:
Input: preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"
Output: true

Example2:
Input: preorder = "1,#"
Output: false

Example3:
Input: preorder = "9,#,#,1"
Output: false
"""

"""
Note:
1. Stack: O(n) time | O(n) space
"""

class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        if preorder == '#':
            return True

        preorder = preorder.split(',')
        stack = []
        
        for i, char in enumerate(preorder):
            if char != '#':
                stack.append([char, 0])
                continue

            if not stack:
                return False
            
            while stack and stack[-1][1] == 1:
                stack.pop()

            if i == len(preorder) - 1 and not stack:
                return True
            elif not stack:
                return False

            stack[-1][1] += 1
        return False


# Unit Tests
import unittest
funcs = [Solution().isValidSerialization]
class TestIsValidSerialization(unittest.TestCase):
    def testIsValidSerialization1(self):
        for func in funcs:
            preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"
            self.assertEqual(func(preorder=preorder), True)

    def testIsValidSerialization2(self):
        for func in funcs:
            preorder = "1,#"
            self.assertEqual(func(preorder=preorder), False)

    def testIsValidSerialization3(self):
        for func in funcs:
            preorder = "9,#,#,1"
            self.assertEqual(func(preorder=preorder), False)

if __name__ == "__main__":
    unittest.main()
