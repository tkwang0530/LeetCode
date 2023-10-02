"""
1583. Count Unhappy Friends
description: https://leetcode.com/problems/count-unhappy-friends/description/
"""

"""
Note:
1. HashTable: O(n^2) time | O(n^2) space
"""


from typing import List
import unittest
class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        couples = {}
        for u, v in pairs:
            couples[u] = v
            couples[v] = u

        def getCouple(person: int) -> int:
            return couples[person]

        ranks = {}
        for person, preference in enumerate(preferences):
            for rank, friend in enumerate(preference):
                t = (person, friend)
                ranks[t] = rank
        
        def getRank(person: int, friend: int) -> int:
            return ranks[(person, friend)]

        unhappies = 0
        for person in range(n):
            couple = getCouple(person)
            coupleRank = getRank(person, couple)
            isUnhappy = False
            for i in range(coupleRank):
                candidate = preferences[person][i]
                candidateCouple = getCouple(candidate)
                coupleRank = getRank(candidate, candidateCouple)
                personRank = getRank(candidate, person)
                if personRank < coupleRank:
                    isUnhappy = True
                    break
            
            unhappies += isUnhappy
        return unhappies

# Unit Tests
funcs = [Solution().unhappyFriends]
class TestUnhappyFriends(unittest.TestCase):
    def testUnhappyFriends1(self):
        for unhappyFriends in funcs:
            n = 4
            preferences = [[1, 2, 3], [3, 2, 0], [3, 1, 0], [1, 2, 0]]
            pairs = [[0, 1], [2, 3]]
            self.assertEqual(unhappyFriends(n=n, preferences=preferences, pairs=pairs), 2)

    def testUnhappyFriends2(self):
        for unhappyFriends in funcs:
            n = 2
            preferences = [[1], [0]]
            pairs = [[1, 0]]
            self.assertEqual(unhappyFriends(n=n, preferences=preferences, pairs=pairs), 0)

    def testUnhappyFriends3(self):
        for unhappyFriends in funcs:
            n = 4
            preferences = [[1, 3, 2], [2, 3, 0], [1, 3, 0], [0, 2, 1]]
            pairs = [[1, 3], [0, 2]]
            self.assertEqual(unhappyFriends(n=n, preferences=preferences, pairs=pairs), 4)

if __name__ == "__main__":
    unittest.main()
