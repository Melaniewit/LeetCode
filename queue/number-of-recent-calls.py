class RecentCounter:
    #if put requests here, then will be parameter
    def __init__(self):
        #requests is used as a data structure to store the timestamps of recent requests (pings). 
        #This is why it should be treated as an instance attribute rather than a parameter:
        
        self.requests=[]
        
#Adds a new request at time t, where t represents some time in milliseconds, 
# returns the number of requests that has happened in the past 3000 milliseconds (including the new request).
    def ping(self, t: int) -> int:
        #add new timestamp
        self.requests.append(t)
        #check if the earliest timestamp out of range(3000)
        while self.requests[0]<t-3000:
            #请求的时间戳列表可以被看作是一个队列（先进先出的数据结构）。最旧的请求（即最先进入队列的元素）总是在列表的前端。因此，可以使用 pop(0) 来移除最旧的请求。这样做既符合问题的逻辑，又能有效维护列表的状态。
            #if yes, pop out the earliest timestamp
            self.requests.pop(0)
        #always return the number of timestamp in the range
        return len(self.requests)
        
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)