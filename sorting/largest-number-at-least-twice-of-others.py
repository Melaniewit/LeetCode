class Solution:
    def dominantIndex(self, nums: List[int]) -> int:

        # if the maximum >= 2* second_max,it means that maixmum is at least twice as much as every other number in the array. 
    # initialize the maximum
        max_value=-1
        #initialize the maximum index
        index=0
        #initlize the second maximum
        second_max_value=-1
    
        #iterate the index and element in nums
        #i--current element index
        #num--current element
        for i,num in enumerate(nums):
            if num>max_value:
                #update the second maximum
                second_max_value=max_value
                #update the maximum
                max_value=num
                #record the index of maximum
                index=i

            elif num>second_max_value:
                second_max_value=num

        if max_value>=2*second_max_value:
            return index
        else:
            return -1
