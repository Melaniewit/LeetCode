class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #因为题目保证：有一个数字出现的次数超过一半。
        #多数一定会占据中间
        nums.sort()
        return nums[len(nums)//2]
        