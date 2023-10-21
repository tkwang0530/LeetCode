"""
2904. Shortest and Lexicographically Smallest Beautiful String
description: https://leetcode.com/problems/shortest-and-lexicographically-smallest-beautiful-string/description/
"""

"""
Note:
1. queue: O(nk) time | O(nk) space - where n is the length of string s
"""

import collections
class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        indice = []
        for i, char in enumerate(s):
            if char == "1":
                indice.append(i)

        if len(indice) < k:
            return ""
        

        first = indice[:k]
        queue = collections.deque(first) 
        candidate = first

        # if current smaller than candidate return true
        def compare(current, candidate):
            if current[-1]-current[0] < candidate[-1]-candidate[0]:
                return True
            elif current[-1]-current[0] > candidate[-1]-candidate[0]:
                return False

            offset = current[0]
            candidateOffset = candidate[0]
            for i in range(len(current)):
                currentVal = current[i]-offset
                candidateVal = candidate[i]-candidateOffset
                if currentVal > candidateVal:
                    return True
                elif currentVal < candidateVal:
                    return False
                
            return False

        for i in range(k, len(indice)):
            queue.append(indice[i])
            queue.popleft()
            
            current = list(queue)
            if compare(current, candidate):
                candidate = current
        
        return "".join(s[candidate[0] : candidate[-1]+1])

# Unit Tests
import unittest
funcs = [Solution().shortestBeautifulSubstring]

class TestShortestBeautifulSubstring(unittest.TestCase):
    def testShortestBeautifulSubstring1(self):
        for shortestBeautifulSubstring in funcs:
            s = "100011001"
            k = 3
            self.assertEqual(shortestBeautifulSubstring(s=s, k=k), "11001")

    def testShortestBeautifulSubstring2(self):
        for ShortestBeautifulSubstring in funcs:
            s = "1011"
            k = 2
            self.assertEqual(ShortestBeautifulSubstring(s=s, k=k), "11")

    def testShortestBeautifulSubstring3(self):
        for ShortestBeautifulSubstring in funcs:
            s = "000"
            k = 1
            self.assertEqual(ShortestBeautifulSubstring(s=s, k=k), "")

if __name__ == "__main__":
    unittest.main()