"""
911. Online Election
You are given two integer arrays persons and times. In an election, the i-th vote was cast for persons[i] at time times[i]

For each query at a time t, find the person that was leading the election at time t. Votes cast at time t will count towards our query. In the case of a tie, the most recent vote (among tied candidates) wins.

Implement the TopVotedCandidate class:
- TopVotedCandidate(int[] persons, int[] times) Initializes the object with the persons and times arrays.
- int q(int t) Returns the number of the person that was leading the election at time t according to the mentioned rules.

Example1:
Input
["TopVotedCandidate", "q", "q", "q", "q", "q", "q"]
[[[0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30]], [3], [12], [25], [15], [24], [8]]
Output
[null, 0, 1, 1, 0, 0, 1]

Explanation
TopVotedCandidate topVotedCandidate = new TopVotedCandidate([0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30]);
topVotedCandidate.q(3); // return 0, At time 3, the votes are [0], and 0 is leading.
topVotedCandidate.q(12); // return 1, At time 12, the votes are [0,1,1], and 1 is leading.
topVotedCandidate.q(25); // return 1, At time 25, the votes are [0,1,1,0,0,1], and 1 is leading (as ties go to the most recent vote.)
topVotedCandidate.q(15); // return 0
topVotedCandidate.q(24); // return 0
topVotedCandidate.q(8); // return 1
"""

"""
Note:
1. HashTable:
__init__: O(n) time | O(n) space
q: O(logn) time | O(1) space
where n is the length of persons
"""




import bisect
from typing import List
import unittest
import collections
class TopVotedCandidate:

    # __init__ Initializes the object with the persons and times arrays
    def __init__(self, persons: List[int], times: List[int]):
        personVotes = collections.defaultdict(int)
        self.leadingPeople = []
        maxVotes = float("-inf")
        for person in persons:
            personVotes[person] += 1
            candidate = self.leadingPeople[-1] if self.leadingPeople else -1
            if personVotes[person] >= maxVotes:
                candidate = person
                maxVotes = max(maxVotes, personVotes[person])
            self.leadingPeople.append(candidate)
        self.times = times

    # Returns the number of the person that was leading the election at time t according to the mentioned rules.
    def q(self, t: int) -> int:
        idx = bisect.bisect_left(self.times, t)
        return self.leadingPeople[idx] if idx < len(self.times) and self.times[idx] == t else self.leadingPeople[idx-1]


# Unit Tests


class TestTopVotedCandidate(unittest.TestCase):
    def testTopVotedCandidate1(self):
        topVotedCandidate = TopVotedCandidate(
            [0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30])
        self.assertEqual(topVotedCandidate.q(3), 0)
        self.assertEqual(topVotedCandidate.q(12), 1)
        self.assertEqual(topVotedCandidate.q(25), 1)
        self.assertEqual(topVotedCandidate.q(15), 0)
        self.assertEqual(topVotedCandidate.q(24), 0)
        self.assertEqual(topVotedCandidate.q(8), 1)


if __name__ == "__main__":
    unittest.main()
