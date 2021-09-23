"""
721. Accounts Merge
Given a list of accounts where each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common email to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format:
- The first element of each account is the name, and the rest of the elements are emails in sorted order.
- The account themselves can be returned in any order.

Example1:
Input: accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
Output: [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
Explanation:
The first and second John's are the same person as they have the common email "johnsmith@mail.com".
The third John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'], 
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.

Example2:
Input: accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]
Output: [["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]]

Constraints:
1 <= accounts.length <= 1000
2 <= accounts[i].length <= 10
1 <= accounts[i][j] <= 30
accounts[i][0] consists of English letters.
accounts[i][j] (for j > 0) is a valid email.
"""

"""
Note:
1. Build a undirect email based graph and use DFS to check group: O(nm) time | O(nm) space - where n is the number of account and m is the max length of account
"""

from collections import defaultdict
from typing import List
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        result = []
        if not accounts:
            return result
        
        emailToName = dict() # <email, name>
        graph = defaultdict(set) # <email, emailSet>
        visited = set() # visited email set for dfs

        for account in accounts:
            name = account[0]
            for i in range(1, len(account)):
                email = account[i]
                emailToName[email] = name
                if i == 1: continue

                # link the email with its neighbor email
                graph[account[i-1]].add(email)
                graph[email].add(account[i-1])
            
        for email in emailToName.keys():
            if email not in visited:
                visited.add(email)
                temp = []
                temp.append(email)
                self.dfs(email, graph, visited, temp)
                result.append([emailToName[email]] + sorted(temp))
        return result

    def dfs(self, email: str, graph: dict[str, set], visited: set, temp: List[str]) -> None:
        for neighbor in graph[email]:
            if neighbor not in visited:
                visited.add(neighbor)
                temp.append(neighbor)
                self.dfs(neighbor, graph, visited, temp)


# Unit Tests
import unittest
funcs = [Solution().accountsMerge]

class TestAccountsMerge(unittest.TestCase):
    def testAccountsMerge1(self):
        for func in funcs:
            accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
            self.assertEqual(sorted(func(accounts=accounts)), sorted([["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]))

    def testAccountsMerge2(self):
        for func in funcs:
            accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]
            self.assertEqual(sorted(func(accounts=accounts)), sorted([["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]]))

if __name__ == "__main__":
    unittest.main()
