class Solution:
    def cutRope(self, number):

        if number <= 3:
            return number

        temp_list = [0, 1, 2, 3]

        for i in range(4, number + 1, 1):
            temp_list.append(i)
            for j in range(1, (i // 2) + 1, 1):
                if temp_list[i] < temp_list[j] * temp_list[i - j]:
                    temp_list[i] = temp_list[j] * temp_list[i - j]

        return temp_list[number]


if __name__ == '__main__':
    soultion = Solution()
    print(soultion.cutRope(8))


# 剪绳子
# 动态规划  自上向下分析，自下向上求解
# 把中间值存起来利用