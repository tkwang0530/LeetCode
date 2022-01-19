"""
399. Evaluate Division
You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0 .

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

Example1:
Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation: 
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]

Example2:
Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Output: [3.75000,0.40000,5.00000,0.20000]

Example3:
Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
Output: [0.50000,2.00000,-1.00000,-1.00000]

Constraints:
1 <= equations.length <= 20
equations[i].length == 2
1 <= Ai.length, Bi.length <= 5
values.length == equations.length
0.0 < values[i] <= 20.0
1 <= queries.length <= 20
queries[i].length == 2
1 <= Cj.length, Dj.length <= 5
Ai, Bi, Ci, Dj consist of lower case English letters and digits.
"""

"""
Note:
1. dfs + path compression: O(n^2) time | O(n^2) space
"""

from typing import List

class Node:
    def __init__(self, name):
        self.name = name
        self.neighbors = {name: 1.0}
        self.divisors = {name: 1.0}


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        nodeDict = {}
        for equation, value in zip(equations, values):
            dividend, divisor = equation
            if dividend not in nodeDict:
                nodeDict[dividend] = Node(dividend)
            
            if divisor not in nodeDict:
                nodeDict[divisor] = Node(divisor)
            
            if divisor not in nodeDict[dividend].neighbors:
                nodeDict[dividend].neighbors[divisor] = value

            if dividend not in nodeDict[divisor].neighbors:
                nodeDict[divisor].neighbors[dividend] = 1/value

        result = []
        
        def dfs(source, target, node, tempVal, visited):
            if node in visited or target.name in source.divisors:
                return
            visited.add(node)
            

            for divisor in node.neighbors.keys():
                dfs(source, target, nodeDict[divisor], tempVal * node.neighbors[divisor], visited)
            
            source.divisors[node.name] = tempVal
            node.divisors[source.name] = 1/tempVal

        for query in queries:
            start, end = query
            if start not in nodeDict or end not in nodeDict:
                result.append(-1.0)
                continue
            visited = set()
            dfs(nodeDict[start], nodeDict[end], nodeDict[start], 1, visited)
            if end in nodeDict[start].divisors:
                result.append(nodeDict[start].divisors[end])
            else:
                result.append(-1.0)
        return result
            

# Unit Tests
import unittest
funcs = [Solution().calcEquation]

class TestCalcEquation(unittest.TestCase):
    def testCalcEquation1(self):
        for func in funcs:
            equations = [["a","b"],["b","c"]]
            values = [2.0,3.0]
            queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
            self.assertEqual(func(equations=equations, values=values, queries=queries), [6.00000,0.50000,-1.00000,1.00000,-1.00000])

    def testCalcEquation2(self):
        for func in funcs:
            equations = [["a","b"],["b","c"],["bc","cd"]]
            values = [1.5,2.5,5.0]
            queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
            self.assertEqual(func(equations=equations, values=values, queries=queries), [3.75000,0.40000,5.00000,0.20000])

    def testCalcEquation3(self):
        for func in funcs:
            equations = [["a","b"]]
            values = [0.5]
            queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
            self.assertEqual(func(equations=equations, values=values, queries=queries), [0.50000,2.00000,-1.00000,-1.00000])


if __name__ == "__main__":
    unittest.main()
