"""
1079. Letter Tile Possibilities
You have n  tiles, where each tile has one letter tiles[i] printed on it.

Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles.

Example1:
Input: tiles = "AAB"
Output: 8
Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".

Example2:
Input: tiles = "AAABBC"
Output: 188

Example3:
Input: tiles = "V"
Output: 1

Constraints:
1 <= tiles.length <= 7
tiles consists of uppercase English letters.
"""

"""
Note:
1. Backtracking: O(26^n) time | O(26) space - where n is the length of string tiles
2. Backtracking: O(min(26,n)^n) time | O(min(26,n)) space - where n is the length of string tiles
"""

import unittest
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def dfs(charCounts):
            total = 0
            for i in range(26):
                if charCounts[i] > 0:
                    total += 1
                    charCounts[i] -= 1
                    total += dfs(charCounts)
                    charCounts[i] += 1
            return total
        
        charCounts = [0] * 26
        for char in tiles:
            charCounts[ord(char)-ord('A')] += 1
        
        return dfs(charCounts)

    def numTilePossibilities2(self, tiles: str) -> int:
        def dfs(charCounts):
            total = 0
            for i in range(len(charCounts)):
                if charCounts[i] > 0:
                    total += 1
                    charCounts[i] -= 1
                    total += dfs(charCounts)
                    charCounts[i] += 1
            return total
        
        charIdx = {}
        idx = 0
        charCounts = []
        for char in tiles:
            if char not in charIdx:
                charIdx[char] = idx
                charCounts.append(0)
                idx += 1
            charCounts[charIdx[char]] += 1
        
        return dfs(charCounts)

# Unit Tests
funcs = [Solution().numTilePossibilities, Solution().numTilePossibilities2]


class TestNumTilePossibilities(unittest.TestCase):
    def testNumTilePossibilities1(self):
        for func in funcs:
            tiles = "AAB"
            self.assertEqual(func(tiles=tiles), 8)

    def testNumTilePossibilities2(self):
        for func in funcs:
            tiles = "AAABBC"
            self.assertEqual(func(tiles=tiles), 188)

    def testNumTilePossibilities3(self):
        for func in funcs:
            tiles = "V"
            self.assertEqual(func(tiles=tiles), 1)


if __name__ == "__main__":
    unittest.main()
