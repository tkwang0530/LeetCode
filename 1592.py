"""
1592. Rearrange Spaces Between Words
description: https://leetcode.com/problems/rearrange-spaces-between-words/description/
"""

"""
Note:
1. Greedy: O(n) time | O(n) space - where n is the length of string text
"""
class Solution:
    def reorderSpaces(self, text: str) -> str:
        spaceCount = 0
        words = []
        currentChars = []
        for i in range(len(text)):
            char = text[i]
            if char == " ":
                spaceCount += 1
                if len(currentChars) > 0:
                    words.append("".join(currentChars))
                    currentChars = []
                continue
            
            currentChars.append(char)
            
        if len(currentChars) > 0:
            words.append("".join(currentChars))
            currentChars = []
        
        wordCount = len(words)
        if wordCount == 1:
            return words[0] + spaceCount * " "
        
        spaceWidth = spaceCount // (wordCount-1)
        return (spaceWidth*" ").join(words) + (spaceCount % (wordCount-1)) * " "

# Unit Tests
import unittest
funcs = [Solution().reorderSpaces]

class TestReorderSpaces(unittest.TestCase):
    def testReorderSpaces1(self):
        for func in funcs:
            text = "  this   is  a sentence "
            self.assertEqual(func(text=text), "this   is   a   sentence")

    def testReorderSpaces2(self):
        for func in funcs:
            text = " practice   makes   perfect"
            self.assertEqual(func(text=text), "practice   makes   perfect ")

if __name__ == "__main__":
    unittest.main()