"""
609. Find Duplicate File in System
Given a list paths of directory info, including the directory path, and all the files with contents in this directory, return all the duplicate files in the file system in terms of their paths. You may return the answer in any order.

A group of duplicate files consists of at least two files that have the same content.

A single of duplicate info string in the input list has the following format:
- "root/d1/d2/.../dm f1.txt(f1_content) f2.txt(f2_content) ... fn.txt(fn_content)"

It means there are n files (f1.txt, f2.txt ... fn.txt) with content (f1_content, f2_content ... fn_content) respectively in the directory "root/d1/d2/.../dm". Note that n >= 1 and m >= 0. If m = 0, it means the directory is just the root directory.

The output is a list of groups of duplicate file paths. For each group, it contains all the file paths of the files that have the same content. A file path is a string that has the following format:
- "directory_path/file_name.txt"

Example1:
Input: paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]
Output: [["root/a/2.txt","root/c/d/4.txt","root/4.txt"],["root/a/1.txt","root/c/3.txt"]]

Example2:
Input: paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)"]
Output: [["root/a/2.txt","root/c/d/4.txt"],["root/a/1.txt","root/c/3.txt"]]

Constraints:
1 <= paths.length <= 2 * 10^4
1 <= paths[i].length <= 3000
1 <= sum(paths[i].length) <= 5 * 10^5
paths[i] consist of English letters, digits, '/', '.', '(', ')', and ' '.
You may assume no files or directories share the same name in the same directory.
You may assume each given directory info represents a unique directory.
A single blank space separates the directory path and file info.

Follow up:
- Imagine you are given a real file system, how will you search files? DFS or BFS?
- If the file content is very large (GB level), how will you modify your solution?
- If you can only read the file by 1kb each time, how will you modify your solution?
- What is the time complexity of your modified solution? What is the most time-consuming part and memory-consuming part of it? How to optimize?
- How to make sure the duplicated files you find are not false positive?
"""

""" 
1. HashMap: O(n) time | O(n) space - where n is the number of files

follow up:
1. DFS
2. make use of meta data, like file size before really reading large content
3. In GFS, it stores large file in multiple "chunks" (one chunk is 64KB). we have meta data, including the file size, file name and index of different chunks along with each chunk's checkSum(the xor for the content). For step-2, we just compare each file's checkSum.
Disadvantage: there might be flase positive duplicates, because two different files might share the same checkSum.
4. hashing part is the most time-consuming and memory consuming. optimize as above mentioned, but also false positive issue.
5. Question-2-Answer-1 will avoid it. We need to compare the content chunk by chunk when we find two "duplicates" using checkSum.
"""

import collections
from typing import List
class Solution(object):
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        contentFilePathsMap = collections.defaultdict(list)
        for line in paths:
            dirPath, *filesElement = line.split(' ')
            for fileElement in filesElement:
                fileName, content = fileElement[:-1].split('(')
                filePath = dirPath + '/' + fileName
                contentFilePathsMap[content].append(filePath)
        return [paths for paths in contentFilePathsMap.values() if len(paths) >= 2]


# Unit Tests
import unittest
funcs = [Solution().findDuplicate]

class TestFindDuplicate(unittest.TestCase):
    def testFindDuplicate1(self):
        for func in funcs:
            paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]
            output = func(paths=paths)
            expectOutput = [["root/a/2.txt","root/c/d/4.txt","root/4.txt"],["root/a/1.txt","root/c/3.txt"]]
            self.assertEqual(len(output), len(expectOutput))
            expectSetArr = [set(expectOutputGroup) for expectOutputGroup in expectOutput]
            for outputGroup in output:
                self.assertTrue(set(outputGroup) in expectSetArr)

    def testFindDuplicate2(self):
        for func in funcs:
            paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)"]
            output = func(paths=paths)
            expectOutput = [["root/a/2.txt","root/c/d/4.txt"],["root/a/1.txt","root/c/3.txt"]]
            self.assertEqual(len(output), len(expectOutput))
            expectSetArr = [set(expectOutputGroup) for expectOutputGroup in expectOutput]
            for outputGroup in output:
                self.assertTrue(set(outputGroup) in expectSetArr)

    def testFindDuplicate3(self):
        for func in funcs:
            paths = ["root/a 1.txt(abcd) 2.txt(efsfgh)","root/c 3.txt(abdfcd)","root/c/d 4.txt(efggdfh)"]
            output = func(paths=paths)
            expectOutput = []
            self.assertEqual(len(output), len(expectOutput))
            expectSetArr = [set(expectOutputGroup) for expectOutputGroup in expectOutput]
            for outputGroup in output:
                self.assertTrue(set(outputGroup) in expectSetArr)

if __name__ == "__main__":
    unittest.main()
