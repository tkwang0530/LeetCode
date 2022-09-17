"""
583. Delete Operation for Two Strings
Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 the same.

In one step, you can delete exactly one character in either string.

Example1:
Input: word1 = "sea", word2 = "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".

Example2:
Input: word1 = "leetcode", word2 = "etco"
Output: 4

Constraints:
1 <= word1.length, word2.length <= 500
word1 and word2 consist of only lowercase English letters.
"""

"""
Note:
1. BFS + HashTable: O((w1+w2)**(w1+w2)) time | O((w1+w2)**(w1+w2)) space -> TLE
2. DFS + memo: O(w1*w2) time | O(w1*w2) space - where w1 is the length of word1 and w2 is the length of word2
dfs(i, j) returns the number of steps required to equalize word1[i:] and word2[j:]

3. DP: O(w1*w2) time | O(w1*w2) space - where w1 is the length of word1 and w2 is the length of word2
"""




import unittest
import collections
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        word1, word2 = sorted([word1, word2])
        queue = collections.deque([(0, word1, word2)])
        cache = set([(word1, word2)])
        while queue:
            step, word1, word2 = queue.popleft()
            if word1 == word2:
                return step

            for i in range(len(word1)):
                newWord = word1[:i] + word1[i+1:]
                w1, w2 = sorted([newWord, word2])
                if (w1, w2) in cache:
                    continue
                cache.add((w1, w2))
                queue.append((step+1, w1, w2))

            for i in range(len(word2)):
                newWord = word2[:i] + word2[i+1:]
                w1, w2 = sorted([newWord, word1])
                if (w1, w2) in cache:
                    continue
                cache.add((w1, w2))
                queue.append((step+1, w1, w2))

        return -1

    def minDistance2(self, word1: str, word2: str) -> int:
        L1, L2 = len(word1), len(word2)
        memo = {}

        def dfs(i: int, j: int) -> int:
            if i == L1 and j == L2:
                return 0
            if i == L1 or j == L2:
                return max(len(word1) - i, len(word2) - j)

            if (i, j) in memo:
                return memo[(i, j)]

            memo[(i, j)] = 0
            if word1[i] == word2[j]:
                memo[(i, j)] = dfs(i+1, j+1)
            else:
                memo[(i, j)] = 1 + min(dfs(i+1, j), dfs(i, j+1))
            return memo[(i, j)]
        return dfs(0, 0)

    def minDistance3(self, word1: str, word2: str) -> int:
        L1, L2 = len(word1), len(word2)
        dp = [[1000] * (L2+1) for _ in range(L1+1)]
        for i in range(L1, -1, -1):
            for j in range(L2, -1, -1):
                if i == L1 and j == L2:
                    dp[i][j] = 0
                elif i == L1 or j == L2:
                    dp[i][j] = max(L1-i, L2-j)
                else:
                    if word1[i] == word2[j]:
                        dp[i][j] = dp[i+1][j+1]
                    else:
                        dp[i][j] = 1+min(dp[i+1][j], dp[i][j+1])
        return dp[0][0]


# Unit Tests
funcs = [Solution().minDistance, Solution().minDistance2,
         Solution().minDistance3]


class TestMinDistance(unittest.TestCase):
    def testMinDistance1(self):
        for func in funcs:
            word1 = "sea"
            word2 = "eat"
            self.assertEqual(func(word1=word1, word2=word2), 2)

    def testMinDistance2(self):
        for func in funcs:
            word1 = "leetcode"
            word2 = "etco"
            self.assertEqual(func(word1=word1, word2=word2), 4)


if __name__ == "__main__":
    unittest.main()
