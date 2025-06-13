class Solution:
    def climbStairs(self, n: int) -> int:
        #Dynamic Programming (DP).
        #F(1)=1
        #F(3)=F(2)+F(1)=2+1=3
        if n==1:
            return 1
        if n==2:
            return 2
        
        return self.climbStairs(n-1)+self.climbStairs(n-2)
