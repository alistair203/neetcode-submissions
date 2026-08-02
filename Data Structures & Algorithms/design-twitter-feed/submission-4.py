class Twitter:

    def __init__(self):
        self.following = {}
        self.tweet_times = {} # userId : set of times they tweeted (idx in tweetIds)
        self.tweetIds = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweet_times:
            self.tweet_times[userId] = set()
        self.tweet_times[userId].add(len(self.tweetIds))
        self.tweetIds.append(tweetId)

    def getNewsFeed(self, userId: int) -> List[int]:
        tweet_times = self.tweet_times.get(userId, set())
        for followee in list(self.following.get(userId, [])):
            tweet_times = tweet_times | self.tweet_times.get(followee, set())
        recent_times = []
        heapq.heapify(recent_times)
        for t in list(tweet_times):
            heapq.heappush(recent_times, t)
            if len(recent_times) > 10:
                heapq.heappop(recent_times)
        return [self.tweetIds[t] for t in sorted(recent_times, reverse=True)]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            self.following[followerId].add(followeeId)
        else:
            self.following[followerId] = set([followeeId])
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
            self.following[followerId].discard(followeeId)
        
