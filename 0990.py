"""
990. Satisfiability of Equality Equations
You are given an array of strings equations that represent relationships between variables where each string equations[i] is of length 4 and takes one of two different forms: "x_i==y_i" or "x_i!=y_i".Here, xi and yi are lowercase letters (not necessarily different) that represent one-letter variable names.

Return true if it is possible to assign integers to variable names so as to satisfy all the given equations, or false otherwise.

Example1:
Input: equations = ["a==b","b!=a"]
Output: false
Explanation: If we assign say, a = 1 and b = 1, then the first equation is satisfied, but not the second.
There is no way to assign the variables to satisfy both equations.

Example2:
Input: equations = ["b==a","a==b"]
Output: true
Explanation: We could assign a = 1 and b = 1 to satisfy both equations.

Constraints:
1 <= equations.length <= 500
equations[i].length == 4
equations[i][0] is a lowercase letter.
equations[i][1] is either '=' or '!'.
equations[i][2] is '='.
equations[i][3] is a lowercase letter.
"""

"""
Notes:
1. Disjoin Set: O(n) time | O(n) space
"""

from typing import List
class UnionFindSet:
    def __init__(self, n):
        self._parents = [i for i in range(n+1)]
        self._ranks = [1 for _ in range(n+1)]
        
    def find(self, u):
        while u != self._parents[u]:
            self._parents[u] = self._parents[self._parents[u]]
            u = self._parents[u]
        return u
    
    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return False
        if self._ranks[pu] < self._ranks[pv]:
            self._parents[pu] = pv
        elif self._ranks[pu] > self._ranks[pv]:
            self._parents[pv] = pu
        else:
            self._parents[pv] = pu
            self._ranks[pu] += 1
        return True

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        unionFindSet = UnionFindSet(26)
        for eq in equations:
            if eq[1] == "=":
                before, after = eq[0], eq[3]
                unionFindSet.union(ord(before) - ord("a"), ord(after) - ord("a"))
                
        for eq in equations:
            if eq[1] == "!":
                before, after = eq[0], eq[3]
                if unionFindSet.find(ord(before) - ord("a")) == unionFindSet.find(ord(after) - ord("a")):
                    return False
        return True


# Unit Tests
import unittest
funcs = [Solution().equationsPossible]

class TestEquationsPossible(unittest.TestCase):
    def testEquationsPossible1(self):
        for func in funcs:
            equations = ["a==b","b!=a"]
            self.assertEqual(func(equations=equations), False)

    def testEquationsPossible2(self):
        for func in funcs:
            equations = ["b==a","a==b"]
            self.assertEqual(func(equations=equations), True)

if __name__ == "__main__":
    unittest.main()