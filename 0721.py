"""
721. Accounts Merge
description: https://leetcode.com/problems/accounts-merge/description/
"""

"""
Note:
1. Build a undirect email based graph and use DFS to check group: O(nm) time | O(nm) space - where n is the number of account and m is the max length of account
2. UnionFind + HashTable + Sort: O(nm*log(nm)) time | O(nm) space - where n is the number of account and m is the max length of account
"""

from typing import List
import collections
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        result = []
        if not accounts:
            return result
        
        emailToName = dict() # <email, name>
        graph = collections.defaultdict(set) # <email, emailSet>
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

class UnionFind:
    def __init__(self, accounts: List[List[str]]):
        n = sum(len(account) for account in accounts)
        index = 0
        self.idInfoMap = {} # <id, (name, len of emails)>
        self.idEmailMap = {} # <id, email>
        self.emailIdsMap = collections.defaultdict(list) # <email, [id0, id1, ...]>
        for i, account in enumerate(accounts):
            for j, ele in enumerate(account):
                if j == 0:
                    name = account[0]
                    self.idInfoMap[index] = (name, len(account)-1)
                else:
                    self.idEmailMap[index+j] = ele
                    self.emailIdsMap[ele].append(index+j)
            index += len(account)

        self.parents = [i for i in range(n)]
        self.ranks = [1 for _ in range(n)]
        
    def merge(self):
        for index, info in self.idInfoMap.items():
            _, L = info
            for i in range(index+1, index+L+1):
                self.union(i, i-1)
            for _, ids in self.emailIdsMap.items():
                for j in range(1, len(ids)):
                    self.union(ids[j-1], ids[j])
    
    def getName(self, id):
        return self.idInfoMap[id][0]
    
    def find(self, u):
        if self.parents[u] != u:
            self.parents[u] = self.find(self.parents[u])
        return self.parents[u]
     
    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return False
        
        if self.ranks[pu] < self.ranks[pv]:
            self.parents[pu] = pv
        elif self.ranks[pv] < self.ranks[pu]:
            self.parents[pv] = pu
        else:
            self.parents[pv] = pu
            self.ranks[pu] += 1
        return True
    
    def getMembersMap(self):
        members = collections.defaultdict(list)
        for i in range(len(self.parents)):
            members[self.find(i)].append(i)
        return members

class Solution2:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        output = []
        uf = UnionFind(accounts)    
        uf.merge()
        members = uf.getMembersMap()
        visited = set()
        for i in uf.idInfoMap.keys():
            name = uf.getName(i)
            parentId = uf.find(i)
            if parentId in visited:
                continue
            visited.add(parentId)

            emails = set([uf.idEmailMap[mid] for mid in members[parentId] if mid in uf.idEmailMap])
            output.append([name] + sorted(list(emails)))
        return output


# Unit Tests
import unittest
funcs = [Solution().accountsMerge, Solution2().accountsMerge]

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
