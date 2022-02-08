class Solution:
    def duplicate(self, numbers):
        nset = set()
        for i in numbers:
            if i in nset:
                return i
            else:
                nset.add(i)
        return -1


if __name__ == '__main__':
    my_list = [2, 3, 1, 0, 2, 5, 3]
    solution = Solution()
    res = solution.duplicate(my_list)
    print(res)
