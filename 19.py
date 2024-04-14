# 递归解法，过长的字符串会超时
class Solution:
    def match(self, str, pattern):
        if str is None or pattern is None:
            return False
        if '' == str:
            if '' == pattern:
                return True
            if len(pattern) == 2 and pattern[1] == '*':
                return True
            else:
                return False
        return self.match_core(str, pattern, 0, 0)

    def match_core(self, str, pattern, index_1, index_2):

        if index_1 >= len(str) and index_2 >= len(pattern):
            return True
        if index_1 >= len(str) and index_2 >= len(pattern) - 2 and pattern[index_2 + 1] == '*':
            return True
        # 除此之外，其他的index_1 > len(str)的情况，都是False
        if index_1 >= len(str):
            return False

        # 讨论index_1 < len(str)的情况
        # 若pattern还有值
        if index_2 < len(pattern):
            if index_2 < len(pattern) - 1 and pattern[index_2 + 1] == '*':
                if str[index_1] == pattern[index_2] or pattern[index_2] == '.':
                    return self.match_core(str, pattern, index_1 + 1, index_2 + 2) or self.match_core(str, pattern, index_1 + 1, index_2) or self.match_core(str, pattern, index_1, index_2 + 2)
                else:
                    return self.match_core(str, pattern, index_1, index_2 + 2)

            if str[index_1] == pattern[index_2] or pattern[index_2] == '.':
                return self.match_core(str, pattern, index_1 + 1, index_2 + 1)

            # 若除了上述两种情况，都是False
            return False
        # 若pattern已无值，直接False
        else:
            return False


if __name__ == '__main__':
    solution = Solution()
    str = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    pattern = "aaaa*aaaaaaaaaaaaaaa*aaa*aaaaaaaaaaaaaaaaa*aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa*aaaaaaaaaaaaaaaaaa*aaaaaaaaaaaa*aaaaaaaaaaaa*aaaaaa*aaaaa*aaaa****aaaaaaaaaaaaaaaaaa*aaaaaaaaaaaaaaaa*aaaaaaaaaaaaa*aaaaaaaaaaaaa*aaaaaaa*aaaaa**a*aaaaaaaaaaaaa*aaaaa*aaaaaa*a*aaaaaaaaaaa*aaaaaaaaaaaaaaaaaaaaaaaaaaaaa*aaaaaaa*aaaaaaaaaaaa*a*aaaaaaaaaaaaaaaaaaaaaaaaaaaaa*aaaaaaaaaaa*aa*aaaaaaaaaaa*aa*aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa*aaaaaaaaaa*aaaaaaaaaaa**aaaaaaaaaaaaaaaaa*aaaaaaaaaaa*aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa*aaaa**aaaaaaaa*a*aaaaaa*a*aaaaaaaaaaa*aa*aa*aa**aaaaaaaaaaaaaaaaaaaaa*aaaaaa*aaa*aaaaaaaaaaaaaaaaaaaaaaaa*aaaaaaaa*aaaaaaaaaa*aaa*aaaaaaaaaaaaaaaaaaaaaaaaaaa*aaaaaa*aaaaaaaaaa*aaaaaaaaaaaaaaaaaaaa***aaaaaaaaaaaaaa*aaaaaaaaaaa*aaaaaa*a*aaaaaaa*aaaa*aaaaaaaaaaaaaaaa*aa*a*aaa*aaa*aaaaaaaaaaaa*aaaaaaa*aaa*aaaa*aaaaaaa*aaaaaa*aaaaaaaaaaaaaaaa*aaaaaa*aaaaaaaaaaaaaaaaa**a**aaa*aaaa*aaa**aaaaaaaaaaaaaaaaaaaaaaa*aaaaaaaaaaa*aaaaaaaaaaaaaaaaaaaa*aaaaaa*aaaaaaaaaaaaa"
    print(solution.match(str, pattern))


# 正则表达式匹配
# 不考虑出现 ** 的情况
# todo:动态规划解法？
