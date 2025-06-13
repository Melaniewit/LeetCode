class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans=[]
        #2 represent the times concatenation nums
        # if x times
        for n in range(2):
            for i in nums:
                ans.append(i)
        return ans

        
        