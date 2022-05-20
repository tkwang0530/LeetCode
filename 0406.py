"""
406. Queue reconstruction by Height
You are given an array of people, people, which are the attributes of some people in a queue (not necessarily in order). Each people[i] = [hi, ki] represents the i-th person of height hi with exactly ki other person in front who have a height greater than or equal to hi.

Reconstruct and return the queue that is represented by the input array people.
The returned queue should be formatted as an array qeueu, where queue[j] = [hj, kj] is the attributes of the j-th person in the queue (queue[0] is the person at the front of the queue).

Example1:
Input: people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
Output: [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
Explanation:
Person 0 has height 5 with no other people taller or the same height in front.
Person 1 has height 7 with no other people taller or the same height in front.
Person 2 has height 5 with two persons taller or the same height in front, which is person 0 and 1.
Person 3 has height 6 with one person taller or the same height in front, which is person 1.
Person 4 has height 4 with four people taller or the same height in front, which are people 0, 1, 2, and 3.
Person 5 has height 7 with one person taller or the same height in front, which is person 1.
Hence [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]] is the reconstructed queue.

Example2:
Input: people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
Output: [[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]]

Constraints:
1 <= people.length <= 2000
0 <= hi <= 10^6
0 <= k_i < people.length
It is guaranteed that the queue can be reconstructed.
"""

""" 
Notes:
1. Greedy: O(n^2) time | O(n) space
For each height from tallest to shortest:
    insert the person in the k-th index

if two people with the same height, insert the one with smaller k first
"""

from typing import List
class Solution(object):
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        output = []
        for h, k in sorted(people, key = lambda x: (-x[0], x[1])):
            output.insert(k, [h, k])
        
        return output

# Unit Tests
import unittest
funcs = [Solution().reconstructQueue]

class TestReconstructQueue(unittest.TestCase):
    def testReconstructQueue1(self):
        for func in funcs:
            people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
            self.assertEqual(func(people=people), [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]])

    def testReconstructQueue2(self):
        for func in funcs:
            people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
            self.assertEqual(func(people=people), [[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]])

if __name__ == "__main__":
    unittest.main()
