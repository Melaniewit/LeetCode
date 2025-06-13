from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 本质：我们每一步都在判断 —— 前面的和加进来值不值？
        # 因为必须连续，所以只能选择：加上前面的，或者放弃前面的，从当前数重新开始！

        # nums[i] 是当前的数
        # dp[i] 表示：以 nums[i] 结尾的连续子数组的最大和
        dp = nums[:]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])  # 继续加 vs 重新开始
        return max(dp)
