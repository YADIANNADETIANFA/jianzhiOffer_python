from typing import List


class Solution:
    def printMatrix(self, matrix: List[List[int]]) -> List[int]:

        if matrix is None:
            return None

        res = list()

        # 上下左右可取到的边界
        left = 0
        right = len(matrix[0]) - 1
        up = 0
        down = len(matrix) - 1

        while left <= right and up <= down:
            # 每次遍历一边都需要判断一下条件，否则输入[1,2,3,4,5]会得到结果[1,2,3,4,5,4,3,2,1]
            if left <= right and up <= down:
                for i in range(left, right + 1, 1):
                    res.append(matrix[up][i])
                # for外进行边界更新，而不是for内部
                up += 1

            if left <= right and up <= down:
                for i in range(up, down + 1, 1):
                    res.append(matrix[i][right])
                right -= 1

            if left <= right and up <= down:
                for i in range(right, left - 1, -1):
                    res.append(matrix[down][i])
                down -= 1

            if left <= right and up <= down:
                for i in range(down, up - 1, -1):
                    res.append(matrix[i][left])
                left += 1

        return res


if __name__ == '__main__':
    solution = Solution()
    res = solution.printMatrix([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
    print(res)


# 倒序遍历：for i in range(10, -1, -1)       结果为10~0

# 顺时针打印矩阵
