"""
588. Design In-Memory File System
Design a data structure that simulates an in-memory file system.

Implement the FileSystem class:
- FileSystem() Initializes the object of the system.
- List<String> ls(String path)
    If path is a file path, returns a list that only contains this file's name.
    If path is a directory path, returns the list of file and directory names in this directory.

The answer should in lexicographic order.
- void mkdir(String path) Makes a new directory according to the given path. The given directory path does not exist. If the middle directories in the path do not exist, you should create them as well.
- void addContentToFile(String filePath, String content)
    If filePath does not exist, creates that file containing given content.
    If filePath already exists, appends the given content to original content.
- String readContentFromFile(String filePath) Returns the content in the file at filePath

Example1:
Input
["FileSystem", "ls", "mkdir", "addContentToFile", "ls", "readContentFromFile"]
[[], ["/"], ["/a/b/c"], ["/a/b/c/d", "hello"], ["/"], ["/a/b/c/d"]]
Output
[null, [], null, null, ["a"], "hello"]

Explanation
FileSystem fileSystem = new FileSystem();
fileSystem.ls("/");                         // return []
fileSystem.mkdir("/a/b/c");
fileSystem.addContentToFile("/a/b/c/d", "hello");
fileSystem.ls("/");                         // return ["a"]
fileSystem.readContentFromFile("/a/b/c/d"); // return "hello"

Constraints:
1 <= path.length, filePath.length <= 100
path and filePath are absolute paths which begin with '/' and do not end with '/' except that path is just '/'.
You can assume that all directory names and file names only contain lowercase letters, and the same names will not exist in the same directory.
You can assume that all operations will be passed valid parameters, and users will not attempt to retrieve file content or list a directory or file that does not exist.
1 <= content.length <= 50
At most 300 calls will be made to ls, mkdir, addContentToFile, and readContentFromFile.
"""

"""
Note:
1. Nested HashTable (Trie Concept)
all methods are O(1) time | O(1) space
except for ls O(n) time | O(n) space
where n is the depth of the path
"""
from typing import List
class File:
    def __init__(self, name, content=""):
        self.type = 0 # 0 indicates file
        self.name = name
        self.content = content

class Directory:
    def __init__(self, name):
        self.type = 1 # 1 indicates directory
        self.name = name
        self.list = {} # name:<File> or name:<Directory>

class FileSystem:

    def __init__(self):
        self.pathMap = {"/": Directory("/")} #path:<File> or path:<Directory>

    def ls(self, path: str) -> List[str]:
        # if path is a file path, returns a list that only contains this file's name.
        if self.pathMap[path].type == 0:
            return [self.pathMap[path].name]
        else:
            # if path is a directory path, returns the list of file and directory names in this directory in lexicographic order
            return sorted(list(self.pathMap[path].list.keys()))

    def mkdir(self, path: str) -> None:
        temp = path.split("/")
        node = self.pathMap["/"]
        currentPath = [""]
        for i in range(len(temp)-1):
            name = temp[i+1]
            currentPath.append(name)
            if name not in node.list:
                directory = Directory(name)
                node.list[name] = directory
                self.pathMap["/".join(currentPath)] = directory
            node = node.list[name]

    def addContentToFile(self, filePath: str, content: str) -> None:
        # If filePath does not exist, creates that file containing given content.
        if filePath not in self.pathMap:
            temp = filePath.split("/")
            name = temp.pop()
            parentPath = "/".join(temp)
            file = File(name, content)
            if parentPath == "":
                parentPath = "/"
            self.pathMap[parentPath].list[name] = file
            self.pathMap[filePath] = file
        else:
            # If filePath already exists, appends the given content to original content.
            self.pathMap[filePath].content += content

    def readContentFromFile(self, filePath: str) -> str:
        return self.pathMap[filePath].content
# Unit Tests
import unittest
classes = [FileSystem]

class TestFileSystem(unittest.TestCase):
    def testFileSystem1(self):
        for myclass in classes:
            fileSystem = myclass()
            self.assertEqual(fileSystem.ls('/'), [])
            fileSystem.mkdir("/a/b/c")
            fileSystem.addContentToFile("/a/b/c/d", "hello")
            self.assertEqual(fileSystem.ls("/"), ["a"])
            self.assertEqual(fileSystem.readContentFromFile("/a/b/c/d"), "hello")

if __name__ == "__main__":
    unittest.main()
