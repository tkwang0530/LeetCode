"""
1258. Synonymous Sentences
You are given a list of equivalent string pairs synonym where synonyms[i] = [s_i, t_i] indicates that s_i and t_i are equivalent strings. You are also given a sentence text.

Return all possible synonymous sentences sorted lexicographically

Example1:
Input: synonyms = [["happy","joy"],["sad","sorrow"],["joy","cheerful"]], text = "I am happy today but was sad yesterday"
Output: ["I am cheerful today but was sad yesterday","I am cheerful today but was sorrow yesterday","I am happy today but was sad yesterday","I am happy today but was sorrow yesterday","I am joy today but was sad yesterday","I am joy today but was sorrow yesterday"]


Example2:
Input: synonyms = [["happy","joy"],["cheerful","glad"]], text = "I am happy today but was sad yesterday"
Output: ["I am happy today but was sad yesterday","I am joy today but was sad yesterday"]

Constraints:
0 <= synonyms.length <= 10
synonyms[i].length == 2
1 <= s_i.length, t_i.length <= 10
s_i != t_i
text consists of at most 10 words.
The words of text are separated by single spaces.
"""

"""
Note:
1. UnionFind + dp: O(nlogn) time | O(n) space
"""


from  typing import List
import collections
class UnionFind:
    def __init__(self):
        self.parents = {}
        self.ranks = {}

    def add(self, u):
        if u in self.parents:
            return
        self.parents[u] = u
        self.ranks[u] = 1

    def find(self, u):
        if u != self.parents[u]:
            self.parents[u] = self.find(self.parents[u])
        return self.parents[u]

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return
        ru, rv = self.parents[pu], self.parents[pv]
        if ru < rv:
            self.parents[pu] = pv
        elif rv < ru:
            self.parents[pv] = pu
        else:
            self.parents[pu] = pv
            self.ranks[pv] += 1


class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        unionFind = UnionFind()
        for word1, word2 in synonyms:
            unionFind.add(word1)
            unionFind.add(word2)
            unionFind.union(word1, word2)

        group = collections.defaultdict(set)
        for word1, word2 in synonyms:
            p1, p2 = unionFind.find(word1), unionFind.find(word2)
            group[p1].add(word1)
            group[p2].add(word2)
        
        for key in group.keys():
            group[key] = sorted(list(group[key]))
        
        text = text.split(' ')
        preCharsArr = [[]]
        for i in range(len(text)):
            word = text[i]
            
            if word not in unionFind.parents:
                length = len(preCharsArr)
                for j in range(length):
                    
                    preCharsArr[j].append(word)
                continue
            
            currentCharsArr = []
            for childWord in group[unionFind.find(word)]:
                for preChars in preCharsArr:
                    currentChars = preChars.copy()
                    currentChars.append(childWord)
                    currentCharsArr.append(currentChars)
            preCharsArr = currentCharsArr

        for i in range(len(preCharsArr)):
            preCharsArr[i] = " ".join(preCharsArr[i])
        
        preCharsArr.sort()
        return preCharsArr

# Unit Tests
import unittest
funcs = [Solution().generateSentences]

class TestGenerateSentences(unittest.TestCase):
    def testGenerateSentences1(self):
        for func in funcs:
            synonyms = [["happy","joy"],["sad","sorrow"],["joy","cheerful"]]
            text = "I am happy today but was sad yesterday"
            expect = ["I am cheerful today but was sad yesterday","I am cheerful today but was sorrow yesterday","I am happy today but was sad yesterday","I am happy today but was sorrow yesterday","I am joy today but was sad yesterday","I am joy today but was sorrow yesterday"]
            self.assertEqual(func(synonyms=synonyms, text=text), expect)

    def testGenerateSentences2(self):
        for func in funcs:
            synonyms = [["happy","joy"],["cheerful","glad"]]
            text = "I am happy today but was sad yesterday"
            expect = ["I am happy today but was sad yesterday","I am joy today but was sad yesterday"]
            self.assertEqual(func(synonyms=synonyms, text=text), expect)

    def testGenerateSentences3(self):
        for func in funcs:
            synonyms = [["a","b"],["b","c"],["d","e"],["c","d"]]
            text = "a b"
            expect = ["a a","a b","a c","a d","a e","b a","b b","b c","b d","b e","c a","c b","c c","c d","c e","d a","d b","d c","d d","d e","e a","e b","e c","e d","e e"]
            self.assertEqual(func(synonyms=synonyms, text=text), expect)

if __name__ == "__main__":
    unittest.main()
