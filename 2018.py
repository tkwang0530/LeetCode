"""
2018. Check if Word Can Be Placed In Crossword
description: https://leetcode.com/problems/check-if-word-can-be-placed-in-crossword/description/
"""

"""
Note:
1. Brute-Force + string splitter: O(mn) space | O(max(m,n)) time - where m is the number of rows and n is the number of columns
"""

from typing import List
import unittest
class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        w = len(word)
        reveredWord = word[::-1]
        rows, cols = len(board), len(board[0])
        
        def hasMatched(element, word):
            if len(element) != w:
                return False
            for i in range(w):
                if element[i] != " " and element[i] != word[i]:
                    return False

            return True
            
        for col in range(cols):
            chars = []
            for row in range(rows):
                chars.append(board[row][col])
                
            str = "".join(chars)
            splitted = str.split("#")
            for element in splitted:
                if hasMatched(element, word) or hasMatched(element, reveredWord):
                    return True
        
        for row in range(rows):
            str = "".join(board[row])
            splitted = str.split("#")
            for element in splitted:
                if hasMatched(element, word) or hasMatched(element, reveredWord):
                    return True
        
        return False



# Unit Tests
funcs = [Solution().placeWordInCrossword]


class TestPlaceWordInCrossword(unittest.TestCase):
    def testPlaceWordInCrossword1(self):
        for func in funcs:
            board = [["#", " ", "#"], [" ", " ", "#"], ["#", "c", " "]]
            word = "abc"
            self.assertEqual(func(board=board, word=word), True)

    def testPlaceWordInCrossword2(self):
        for func in funcs:
            board = [[" ", "#", "a"], [" ", "#", "c"], [" ", "#", "a"]]
            word = "ac"
            self.assertEqual(func(board=board, word=word), False)

    def testPlaceWordInCrossword3(self):
        for func in funcs:
            board = [["#", " ", "#"], [" ", " ", "#"], ["#", " ", "c"]]
            word = "ca"
            self.assertEqual(func(board=board, word=word), True)

if __name__ == "__main__":
    unittest.main()
