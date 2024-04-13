class Solution:
    def NumberOf1(self, n: int) -> int:
        if n < 0:
            n &= 0xffffffff
        count = 0
        while n > 0:
            count += 1
            n = n & (n - 1)
        return count


# 二进制中1的个数
# 也适用于：
#   判断一个整数是否为2的整数次方。把这个数减1之后，再和它自己做与运算，这个整数中唯一的1会变为0，因2的整数次方只能有最高位一个1
#   输入两个整数m和n，将m的二进制改为n需要几次。(将m和n异或^，然后查1的个数)
