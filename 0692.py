"""
692. Top K Frequent Words
Given an array of strings words and an integer k, return the k most frequent strings.

Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.

Example1:
Input: words = ["i","love","leetcode","i","love","coding"], k = 2
Output: ["i","love"]
Explanation: "i" and "love" are the two most frequent words.
Note that "i" comes before "love" due to a lower alphabetical order.

Example2:
Input: words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
Output: ["the","is","sunny","day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words, with the number of occurrence being 4, 3, 2 and 1 respectively.

Constraints:
1 <= words.length <= 500
1 <= words[i] <= 10
words[i] consists of lowercase English letters.
k is in the range [1, The number of unique words[i]]

Follow-up: Could you solve it in O(nlogk) time and O(n) extra space?
"""

"""
Note:
1. Buckets + Hash Table: O(n+k) time | O(n) space
2. minHeap + Hash Table: O(n+nlogk+klogk) time | O(k) space
"""

import collections
import heapq
from typing import List
class ReverseWordOrder:
    def __init__(self, word):
        self.word = word
    
    def __lt__(self, other):
        # flipping the lesser than comparator for our purpose to keep greater word in heap
        return self.word > other.word

class Solution(object):
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        wordCount = {} # <word, count>
        buckets = [[] for _ in range(len(words)+1)]
        for word in words:
            wordCount[word] = wordCount.get(word, 0) + 1
        for word, count in wordCount.items():
            buckets[count].append(word)
        
        count = len(words)
        result = []
        while count >= 0:
            buckets[count].sort()
            for word in buckets[count]:
                result.append(word)
                if len(result) == k:
                    return result
            count -= 1
        return result

    
    def topKFrequent2(self, words: List[str], k: int) -> List[str]:
        counter = collections.Counter(words)
        minHeap = []
        for word, count in counter.items():
            if len(minHeap) < k:
                heapq.heappush(minHeap, (count, ReverseWordOrder(word)))
            else:
                heapq.heappushpop(minHeap, (count, ReverseWordOrder(word)))
        result = []
        while minHeap:
            _, reverseWordOrder = heapq.heappop(minHeap)
            result.append(reverseWordOrder.word)
        return result[::-1]


# Unit Tests
import unittest
funcs = [Solution().topKFrequent, Solution().topKFrequent2]

class TestTopKFrequent(unittest.TestCase):
    def testTopKFrequent1(self):
        for func in funcs:
            words = ["i","love","leetcode","i","love","coding"]
            k = 2
            self.assertEqual(func(words=words, k=k), ["i","love"])

    def testTopKFrequent2(self):
        for func in funcs:
            words = ["the","day","is","sunny","the","the","the","sunny","is","is"]
            k = 4
            self.assertEqual(func(words=words, k=k), ["the","is","sunny","day"])

if __name__ == "__main__":
    unittest.main()
