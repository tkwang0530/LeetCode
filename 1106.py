"""
1106. Parsing A Boolean Expression
A boolean expression is an expression that evaluates to either true or false. It can be in one of the following shapes:

't' that evaluates to true.
'f' that evaluates to false.
'!(subExpr)' that evaluates to the logical NOT of the inner expression subExpr.
'&(subExpr1, subExpr2, ..., subExprn)' that evaluates to the logical AND of the inner expressions subExpr1, subExpr2, ..., subExprn where n >= 1.
'|(subExpr1, subExpr2, ..., subExprn)' that evaluates to the logical OR of the inner expressions subExpr1, subExpr2, ..., subExprn where n >= 1.
Given a string expression that represents a boolean expression, return the evaluation of that expression.

It is guaranteed that the given expression is valid and follows the given rules.

Example1:
Input: expression = "&(|(f))"
Output: false
Explanation: 
First, evaluate |(f) --> f. The expression is now "&(f)".
Then, evaluate &(f) --> f. The expression is now "f".
Finally, return false.

Example2:
Input: expression = "|(f,f,f,t)"
Output: true
Explanation: The evaluation of (false OR false OR false OR true) is true.

Example3:
Input: expression = "!(&(f,t))"
Output: true
Explanation: 
First, evaluate &(f,t) --> (false AND true) --> false --> f. The expression is now "!(f)".
Then, evaluate !(f) --> NOT false --> true. We return true.

Constraints:
1 <= expression.length <= 2 * 10^4
expression[i] is one following characters: '(', ')', '&', '|', '!', 't', 'f', and ','.
"""

"""
Note:
1. Two Stacks: O(n) time | O(n) space - where n is the length of string expression
"""

class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        boolStack = []
        specialStack = []
        i = 0
        while i < len(expression):
            char = expression[i]
            if char in ("t", "f"):
                boolStack.append(char == "t")
                i += 1
                continue
            
            if char == ",":
                i += 1
                continue
                
            if char in ("!", "&", "|"):
                specialStack.append(char)
                boolStack.append("(")
                i += 2
                continue
                
            if char == ")":
                specialChar = specialStack.pop()
                if specialChar == "&":
                    newBool = True
                    while boolStack[-1] != "(":
                        if not boolStack.pop():
                            newBool = False
                    boolStack.pop()
                    boolStack.append(newBool)
                elif specialChar == "|":
                    newBool = False
                    while boolStack[-1] != "(":
                        if boolStack.pop():
                            newBool = True
                    boolStack.pop()
                    boolStack.append(newBool)
                else:
                    newBool = not boolStack.pop()
                    boolStack.pop()
                    boolStack.append(newBool)
                i += 1
        
        return boolStack[0]

# Unit Tests
import unittest
funcs = [Solution().parseBoolExpr]

class TestParseBoolExpr(unittest.TestCase):
    def testParseBoolExpr1(self):
        for func in funcs:
            expression = "&(|(f))"
            self.assertEqual(func(expression=expression), False)

    def testParseBoolExpr2(self):
        for func in funcs:
            expression = "|(f,f,f,t)"
            self.assertEqual(func(expression=expression), True)

    def testParseBoolExpr3(self):
        for func in funcs:
            expression = "!(&(f,t))"
            self.assertEqual(func(expression=expression), True)

if __name__ == "__main__":
    unittest.main()