"""
1807. Evaluate the Bracket Pairs of a String
You are given a string s that contains some bracket pairs, with each pair containing a non-empty key.
- For example, in the string "(name)is(age)yearsold", there are two bracket pairs that contain the keys "name" and "age".

You know the values of a wide range of keys. This is represented by a 2D string array knowledge where each knowledge[i] = [key_i, value_i] indicates that key key_i has a value of value_i

You are tasked to evaluate all of the bracket pairs. When you evaluate a bracket pair that contains some key key_i, you will:
- Replace key_i and the bracket pairs with the key's corresponding value_i.
- If you do not know the value of the key, will replace key_i and the bracket pair with a question mark "?" (without the quotation marks).

Each key will appear at most once in your knowledge. There will not be any nested brackets in s.
Return the resulting string after evaluating all the bracket pairs.

Example1:
Input: s = "(name)is(age)yearsold", knowledge = [["name","bob"],["age","two"]]
Output: "bobistwoyearsold"
Explanation:
The key "name" has a value of "bob", so replace "(name)" with "bob".
The key "age" has a value of "two", so replace "(age)" with "two".

Example2:
Input: s = "hi(name)", knowledge = [["a","b"]]
Output: "hi?"
Explanation: As you do not know the value of the key "name", replace "(name)" with "?".

Example3:
Input: s = "(a)(a)(a)aaa", knowledge = [["a","yes"]]
Output: "yesyesyesaaa"
Explanation: The same key can appear multiple times.
The key "a" has a value of "yes", so replace all occurrences of "(a)" with "yes".
Notice that the "a"s not in a bracket pair are not evaluated.

Constraints:
1 <= s.length <= 10^5
0 <= knowledge.length <= 10^5
knowledge[i].length == 2
1 <= key[i].length, value[i].length <= 10
s consists of lowercase English letters and round brackets '(' and ')'.
Every open bracket '(' in s will have a corresponding close bracket ')'.
The key in each bracket pair of s will be non-empty.
There will not be any nested bracket pairs in s.
key_i and value_i consist consist of lowercase English letters.
Each key_i in knowledge is unique.
"""

"""
Note:
1. Stack + HashTable: O(n+k) time | O(n+k) space - where n is the length of string s and k is the length of array knowledge
"""
from typing import List
class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        keyValues = {}
        for key, value in knowledge:
            keyValues[key] = value

        stack = []
        output = []
        for char in s:
            if not stack and char.isalpha():
                output.append(char)
                continue

            if stack and char.isalpha():
                stack.append(char)
                continue

            if char == "(":
                stack.append(char)
                continue

            if char == ")":
                key = "".join(stack[1:])
                toAdd = "?"
                if key in keyValues:
                    toAdd = keyValues[key]
                
                output.append(toAdd)
                stack = []
        return "".join(output)



# Unit Tests
import unittest
funcs = [Solution().evaluate]
class TestEvaluate(unittest.TestCase):
    def testEvaluate1(self):
        for func in funcs:
            s = "(name)is(age)yearsold"
            knowledge = [["name","bob"],["age","two"]]
            self.assertEqual(func(s, knowledge=knowledge), "bobistwoyearsold")

    def testEvaluate2(self):
        for func in funcs:
            s = "hi(name)"
            knowledge = [["a","b"]]
            self.assertEqual(func(s=s, knowledge=knowledge), "hi?")

    def testEvaluate3(self):
        for func in funcs:
            s = "(a)(a)(a)aaa"
            knowledge = [["a","yes"]]
            self.assertEqual(func(s=s, knowledge=knowledge), "yesyesyesaaa")

if __name__ == "__main__":
    unittest.main()
