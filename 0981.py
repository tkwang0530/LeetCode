"""
981. Time Based Key-Value Store
Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

Implement the TimeMap class:
- TimeMap() Initializes the object of the data structure.
- void set(String key, String value, int timestamp) Stores the key "key" with the value "value" at the given time timestamp.
- String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".

Example1:
Input
["TimeMap", "set", "get", "get", "set", "get", "get"]
[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
Output
[null, null, "bar", "bar", null, "bar2", "bar2"]

Explanation
TimeMap timeMap = new TimeMap();
timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1.
timeMap.get("foo", 1);         // return "bar"
timeMap.get("foo", 3);         // return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along with timestamp = 4.
timeMap.get("foo", 4);         // return "bar2"
timeMap.get("foo", 5);         // return "bar2"
"""

"""
Note:
1. Hash Map + Binary Search:
set: O(n) time | O(1) space
get: O(logn) time | O(1) space
total space: O(n)
where n is the total number of key-value pairs of all time
"""

import collections
class TimeMap:

    def __init__(self):
        self.strTimeDict = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.strTimeDict[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.strTimeDict:
            return ""
        
        left, right = 0, len(self.strTimeDict[key])
        while left < right:
            mid = left + (right-left) // 2
            midTimestamp = self.strTimeDict[key][mid][1]
            if midTimestamp == timestamp:
                return self.strTimeDict[key][mid][0]
            elif midTimestamp > timestamp:
                right = mid
            else:
                left = mid + 1
        return "" if self.strTimeDict[key][left-1][1] > timestamp else self.strTimeDict[key][left-1][0]

# Unit Tests
import unittest

class TestTimeMap(unittest.TestCase):
    def testTimeMap1(self):
        timeMap = TimeMap()
        timeMap.set("foo", "bar", 1)
        self.assertEqual(timeMap.get("foo", 1), "bar")
        self.assertEqual(timeMap.get("foo", 3), "bar")

        timeMap.set("foo", "bar2", 4)
        
        self.assertEqual(timeMap.get("foo", 4), "bar2")
        self.assertEqual(timeMap.get("foo", 5), "bar2")
        self.assertEqual(timeMap.get("foo", 0), "")


if __name__ == "__main__":
    unittest.main()
