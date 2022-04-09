"""
1366. Rank Teams by Votes
In a special ranking system, each voter gives a rank from highest to lowest to all teams participated in the competition.

The ordering of teams is decided by who received the most position-one votes. If two or more teams tie in the first position, we consider the second position to resolve the conflict, if they tie again, we continue this process until the ties are resolved. If two or more teams are still tied after considering all positions, we rank them alphabetically based on their team letter.

Given an array of strings votes which is the votes of all voters in the ranking systems.
Sort all teams according to the ranking system described above.

Return a string of all teams sorted by the ranking system.

Example1:
Input: votes = ["ABC","ACB","ABC","ACB","ACB"]
Output: "ACB"
Explanation: Team A was ranked first place by 5 voters. No other team was voted as first place so team A is the first team.
Team B was ranked second by 2 voters and was ranked third by 3 voters.
Team C was ranked second by 3 voters and was ranked third by 2 voters.
As most of the voters ranked C second, team C is the second team and team B is the third.

Example2:
Input: votes = ["WXYZ","XYZW"]
Output: "XWYZ"
Explanation: X is the winner due to tie-breaking rule. X has same votes as W for the first position but X has one vote as second position while W doesn't have any votes as second position.

Example3:
Input: votes = ["ZMNAGUEDSJYLBOPHRQICWFXTVK"]
Output: "ZMNAGUEDSJYLBOPHRQICWFXTVK"
Explanation: Only one voter so his votes are used for the ranking.

Constraints:
1 <= votes.length <= 1000
1 <= votes[i].length <= 26
votes[i].length == votes[j].length for 0 <= i, j < votes.length.
votes[i][j] is an English uppercase letter.
All characters of votes[i] are unique.
All the characters that occur in votes[0] also occur in votes[j] where 1 <= j < votes.length.
s consists only of lowercase English letters.
"""

""" 
1. HashTable: O(26n) time | O(1) space
"""
from typing import List
import collections
class Solution(object):
    def rankTeams(self, votes: List[str]) -> str:
        teamVotes = collections.defaultdict(list)
        for team in votes[0]:
            teamVotes[team] = [0] * len(votes[0])
            teamVotes[team].append(-1*ord(team))
        for vote in votes:
            for i, team in enumerate(vote):
                teamVotes[team][i] += 1
        return "".join(sorted(votes[0], key=lambda team: tuple(teamVotes[team]), reverse=True))



# Unit Tests
import unittest
funcs = [Solution().rankTeams]


class TestRankTeams(unittest.TestCase):
    def testRankTeams1(self):
        for func in funcs:
            votes = ["ABC","ACB","ABC","ACB","ACB"]
            self.assertEqual(func(votes=votes), "ACB")

    def testRankTeams2(self):
        for func in funcs:
            votes = ["WXYZ","XYZW"]
            self.assertEqual(func(votes=votes), "XWYZ")
    
    def testRankTeams3(self):
        for func in funcs:
            votes = ["ZMNAGUEDSJYLBOPHRQICWFXTVK"]
            self.assertEqual(func(votes=votes), "ZMNAGUEDSJYLBOPHRQICWFXTVK")

    def testRankTeams4(self):
        for func in funcs:
            votes = ["BCA","CAB","CBA","ABC","ACB","BAC"]
            self.assertEqual(func(votes=votes), "ABC")

if __name__ == "__main__":
    unittest.main()
