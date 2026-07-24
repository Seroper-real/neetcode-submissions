class Twitter:

    def __init__(self):
        self.posts = []
        self.follows = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.follows[userId].add(userId)
        heapq.heappush(self.posts, (-self.time, tweetId, userId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        #print(self.posts, self.follows)
        feed = []
        seens = []
        while len(feed) < 10 and self.posts:
            time, tId, uId = heapq.heappop(self.posts)
            seens.append((time, tId, uId))
            if uId in self.follows[userId]: feed.append(tId)
        
        for seen in seens: heapq.heappush(self.posts, seen)
        
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followeeId].add(followeeId)
        self.follows[followerId].add(followerId)
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
        self.follows[followeeId].add(followeeId)
        self.follows[followerId].add(followerId)

