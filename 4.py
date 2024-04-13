class Solution:
    def find(self, target: int, array: list[list[int]]) -> bool:
        if len(array) == 0:
            return False
        rows = len(array)
        cols = len(array[0])
        # 选取右上角tmp
        # tmp > target，删列
        # tmp < target，删行
        right, down = cols - 1, 0
        while right >= 0 and down < rows:
            tmp = array[down][right]
            if tmp == target:
                return True
            elif tmp < target:
                down += 1
            else:
                right -= 1
        return False


if __name__ == '__main__':
    tmp_array = [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]]
    solution = Solution()
    print(solution.find(7, tmp_array))


# 二维数组中的查找

# 选取右上角
