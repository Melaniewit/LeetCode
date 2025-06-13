class Solution:
    def topKFrequent(self, nums, k):
        #neetcode bucket sort O(n)
        #recored times for each element
        count={}
        #freq bucket(number is the length of arr)
        freq=[[] for i in range(len(nums)+1)]
        for num in nums:
            #以num为key,count.get得之前次数，没有的话默认值为0
            count[num]=1+count.get(num,0)
        #put count's num and freq in buckets
        for num,c in count.items():
            #以频次为key
            freq[c].append(num)
        res=[]
        #从频次最高的bucket
        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                res.append(num)
                if len(res)==k:
                    return res

