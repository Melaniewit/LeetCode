class Solution:
    def mySqrt(self, x: int) -> int:
        #find element from sorted list--binary search--effiecent
        #close interval
        #define inital
        l,r=0,x
        while l<=r:
            #avoid overflow
            m=l+(r-l)//2
            if m**2>x:
                r=m-1
            elif m**2<x:
                l=m+1
            else:
                return m
        #when 
        return r
