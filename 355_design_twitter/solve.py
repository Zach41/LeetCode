#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Twitter(object):

    def __init__(self):
        self.user_tweets = {}
        self.user_followee = {}
        self.tweet_index = {}
        self.index = 0
        self.index_tweet = {}
    
    def postTweet(self, userId, tweetId):
        self._insertTweet(userId, tweetId)
        self.tweet_index[tweetId] = self.index
        self.index_tweet[self.index] = tweetId
        self.index += 1


    def _insertTweet(self, userId, tweetId):
        if self.user_tweets.has_key(userId):
            self.user_tweets[userId].insert(0, tweetId)
        else:
            self.user_tweets[userId] = [tweetId]

    
    def getNewsFeed(self, userId):
        res = []
        if self.user_tweets.has_key(userId):
            res = self.user_tweets[userId]

        for followee in self.user_followee.get(userId, []):
            tweets = self.user_tweets.get(followee, [])
            res = self._merge(res, tweets)

        return res[:10]
        

    def _merge(self, list1, list2):
        index1 = map(lambda x: self.tweet_index[x], list1)
        index2 = map(lambda x: self.tweet_index[x], list2)

        res = index1 + index2
        res = sorted(index1+index2)
        res = reversed(res)
        return map(lambda x: self.index_tweet[x], res)
    
    def follow(self, followerId, followeeId):
        if not self.user_followee.has_key(followerId):
            self.user_followee[followerId] = []
        if followerId == followeeId:
            return
        if followeeId in self.user_followee[followerId]:
            return
        self.user_followee[followerId].append(followeeId)

    def unfollow(self, followerId, followeeId):
        if self.user_followee.has_key(followerId):
            if followeeId in self.user_followee[followerId]:
                self.user_followee[followerId].remove(followeeId)


t = Twitter()

import pdb
pdb.set_trace()
# t.postTweet(1, 5)
# print t.getNewsFeed(1)

# t.follow(1, 2)

# t.postTweet(2, 6)

# print t.getNewsFeed(1)

# t.unfollow(1, 2)

# print t.getNewsFeed(1)
t.follow(1, 5)
t.postTweet(1, 1)
t.unfollow(1, 1)
print t.getNewsFeed(1)
        

    
