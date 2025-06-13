class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # leftmost index
        l=0
        #right most index
        r=len(s)-1

        while l<r:
            #对称reverse所以要撞针two pointer
            s[l],s[r]=s[r],s[l]
            #撞针每步往中间靠
            l+=1
            r-=1
        