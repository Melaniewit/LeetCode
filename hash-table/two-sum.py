class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #brute way

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                #core
                if nums[i]+nums[j]==target:
                    return [i,j]



        
        