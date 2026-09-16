class User:
    def __init__(self, userId):
        self.userId = userId
        self.following = set()
        self.followers = set()
        self.tweets = []
        
    
class Twitter:

    def __init__(self):
        self.users = {}
        self.time = 0

    def createUser(self, userId):
        if userId in self.users:
            return
        #initiate
        user = User(userId)
        #create
        self.users[userId] = user
    
    
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.createUser(userId)
        userTweets = self.users[userId].tweets
        userTweets.append((self.time, tweetId))
        self.time += 1


    def getNewsFeed(self, userId: int) -> List[int]:
        # get followers -> extract their tweets, use a max heap to sort top-10 elements.
        feed = []


        userTweets = list(self.users[userId].following)
        userTweets.append(userId)

        for tweeter in userTweets:
            allTweets = self.users[tweeter].tweets
            for t, id in allTweets:
                if len(feed) < 10:
                    heapq.heappush(feed, (t, id))
                else:
                    if feed[0][0] < t:
                        heapq.heappop(feed)
                        heapq.heappush(feed, (t, id))
        
        feed.sort(key= lambda x : x[0], reverse=True)
        feed = [id for t, id in feed]
            
        
        
        return feed

                        

        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.createUser(followerId)
        self.createUser(followeeId)

        follower = self.users[followerId]
        followee = self.users[followeeId]

        follower.following.add(followeeId)
        followee.followers.add(followerId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.createUser(followerId)
        self.createUser(followeeId)

        follower = self.users[followerId]
        followee = self.users[followeeId]

        follower.following.discard(followeeId)
        followee.followers.discard(followerId)

        
