"""
359. Logger Rate Limiter
desscription: https://leetcode.com/problems/logger-rate-limiter/description/
"""

"""
Note:
1. Hashtable: O(1) time | O(n) space - where n is the number of unique messages
"""

import unittest
class Logger:
    # Initializes the logger object.
    def __init__(self):
        self.lookup = {}
        

    # Returns true if the message should be printed in the given timestamp, otherwise returns false.
    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.lookup:
            self.lookup[message] = timestamp
            return True

        lastTimestamp = self.lookup[message]
        if timestamp >= lastTimestamp+10:
            self.lookup[message] = timestamp
            return True
        else:
            return False
        
        

# Unit Tests
classes = [Logger]

class TestLogger(unittest.TestCase):
    def testLogger1(self):
        for myclass in classes:
            logger = Logger()
            self.assertEqual(logger.shouldPrintMessage(1, "foo"), True) # return true, next allowed timestamp for "foo" is 1 + 10 = 11
            self.assertEqual(logger.shouldPrintMessage(2, "bar"), True) # return true, next allowed timestamp for "bar" is 2 + 10 = 12
            self.assertEqual(logger.shouldPrintMessage(3, "foo"), False) # 3 < 11, return false
            self.assertEqual(logger.shouldPrintMessage(8, "bar"), False)
            self.assertEqual(logger.shouldPrintMessage(10, "foo"), False)
            self.assertEqual(logger.shouldPrintMessage(11, "foo"), True)

if __name__ == "__main__":
    unittest.main()
