class Solution:

    def movingCount(self, threshold, rows, cols):
        if threshold < 0 or rows <= 0 or cols <= 0:
            return 0
        self.rows = rows
        self.cols = cols
        self.threshold = threshold
        self.count = 0
        # matrix用于记录走过的路径
        self.matrix = [[False for j in range(cols)] for i in range(rows)]
        self.movingCountCore(0, 0)
        return self.count

    def check(self, pos_x, pos_y):

        sum = 0
        while pos_x > 0:
            sum += pos_x % 10
            # python / 表浮点数除法，返回浮点数结果 1 / 10 返 0.1
            # python // 表整数除法 1 // 10 返 0
            pos_x //= 10
        while pos_y > 0:
            sum += pos_y % 10
            pos_y //= 10

        if sum > self.threshold:
            return False
        else:
            return True

    def movingCountCore(self, pos_x, pos_y):
        if self.matrix[pos_x][pos_y] is False and self.check(pos_x, pos_y):
            self.count += 1
            self.matrix[pos_x][pos_y] = True

            # 先判断条件后回溯，防止不满足条件时仍无限递归
            if 0 < pos_x:
                self.movingCountCore(pos_x - 1, pos_y)
            if pos_x < self.rows - 1:
                self.movingCountCore(pos_x + 1, pos_y)
            if 0 < pos_y:
                self.movingCountCore(pos_x, pos_y - 1)
            if pos_y < self.cols - 1:
                self.movingCountCore(pos_x, pos_y + 1)




if __name__ == '__main__':
    solution = Solution()
    print(solution.movingCount(5, 10, 10))


# 机器人的运动范围
# 回溯法



# 创建二维数组的方式

# 错误 只是指向三个列表的引用
# m_0 = [[0] * 5] * 3
# m_0[1][2] = 1
# print(m_0)
# [[0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0]]


# 正确
# m_1 = [[0] * 5 for i in range(3)]
# m_1[1][2] = 1
# print(m_1)
# [[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]

# 正确 推荐使用
# m_2 = [[0 for j in range(5)] for i in range(3)]
# m_2[1][2] = 1
# print(m_2)

# 创建空列表 m_3[1][2]会报越界
# m_3 = [[] for i in range(3)]
# m_3[0].append(1)
# print(m_3)