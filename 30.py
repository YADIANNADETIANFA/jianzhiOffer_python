class Solution:
    def __init__(self):
        self.m_data = list()
        self.m_min = list()

    def push(self, node):
        self.m_data.append(node)
        # len(self.m_min) == 0 记得考虑
        if len(self.m_min) == 0 or node < self.m_min[-1]:
            self.m_min.append(node)
        else:
            self.m_min.append(self.m_min[-1])

    def pop(self):
        self.m_min.pop()
        return self.m_data.pop()

    def top(self):
        return self.m_data[-1]

    def min(self):
        return self.m_min[-1]

# 包含min函数的栈
# m_data存数据，m_min存min值