"""
451. Sort Characters By Frequency
Given a string s, sort it in decreasing order based on the frequency of the characters.
The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.

Example1:
Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

Example2:
Input: s = "cccaaa"
Output: "aaaccc"
Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
Note that "cacaca" is incorrect, as the same characters must be together.

Example3:
Input: s = "Aabb"
Output: "bbAa"
Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.

Constraints:
1 <= s.length <= 5*10^5
s consists of uppercase and lowercase English letters and digits
"""

"""
Note:
1. maxHeap: O(n+wlogw) time | O(n) space - where n is the length of given string s and w is the number of distinct char in s
(1) store the char count using collections.Counter(s)
(2) using a maxHeap with (-count, char)
(3) for each run, pop items out and append the char "count" times into the result array (chars), until the maxHeap is empty
(4) return "".join(chars)

2. bucket sort: O(26n) time | O(n) space - where n is the length of given string s and w is the number of distinct char in s

3. hashTable + sort: O(n+wlogw) time | O(1) space - where n is the length of given string s and w is the number of distinct char in s
"""
import collections
import heapq
class Solution:
    def frequencySort(self, s: str) -> str:
        charCount = collections.Counter(s)
        maxHeap = []
        for char, count in charCount.items():
            heapq.heappush(maxHeap, (-1*count, char))
        
        chars = []
        while len(maxHeap) > 0:
            item = heapq.heappop(maxHeap)
            count = -1 * item[0]
            char = item[1]
            chars.append(char * count)
        return "".join(chars)

    def frequencySort2(self, s: str) -> str:
        charCount = collections.Counter(s)
        bucket = [[] for _ in range(len(s) + 1)]
        maxCount = float("-inf")
        for char, count in charCount.items():
            bucket[count].append(char)
            maxCount = max(maxCount, count)
        
        characters = []
        for count in range(maxCount, -1, -1):
            chars = bucket[count]
            for char in chars:
                characters.append(count * char)
        return "".join(characters)

    def frequencySort3(self, s: str) -> str:
        charCounts = collections.Counter(s)
        countCharsArr = [(count, char*count) for char, count in charCounts.items()]
        result = []
        
        countCharsArr.sort(reverse=True)
        for _, chars in countCharsArr:
            result.append(chars)
        
        return "".join(result)


# Unit Tests
import unittest
funcs = [Solution().frequencySort, Solution().frequencySort2, Solution().frequencySort3]


class TestFrequencySort(unittest.TestCase):
    def testFrequencySort1(self):
        for func in funcs:
            s = "tree"
            self.assertTrue(func(s=s) in ("eetr", "eert"))

    def testFrequencySort2(self):
        for func in funcs:
            s = "cccaaa"
            self.assertTrue(func(s=s) in ("aaaccc", "cccaaa"))

    def testFrequencySort3(self):
        for func in funcs:
            s = "Aabb"
            self.assertTrue(func(s=s) in ("bbAa", "bbaA"))

if __name__ == "__main__":
    unittest.main()
