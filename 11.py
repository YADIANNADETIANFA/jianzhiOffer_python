class Solution:
    # def minNumberInRotateArray(self, rotateArray) -> int:
    #     if len(rotateArray) == 0:
    #         return 0
    #     else:
    #         return min(rotateArray)

    def minNumberInRotateArray(self, rotateArray) -> int:
        if len(rotateArray) == 0:
            return 0
        # 首先定义最左和最右两个下标变量
        left = 0
        right = len(rotateArray) - 1
        # 开始二分
        while left < right:
            # 使用位运算
            middle = left + ((right - left) >> 1)
            if rotateArray[middle] > rotateArray[right]:
                # 此时最小值在右区间，可忽略左区间
                # 由于中间点大于最右值，所以中间点一定不是最小值
                left = middle + 1
            elif rotateArray[middle] < rotateArray[right]:
                # 此时忽略右区间
                right = middle
            else:
                # 当中间值等于最右值，即数组中存在重复数字，直接右边界下标减一来更新右边界
                right = right - 1
        return rotateArray[left]


# 旋转数组的最小数字
# 二分法