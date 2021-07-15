"""
71. Simplify Path
Given a string path, which is an absolute path (starting with a slash '/') to a file or directory in a Unix-style file system, convert it to the simplified canonical path.

In a Unix-style file system, a period '.' refers to the current directory, a double period '..' refers to the directory up a level, and any multiple consecutive slashes (i.e. '//') are treated as a single slash '/'. For this problem, any other format of periods such as '...' are treated as file/directory names.

The canonical path should have the following format:
- The path starts with a single slash '/'.
- Any two directories are separated by a single slash '/'.
- The path does not end with a trailing '/'.
- The path only contains the directories on the path from the root directory to the target file or directory (i.e., no period '.' or double period '..')

Example1:
Input: path = "/home/"
Output: "/home"
Explanation: Note that there is no trailing slash after the last directory name.

Example2:
Input: path = "/../"
Output: "/"
Explanation: Going one level up from the root directory is a no-op, as the root level is the highest level you can go.

Example3:
Input: path = "/home//foo/"
Output: "/home/foo"
Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.

Example4:
Input: path = "/a/./b/../../c/"
Output: "/c"

Constraints:
1 <= path.length <= 3000
path consists of English letters, digits, period '.', slash '/' or '_'.
path is a valid absolute Unix path.
"""

"""
Note:
1. Using Stack: O(n) time | O(n) space
2. Using Stack (improved): O(n) time | O(n) space
"""




import unittest
class Solution:
    def simplifyPath(self, path: str) -> str:
        specials = {"..", ".", ""}
        stack = []
        for token in path.split("/"):
            if token == ".." and len(stack) > 0:
                stack.pop()
            elif not token in specials:
                stack.append(token)
        return "/" if not stack else "/" + "/".join(stack)

    def simplifyPath2(self, path: str) -> str:
        specials = {"..", ".", ""}
        stack = [""] if path[0] == "/" else []
        for token in path.split("/"):
            if token == ".." and stack and stack[-1] != "":
                stack.pop()
            elif token not in specials:
                stack.append(token)
        return "/" if len(stack) == 1 and stack[0] == "" else "/".join(stack)


# Unit Tests
funcs = [Solution().simplifyPath, Solution().simplifyPath2]


class TestSimplifyPath(unittest.TestCase):
    def testSimplifyPath1(self):
        for func in funcs:
            self.assertEqual(func(path="/home/"), "/home")

    def testSimplifyPath2(self):
        for func in funcs:
            self.assertEqual(func(path="/../"), "/")

    def testSimplifyPath3(self):
        for func in funcs:
            self.assertEqual(func(path="/home//foo/"), "/home/foo")

    def testSimplifyPath4(self):
        for func in funcs:
            self.assertEqual(func(path="/a/./b/../../c/"), "/c")


if __name__ == "__main__":
    unittest.main()
