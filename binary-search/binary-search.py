from math import floor
class Solution:
    def search(self, nums: List[int], target: int) -> int:
#binary search
#here choose the right open interval for left and right
        #define index
        #right interval
        left,right=0,len(nums)
        #find every element in nums---until left and right no element--condition loop--while
        while(left<right):
            mid=floor((left+right)/2)
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                #update right interval
                # right open interval here
                right=mid
            elif nums[mid]<target:
                #update left interval 
                #right open interval
                left=mid+1
        return -1

            


        