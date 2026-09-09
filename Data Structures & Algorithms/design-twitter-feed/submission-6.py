class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.following = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        
        self.tweets[userId].append((tweetId, self.time))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = self.tweets[userId][:]

        for followeeId in self.following[userId]:
            feed.extend(self.tweets[followeeId])
        
        feed.sort(key = lambda x: -x[1])
        return [tweetId for tweetId, _ in feed[:10]]


    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.following[followerId]:
             self.following[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)