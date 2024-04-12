"""
399. Evaluate Division
description: https://leetcode.com/problems/evaluate-division/description/
"""

"""
Note:
1. dfs + path compression: O(n^2) time | O(n^2) space
2. Floyd Warshall: O(n^3) time | O(n^2) space
3. bfs + hashSet: O(Q*E) time | O(V+E) space - where Q is the length of queries, E is the length of equations, V is the length of variables
ref: https://www.youtube.com/watch?v=Uei1fwDoyKk
"""

import collections
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
    
class Solution2:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # graph
        indexTable = {} #<var, the index of a in indexList>
        indexList = []
        graph = collections.defaultdict(list)
        for i, (a, b) in enumerate(equations):
            value = values[i]

            if a not in indexTable:
                indexTable[a] = len(indexTable)
                indexList.append(a)
            
            if b not in indexTable:
                indexTable[b] = len(indexTable)
                indexList.append(b)

            graph[a].append((value, b))
            graph[b].append((1/value, a))

        # initialize all node-to-node's weight(division) into float("inf")
        table = [[float("inf")] * len(indexTable) for _ in range(len(indexTable))]

        # node to node itself has node/node = 1
        for i in range(len(indexTable)):
            table[i][i] = 1

        for i, (a, b) in enumerate(equations):
            value = values[i]
            indexA = indexTable[a]
            indexB = indexTable[b]
            table[indexA][indexB] = value
            table[indexB][indexA] = 1 / value

        # floyd warshall
        for src in indexList:
            for dst in indexList:
                for mid in indexList:
                    indexSrc = indexTable[src]
                    indexDst = indexTable[dst]
                    indexMid = indexTable[mid]

                    table[indexSrc][indexDst] = min(table[indexSrc][indexDst], table[indexSrc][indexMid] * table[indexMid][indexDst])

        result = []
        for a, b in queries:
            if a not in indexTable or b not in indexTable:
                result.append(-1.0)
            else:
                indexA = indexTable[a]
                indexB = indexTable[b]
                if table[indexA][indexB] != float("inf"):
                    result.append(table[indexA][indexB])
                else:
                    result.append(-1.0)
        return result

class Solution3:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = collections.defaultdict(list) # <strA, (strB, strA/strB)>
        for i, (strA, strB) in enumerate(equations):
            value = values[i]
            graph[strA].append((strB, value))
            graph[strB].append((strA, 1/value))

        def bfs(src, target):
            if src not in graph or target not in graph:
                return -1
            
            queue, visited = collections.deque(), set()
            queue.append((src, 1))
            visited.add(src)
            while queue:
                node, w = queue.popleft()
                if node == target:
                    return w
                for neighbor, weight in graph[node]:
                    if neighbor not in visited:
                        queue.append([neighbor, w * weight])
                        visited.add(neighbor)
            return -1

        
        return [bfs(q[0], q[1]) for q in queries]

# Unit Tests
import unittest
funcs = [Solution().calcEquation, Solution2().calcEquation, Solution3().calcEquation]

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
