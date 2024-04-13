class Solution:
    def hasPath(self, matrix: list[list[str]], word: str) -> bool:
        if matrix is None or str is None:
            return False
        if word == '':
            return True

        row = len(matrix)
        col = len(matrix[0])

        if row < 1 or col < 1:
            return False

        for i in range(row):
            for j in range(col):
                if self.hasPathCore(matrix, row, col, word, i, j, 0):
                    return True
        return False

    def hasPathCore(self, matrix: list[list[str]], row: int, col: int, word: str, i: int, j: int, index: int) -> bool:
        if i > row or j > col or i < 0 or j < 0:
            return False
        if matrix[i][j] != word[index]:
            return False
        if index == len(word) - 1:
            return True

        # 将走过的位置变为不可能出现的字符'0'，False的时候记得换回来
        temp = matrix[i][j]
        matrix[i][j] = '0'
        res = self.hasPathCore(matrix, row, col, word, i - 1, j, index + 1) \
            or self.hasPathCore(matrix, row, col, word, i + 1, j, index + 1) \
            or self.hasPathCore(matrix, row, col, word, i, j - 1, index + 1) \
            or self.hasPathCore(matrix, row, col, word, i, j + 1, index + 1)
        if res:
            return True
        else:
            return False


# 矩阵中的路径
