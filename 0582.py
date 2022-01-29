"""
582. Kill Process
You have n processes forming a rooted tree structure. You are given two integer arrays pid and ppid, where pid[i] is the ID of the ith process and ppid[i] is the ID of the ith process's parent process.

Each process has only one parent process but may have multiple children processes. Only one process has ppid[i] = 0, which means this process has no parent process (the root of the tree).

When a process is killed, all of its children processes will also be killed.

Given an integer kill representing the ID of a process you want to kill, return a list of the IDs of the processes that will be killed. You may return the answer in any order.

Example1:
Input: pid = [1,3,10,5], ppid = [3,0,5,3], kill = 5
Output: [5,10]
Explanation: The processes colored in red are the processes that should be killed.

Example2:
Input: pid = [1], ppid = [0], kill = 1
Output: [1]

Constraints:
n == pid.length
n == ppid.length
1 <= n <= 5 * 10^4
1 <= pid[i] <= 5 * 10^4
0 <= ppid[i] <= 5 * 10^4
Only one process has no parent.
All the values of pid are unique.
kill is guaranteed to be in pid.
"""

"""
Note:
1. BFS: O(n) time | O(n) space
"""

from typing import List
import collections

class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        subprocessMap = collections.defaultdict(list)
        for i, process in enumerate(ppid):
            if process == 0:
                continue
            subprocessMap[process].append(pid[i])
            
        queue = collections.deque([kill])
        result = []
        while queue:
            process = queue.popleft()
            result.append(process)
            
            for subprocess in subprocessMap[process]:
                queue.append(subprocess)
        
        return result


# Unit Tests
import unittest
funcs = [Solution().killProcess]

class TestKillProcess(unittest.TestCase):
    def testKillProcess1(self):
        for func in funcs:
            pid = [1,3,10,5]
            ppid = [3,0,5,3]
            kill = 5
            self.assertEqual(func(pid=pid, ppid=ppid, kill=kill), [5, 10])

    def testKillProcess2(self):
        for func in funcs:
            pid = [1]
            ppid = [0]
            kill = 1
            self.assertEqual(func(pid=pid, ppid=ppid, kill=kill), [1])


if __name__ == "__main__":
    unittest.main()