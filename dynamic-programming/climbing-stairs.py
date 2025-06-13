class Solution:
    def climbStairs(self, n: int) -> int:
        # base case：当 n = 1 时，只有 1 种走法
        if n == 1:
            return 1
        
        # 初始化：到第 0 阶和第 1 阶的走法都是 1 种
        prev_prev = 1  # ways to reach step 0
        prev = 1       # ways to reach step 1

        # 从第 2 阶开始计算，一直到第 n 阶
        for i in range(2, n + 1):
            # 当前阶的走法数 = 前一阶 + 前两阶的走法数
            current = prev + prev_prev
            # 更新状态，准备计算下一阶
            prev_prev = prev
            prev = current

        return current
