class Solution:
    def Fibonacci(self, n: int) -> int:
        if n < 2:
            return n;
        else:
            last_two = 0
            last_one = 1
            for i in range(2, n+1, 1):
                last_two, last_one = last_one, last_two  + last_one
            return last_one


# 斐波那契数列
# 青蛙跳台阶
# 矩形覆盖
# 迭代求解，自下而上
