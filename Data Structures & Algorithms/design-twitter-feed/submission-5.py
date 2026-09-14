class Twitter:

    def __init__(self):
        self.relationship = defaultdict(set)
        self.tweet = defaultdict(deque)
        self.clock = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet[userId].append( (tweetId, self.clock) )
        self.clock += 1
        if len(self.tweet[userId]) > 10:
            self.tweet[userId].popleft()

    def _getNewsFeed(self, userId, vis):
        if userId in vis:
            return []
        
        vis.add(userId)
        tweets = list(self.tweet[userId])[:]
        for followeeId in self.relationship[userId]:
            tweets.extend(self._getNewsFeed(followeeId, vis))
        
        return tweets

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = self._getNewsFeed(userId, set())
        tweets.sort(key = lambda x : x[1], reverse=True)
        return [tweet_id for tweet_id, clock in tweets[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.relationship[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.relationship[followerId].discard(followeeId)
        