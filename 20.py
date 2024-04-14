class Solution:
    def isNumeric(self, str: str) -> bool:
        try:
            float(str)
        except:
            return False
        return True


# 表示数值的字符串
# 表示数值的字符串都可转化为浮点数，因此可使用异常捕获的方法进行判断
# 麻烦点就是用正则表达式
