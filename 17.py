class Solution:
    def printNumbers(self, n: int) -> list[int]:
        number = 10 ** n - 1
        ls = []
        i = 0
        while i < number:
            ls.append(i + 1)
            i += 1
        return ls


# 打印1到最大的n位数
# todo: 尚未考虑大数需用字符串的问题
