"""
394. Decode String
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Example1:
Input: s = "3[a]2[bc]"
Output: "aaabcbc"

Example2:
Input: s = "3[a2[c]]"
Output: "accaccacc"

Example3:
Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"

Example4:
Input: s = "abc3[cd]xyz"
Output: "abccdcdcdxyz"

Constraints:
1 <= s.length <= 30
s consists of lowercase English letters, digits, and square brackets '[]'.
s is guaranteed to be a valid input.
All the integers in s are in the range [1, 300].
"""

"""
Notes:
1. Using Stack 1: O(n^2) time | O(n) space - where n is the length of the decode string
2. Using Stack 2: O(n^2) time | O(n) space - where n is the length of the decode string
3. Recursion with queue: O(n^2) time | O(n) space - where n is the length of the decode string
"""

from collections import deque
class Solution(object):
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                chars = []
                while stack[-1] != "[":
                    chars.append(stack.pop())
                stack.pop() # one more pop to pop the opening bracket

                # calculate the k before the opening bracket
                k, count = 0, 1
                while stack and stack[-1].isdigit():
                    k += count * (ord(stack.pop()) - ord("0"))
                    count *= 10
                stack.append(k * "".join(chars[::-1]))
        return "".join(stack)

    def decodeString2(self, s: str) -> str:
        stack, currNum, currChars = [], 0, [], 
        for char in s:
            if char == "[":
                stack.append(currChars)
                stack.append(currNum)
                currChars = []
                currNum = 0
            elif char == "]":
                num = stack.pop()
                prevString = stack.pop()
                prevString.extend(currChars * num)
                currChars = prevString
            elif char.isdigit():
                currNum = currNum * 10 + (ord(char) - ord("0"))
            else:
                currChars.append(char)
        return "".join(currChars)

    def decodeString3(self, s: str) -> str:
        queue = deque()
        for char in s:
            queue.append(char)
        return self.decodeStringHelper(queue)

    def decodeStringHelper(self, queue: deque) -> str:
        chars = []
        num = 0
        while len(queue) > 0:
            char = queue.popleft()
            if char.isdigit():
                num = 10 * num + (ord(char) - ord("0"))
            elif char == "[":
                sub = self.decodeStringHelper(queue)
                chars.append(num * sub)
                num = 0
            elif char == "]":
                break
            else:
                chars.append(char)
        return "".join(chars)

# Unit Tests
import unittest
funcs = [Solution().decodeString, Solution().decodeString2, Solution().decodeString3]

class TestDecodeString(unittest.TestCase):
    def testDecodeString1(self):
        for func in funcs:
            s = "3[a]2[bc]"
            self.assertEqual(func(s=s), "aaabcbc")

    def testDecodeString2(self):
        for func in funcs:
            s = "3[a2[c]]"
            self.assertEqual(func(s=s), "accaccacc")

    def testDecodeString3(self):
        for func in funcs:
            s = "2[abc]3[cd]ef"
            self.assertEqual(func(s=s), "abcabccdcdcdef")

    def testDecodeString4(self):
        for func in funcs:
            s = "abc3[cd]xyz"
            self.assertEqual(func(s=s), "abccdcdcdxyz")


if __name__ == "__main__":
    unittest.main()