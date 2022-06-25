"""
1472. Design Browser History
You have a browser of one tab where you start on the homepage and you can visit another url, get back in the history number of steps or move forward in the history number of steps.

Implement the BrowserHistory class:
- BrowserHistory(string homepage) Initializes the object with the homepage of the browser.
- void visit(string url) Visits url from the current page. It clears up all the forward history.
- string back(int steps) Move steps back in history. If you can only return x steps in the history and steps > x, you will return only x steps. Return the current url after moving back in history at most steps.
- string forward(int steps) Move steps forward in history. If you can only forward x steps in the history and steps > x, you will forward only x steps. Return the current url after forwarding in history at most steps.

Example1:
Input:
["BrowserHistory","visit","visit","visit","back","back","forward","visit","forward","back","back"]
[["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],["linkedin.com"],[2],[2],[7]]
Output:
[null,null,null,null,"facebook.com","google.com","facebook.com",null,"linkedin.com","google.com","leetcode.com"]

Explanation:
BrowserHistory browserHistory = new BrowserHistory("leetcode.com");
browserHistory.visit("google.com");       // You are in "leetcode.com". Visit "google.com"
browserHistory.visit("facebook.com");     // You are in "google.com". Visit "facebook.com"
browserHistory.visit("youtube.com");      // You are in "facebook.com". Visit "youtube.com"
browserHistory.back(1);                   // You are in "youtube.com", move back to "facebook.com" return "facebook.com"
browserHistory.back(1);                   // You are in "facebook.com", move back to "google.com" return "google.com"
browserHistory.forward(1);                // You are in "google.com", move forward to "facebook.com" return "facebook.com"
browserHistory.visit("linkedin.com");     // You are in "facebook.com". Visit "linkedin.com"
browserHistory.forward(2);                // You are in "linkedin.com", you cannot move forward any steps.
browserHistory.back(2);                   // You are in "linkedin.com", move back two steps to "facebook.com" then to "google.com". return "google.com"
browserHistory.back(7);                   // You are in "google.com", you can move back only one step to "leetcode.com". return "leetcode.com"

Constraints:
1 <= homepage.length <= 20
1 <= url.length <= 20
1 <= steps <= 100
homepage and url consist of '.' or lower case English letters.
At most 5000 calls will be made to visit, back, and forward.
"""

"""
Note:
1. Singly LinkedList + HashTable
All methods are O(1) time and O(1) space
"""
class ListNode:
    def __init__(self, order: int, url: str) -> None:
        self.order = order
        self.url = url
        self.next = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.dummyHead = ListNode(0, "")
        self.current = self.dummyHead
        self.orderNodeMap = {}
        self.visit(homepage)
        
    def visit(self, url: str) -> None:
        self.current.next = ListNode(self.current.order+1, url)
        self.current = self.current.next
        self.maxOrder = self.current.order
        self.orderNodeMap[self.current.order] = self.current
        
    def back(self, steps: int) -> str:
        if self.current.order - steps <= 0:
            self.current = self.orderNodeMap[1]
            return self.current.url

        self.current = self.orderNodeMap[self.current.order-steps]
        return self.current.url
        
    def forward(self, steps: int) -> str:
        if self.current.order + steps > self.maxOrder:
            self.current = self.orderNodeMap[self.maxOrder]
            return self.current.url

        self.current = self.orderNodeMap[self.current.order+steps]
        return self.current.url

# Unit Tests
import unittest
classes = [BrowserHistory]

class TestBrowserHistory(unittest.TestCase):
    def testBrowserHistory1(self):
        for myclass in classes:
            browserHistory = myclass("leetcode.com")

            # You are in "leetcode.com". Visit "google.com"
            browserHistory.visit("google.com")

            # You are in "google.com". Visit "facebook.com"
            browserHistory.visit("facebook.com")

            # You are in "facebook.com". Visit "youtube.com"
            browserHistory.visit("youtube.com")

            # You are in "youtube.com", move back to "facebook.com" return "facebook.com"
            self.assertEqual(browserHistory.back(1), "facebook.com")

            # You are in "facebook.com", move back to "google.com" return "google.com"
            self.assertEqual(browserHistory.back(1), "google.com") 

            # You are in "google.com", move forward to "facebook.com" return "facebook.com"
            self.assertEqual(browserHistory.forward(1), "facebook.com")

            # You are in "facebook.com". Visit "linkedin.com"
            browserHistory.visit("linkedin.com")

            # You are in "linkedin.com", you cannot move forward any steps.
            self.assertEqual(browserHistory.forward(2), "linkedin.com")

            # You are in "linkedin.com", move back two steps to "facebook.com" then to "google.com". return "google.com"
            self.assertEqual(browserHistory.back(2), "google.com")

            # You are in "google.com", you can move back only one step to "leetcode.com". return "leetcode.com"
            self.assertEqual(browserHistory.back(7), "leetcode.com")

if __name__ == "__main__":
    unittest.main()
