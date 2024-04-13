class Solution:
    def cutRope(self, n: int) -> int:
        if n <= 3:
            return n

        tmp_list = [0, 1, 2, 3]

        for i in range(4, n + 1, 1):
            tmp_list.append(i)
            for j in range(1, (i // 2) + 1, 1):
                if tmp_list[i] < tmp_list[j] * tmp_list[i - j]:
                    tmp_list[i] = tmp_list[j] * tmp_list[i - j]

        return tmp_list[n]


# 剪绳子
# 动态规划，自上向下分析，自下向上求解
# 把中间值存起来利用
