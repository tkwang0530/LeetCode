"""
244. Shortest Word Distance II
Design a data structure that will be initialized with a string array, and then it should answer queries of the shortest distance between two different strings from the array.

Implement the WordDistance class:
- WordDistance(String[] wordsDict) initializes the object with the strings array wordsDict.
- int shortest(String word1, String word2) returns the shortest distance between word1 and word2 in the array wordsDict.

Example1:
Input
["WordDistance", "shortest", "shortest"]
[[["practice", "makes", "perfect", "coding", "makes"]], ["coding", "practice"], ["makes", "coding"]]
Output
[null, 3, 1]

Explanation
WordDistance wordDistance = new WordDistance(["practice", "makes", "perfect", "coding", "makes"]);
wordDistance.shortest("coding", "practice"); // return 3
wordDistance.shortest("makes", "coding");    // return 1

Constraints:
1 <= wordsDict.length <= 3 * 10^4
1 <= wordsDict[i].length <= 10
wordsDict[i] consists of lowercase English letters.
word1 and word2 are in wordsDict.
word1 != word2
At most 5000 calls will be made to shortest.
"""

"""
Note:
1. Brute-Force + HashTable: O(n^2) time | O(n^2) space - where n is the length of array wordsDict
2. Two Pointers + HashTable: O(n) time | O(n) space - where n is the length of array wordsDict
"""




import unittest
import collections
from typing import List
class WordDistance:

    def __init__(self, wordsDict: List[str]):
        n = len(wordsDict)
        self.minDistance = {}

        for i in range(n):
            for j in range(i+1, n):
                word1 = wordsDict[i]
                word2 = wordsDict[j]
                if word1 == word2:
                    continue
                pair = tuple(sorted([word1, word2]))
                if pair not in self.minDistance:
                    self.minDistance[pair] = j-i
                else:
                    self.minDistance[pair] = min(self.minDistance[pair], j-i)

    def shortest(self, word1: str, word2: str) -> int:
        return self.minDistance[tuple(sorted([word1, word2]))]


class WordDistance2:

    def __init__(self, wordsDict: List[str]):
        self.wordIndice = collections.defaultdict(list)
        self.memo = {}
        for i, word in enumerate(wordsDict):
            self.wordIndice[word].append(i)

    def __getDistance(self, word1, word2):
        word1, word2 = sorted([word1, word2])
        if (word1, word2) in self.memo:
            return self.memo[(word1, word2)]

        n = len(self.wordIndice[word1])
        m = len(self.wordIndice[word2])

        # Two Pointers method
        i = j = 0
        minDistance = float("inf")
        while i < n and j < m:
            idx1, idx2 = self.wordIndice[word1][i], self.wordIndice[word2][j]
            minDistance = min(minDistance, abs(idx1-idx2))

            if idx1 < idx2:
                i += 1
            else:
                j += 1

        self.memo[(word1, word2)] = minDistance
        return minDistance

    def shortest(self, word1: str, word2: str) -> int:
        return self.__getDistance(word1, word2)


# Unit Tests
classes = [WordDistance, WordDistance2]


class TestWordDistance(unittest.TestCase):
    def testWordDistance1(self):
        for myclass in classes:
            wordDistance = myclass(
                ["practice", "makes", "perfect", "coding", "makes"])
            self.assertEqual(wordDistance.shortest("coding", "practice"), 3)
            self.assertEqual(wordDistance.shortest("makes", "coding"), 1)


if __name__ == "__main__":
    unittest.main()
