"""
355. Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see the 10 most recent tweets in the user's news feed.

Implement the Twitter class:
- Twitter() Initializes your twitter object.
- void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId. Each call to this function will be made with a unique tweetId.
- List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user themself. Tweets must be ordered from most recent to least recent.
- void follow(int followerId, int followeeId) The user with ID followerId started unfollowing the user with ID followeeId.

Example1:
Input
["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
[[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
Output
[null, null, [5], null, null, [6, 5], null, [5]]

Explanation
Twitter twitter = new Twitter();
twitter.postTweet(1, 5); // User 1 posts a new tweet (id = 5).
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
twitter.follow(1, 2);    // User 1 follows user 2.
twitter.postTweet(2, 6); // User 2 posts a new tweet (id = 6).
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
twitter.unfollow(1, 2);  // User 1 unfollows user 2.
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5], since user 1 is no longer following user 2.

Constraints:
1 <= userId, followerId, followeeId <= 500
0 <= tweetId <= 10^4
All the tweets have unique IDs.
At most 3 * 10 ^4 calls will be made to postTweet, getNewsFeed, follow, and unfollow.
"""

"""
Note:
1. Hash Table + List
postTweet: O(1) time
getNewsFeed: O(recentMax * num) time | O() space - where recentMax = 10, num is the followees + 1
follow: O(1) time
unfollow: O(1) time
Total Space Complexity: O(tweets + users) - where tweets is the number of tweets and users is the number of users

2. OO design:
postTweet: O(1) time | O(1) space
getNewsFeed: O(num*log(num)) time | O(recentMax=10) space - where num is the followees + 1
follow: O(1) time | O(1) space
unfollow: O(1) time | O(1) space
Total Space Complexity: O(tweets + users) - where tweets is the number of tweets and users is the number of total users
"""

from typing import List
import unittest
class Twitter:
    class User:
        def __init__(self):
            self.followee = set() # to store the followees
            self.tweet = [] # use list to store tweets

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.time = 0 # current time
        self.recentMax = 10 # the upper limit of the number of most recent tweets
        self.tweetTime = dict() # to store the each tweet's post time <tweetId, time>
        self.user = dict() # to stores user's information <userId, Tweet.User>

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        # if user is new, add it into the Twitter's user Hash Table
        if userId not in self.user:
            self.user[userId] = Twitter.User()
        
        # append the new tweetId to the user's tweet list
        self.user[userId].tweet.append(tweetId)

        # increase the time
        self.time += 1

        # store the time to the tweetTime<tweetId, time> Hash Table
        self.tweetTime[tweetId] = self.time

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        if userId not in self.user:
            return []

        # get the user's most recent 10 tweets
        result = self.user[userId].tweet[-10:][::-1]
        
        for followeeId in self.user[userId].followee:
            if followeeId in self.user:
                tweetsOfTheFollowee = self.user[followeeId].tweet[-10:][::-1]
                i, j, combined = 0, 0, []
                while i < len(result) and j < len(tweetsOfTheFollowee):
                    if self.tweetTime[result[i]] > self.tweetTime[tweetsOfTheFollowee[j]]:
                        combined.append(result[i])
                        i += 1
                    else:
                        combined.append(tweetsOfTheFollowee[j])
                        j += 1
                combined.extend(result[i:])
                combined.extend(tweetsOfTheFollowee[j:])
                result = combined[:10]
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId != followeeId:
            if followerId not in self.user:
                self.user[followerId] = Twitter.User()
            self.user[followerId].followee.add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId != followeeId:
            if followerId in self.user and followeeId in self.user[followerId].followee:
                self.user[followerId].followee.remove(followeeId)


import heapq
class Tweet:
    def __init__(self, id, timeStamp):
        self.id = id
        self.time = timeStamp
        self.next = None # None or Tweet
    def __lt__(self, other):
        return self.time > other.time

class User:
    def __init__(self, id):
        self.id = id
        self.followed = set()
        self.follow(id) # first follow itself
        self.tweetHead = None # None or Tweet
    
    def follow(self, id) -> None:
        self.followed.add(id)
    
    def unfollow(self, id) -> None:
        self.followed.discard(id)

    def post(self, id: int, timeStamp: int) -> None:
        tweet = Tweet(id, timeStamp)
        tweet.next = self.tweetHead
        self.tweetHead = tweet

class Twitter2:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.userMap = dict() # <userId, User>
        self.timeStamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        if userId not in self.userMap:
            self.userMap[userId] = User(userId)
        self.timeStamp += 1
        self.userMap[userId].post(tweetId, self.timeStamp)
        

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        result = [] 
        if userId not in self.userMap:
            return result
        users = self.userMap[userId].followed
        heap = []
        for user in users:
            tweet = self.userMap[user].tweetHead
            if tweet:
                heapq.heappush(heap, tweet)
        n = 0
        while len(heap) > 0 and n < 10:
            tweet = heapq.heappop(heap)
            result.append(tweet.id)
            n += 1
            if tweet.next:
                heapq.heappush(heap, tweet.next)
        return result
        

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId not in self.userMap:
            self.userMap[followerId] = User(followerId)
        if followeeId not in self.userMap:
            self.userMap[followeeId] = User(followeeId)
        self.userMap[followerId].follow(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId not in self.userMap:
            self.userMap[followerId] = User(followerId)
        if followeeId not in self.userMap:
            self.userMap[followeeId] = User(followeeId)
        self.userMap[followerId].unfollow(followeeId)

# Unit Tests
classes = [Twitter, Twitter2]
class TestTwitter(unittest.TestCase):
    def testTwitter1(self):
        for myclass in classes:
            twitter = myclass()
            twitter.postTweet(1,5)
            self.assertEqual(twitter.getNewsFeed(1), [5])
            twitter.follow(1, 2)
            twitter.postTweet(2, 6)
            self.assertEqual(twitter.getNewsFeed(1), [6, 5])
            twitter.unfollow(1, 2)
            self.assertEqual(twitter.getNewsFeed(1), [5])

if __name__ == "__main__":
    unittest.main()
