class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def condition(k):
            total_hours=0
            for pile in piles:
                total_hours+=(pile+k-1)//k
            return total_hours<=h
        left=1
        right=max(piles)
        while left<right:
            mid=left+(right-left)//2
            if condition(mid):
                right=mid
            else:
                left=mid+1
        return left

            
        