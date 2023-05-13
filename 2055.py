"""
2055. Plates Between Candles
There is a long table with a line of plates and candles arranged on top of it. You are given a 0-indexed string s consisting of characters '*' and '|' only, where a '*' represents a plate and a '|' represents a candle.

You are also given a 0-indexed 2D integer array queries where queries[i] = [lefti, righti] denotes the substring s[lefti...righti] (inclusive). For each query, you need to find the number of plates between candles that are in the substring. A plate is considered between candles if there is at least one candle to its left and at least one candle to its right in the substring.

For example, s = "||**||**|*", and a query [3, 8] denotes the substring "*||**|". The number of plates between candles in this substring is 2, as each of the two plates has at least one candle in the substring to its left and right.
Return an integer array answer where answer[i] is the answer to the ith query.

Example1:
Input: s = "**|**|***|", queries = [[2,5],[5,9]]
Output: [2,3]
Explanation:
- queries[0] has two plates between candles.
- queries[1] has three plates between candles.

Example2:
Input: s = "***|**|*****|**||**|*", queries = [[1,17],[4,5],[14,17],[5,11],[15,16]]
Output: [9,0,0,0,0]
Explanation:
- queries[0] has nine plates between candles.
- The other queries have zero plates between candles.

Constraints:
3 <= s.length <= 10^5
s consists of '*' and '|' characters.
1 <= queries.length <= 10^5
queries[i].length == 2
0 <= left_i <= right_i < s.length
"""

"""
Note:
1. prefixSums + binary search: O(n+qlogn) time | O(n+q) space - where n is the length of string s and q is the length of array queries
2. prefixSums + prefix + suffix: O(n+q) time | O(n+q) space - where n is the length of string s and q is the length of array queries
For each indice, find the nearest candle index on the left and on the right.
"""




import unittest
from typing import List
import bisect
class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        prefixSums = [0] * (n+1)
        for i in range(1, n+1):
            prefixSums[i] = prefixSums[i-1] + (s[i-1] == "*")

        candleIndice = []
        for i, char in enumerate(s):
            if char == "|":
                candleIndice.append(i)

        def countPlates(left, right):
            return prefixSums[right+1] - prefixSums[left]

        answer = []
        for left, right in queries:
            leftIdx = bisect.bisect_left(candleIndice, left)
            if leftIdx == len(candleIndice):
                answer.append(0)
                continue
            leftCandleIdx = candleIndice[leftIdx]
            rightIdx = bisect.bisect_right(candleIndice, right)

            if rightIdx - 1 < 0:
                answer.append(0)
                continue
    
            rightCandleIdx = candleIndice[rightIdx-1]
            if rightIdx < len(candleIndice) and candleIndice[rightIdx] == right:
                rightCandleIdx = candleIndice[rightIdx]

            if leftCandleIdx < rightCandleIdx:
                answer.append(countPlates(leftCandleIdx, rightCandleIdx))
            else:
                answer.append(0)
        return answer

    def platesBetweenCandles2(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        prefixSums = [0] * (n+1)
        for i in range(1, n+1):
            prefixSums[i] = prefixSums[i-1] + (s[i-1] == "*")

        candleIndice = []
        for i, char in enumerate(s):
            if char == "|":
                candleIndice.append(i)

        def countPlates(left, right):
            return prefixSums[right+1] - prefixSums[left]
        
        nearestLeftCandle = [0] * n
        nearestRightCandle = [0] * n

        candle = -1
        for i, char in enumerate(s):
            if char == "|":
                candle = i
            nearestLeftCandle[i] = candle

        candle = -1
        for i in range(n-1, -1, -1):
            if s[i] == "|":
                candle = i
            nearestRightCandle[i] = candle
        
        answer = []
        for left, right in queries:
            leftCandle = nearestRightCandle[left]
            rightCandle  = nearestLeftCandle[right]
            if leftCandle == -1 or rightCandle == -1 or leftCandle >= rightCandle:
                answer.append(0)
                continue

            answer.append(countPlates(leftCandle, rightCandle))
        return answer

# Unit Tests
funcs = [Solution().platesBetweenCandles, Solution().platesBetweenCandles2]


class TestPlatesBetweenCandles(unittest.TestCase):
    def testPlatesBetweenCandles1(self):
        for func in funcs:
            s = "**|**|***|"
            queries = [[2,5],[5,9]]
            self.assertEqual(func(s=s, queries=queries), [2,3])

    def testPlatesBetweenCandles2(self):
        for func in funcs:
            s = "***|**|*****|**||**|*"
            queries = [[1,17],[4,5],[14,17],[5,11],[15,16]]
            self.assertEqual(func(s=s, queries=queries), [9,0,0,0,0])

    def testPlatesBetweenCandles3(self):
        for func in funcs:
            s = "*|*|||"
            queries = [[0,0],[1,3]]
            self.assertEqual(func(s=s, queries=queries), [0,1])


if __name__ == "__main__":
    unittest.main()
