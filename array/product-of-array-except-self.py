class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
    
        # 初始化 prefix 和 suffix 数组
        prefix = [1] * n
        suffix = [1] * n
        
        # 计算 prefix 数组
        prefix[0] = nums[0]
        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i]
        
        # 计算 suffix 数组
        suffix[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            suffix[i] = nums[i] * suffix[i+1]
        
        # 计算结果数组
        res = [0] * n
        for i in range(n):
            if i == 0:
                res[i] = suffix[i+1]  # 左边没有元素，直接取 suffix[i+1]
            elif i == n-1:
                res[i] = prefix[i-1]  # 右边没有元素，直接取 prefix[i-1]
            else:
                res[i] = prefix[i-1] * suffix[i+1]  # 左右两边的乘积
        
        return res