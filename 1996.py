"""
1996. The Number of Weak Characters in the Game
You are playing a game that contains multiple characters, and each of the characters has two main properties: attack and defense. You are given a 2D integer array properties where properties[i] = [attack_i, defense_i] represents the properties of the i-th character in the game.

A character is said to be weak if any other character has both attack and defense levels strictly greater than this character's attack and defense levels. More formally, a character i is said to be weak if there exists another character j where attack_j > attack_i and defense_j > defense_i.

Return the number of weak characters.

Example1:
Input: properties = [[5,5],[6,3],[3,6]]
Output: 0
Explanation: No character has strictly greater attack and defense than the other.

Example2:
Input: properties = [[2,2],[3,3]]
Output: 1
Explanation: The first character is weak because the second character has a strictly greater attack and defense.

Example3:
Input: properties = [[1,5],[10,4],[4,3]]
Output: 1
Explanation: The third character is weak because the second character has a strictly greater attack and defense.

Constraints:
2 <= properties.length <= 10^5
properties[i].length == 2
1 <= attack_i, defense_i <= 10^5
"""

"""
Note:
1. Greedy with Sorting: O(nlogn) time | O(n) space - where n is the length of array properties
2. Sort + Monotonic Stack: O(nlogn) time | O(n) space - where n is the length of array properties
3. buckets: O(n) time | O(n) space - where n is the length of array properties
"""

from typing import List
class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (-x[0], x[1]))
        count = 0
        currentDefenseMax = 0
        for _, defense in properties:
            if defense < currentDefenseMax:
                count += 1
            else:
                currentDefenseMax = defense
        return count

    def numberOfWeakCharacters2(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (x[0], -x[1]))
        count = 0
        stack = []
        for _, defense in properties:
            while stack and stack[-1] < defense:
                stack.pop()
                count += 1
            stack.append(defense)
        return count

    def numberOfWeakCharacters3(self, properties: List[List[int]]) -> int:
        maxDefenses = [0] * (100001)
        for attack, defense in properties:
            maxDefenses[attack] = max(maxDefenses[attack], defense)

        suffixMaxDefenses = [0] * (100001)
        for i in range(100000-1, -1, -1):
            suffixMaxDefenses[i] = max(suffixMaxDefenses[i+1], maxDefenses[i+1])
        
        count = 0
        for attack, defense in properties:
            count += suffixMaxDefenses[attack] > defense
        return count

# Unit Tests
import unittest
funcs = [Solution().numberOfWeakCharacters, Solution().numberOfWeakCharacters2, Solution().numberOfWeakCharacters3]
class TestNumberOfWeakCharacters(unittest.TestCase):
    def testNumberOfWeakCharacters1(self):
        for func in funcs:
            properties = [[5,5],[6,3],[3,6]]
            self.assertEqual(func(properties=properties), 0)

    def testNumberOfWeakCharacters2(self):
        for func in funcs:
            properties = [[2,2],[3,3]]
            self.assertEqual(func(properties=properties), 1)

    def testNumberOfWeakCharacters3(self):
        for func in funcs:
            properties = [[1,5],[10,4],[4,3]]
            self.assertEqual(func(properties=properties), 1)

    def testNumberOfWeakCharacters4(self):
        for func in funcs:
            properties = [[1,1],[2,1],[2,2],[1,2]]
            self.assertEqual(func(properties=properties), 1)

    def testNumberOfWeakCharacters5(self):
        for func in funcs:
            properties = [[7,9],[10,7],[6,9],[10,4],[7,5],[7,10]]
            self.assertEqual(func(properties=properties), 2)

    def testNumberOfWeakCharacters6(self):
        for func in funcs:
            properties = [[1,5],[1,4],[1,3],[4,3],[10,4],[10,4],[10,3]]
            self.assertEqual(func(properties=properties), 2)

if __name__ == "__main__":
    unittest.main()
