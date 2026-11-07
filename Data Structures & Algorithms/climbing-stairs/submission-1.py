class Solution:
    def __init__(self):
        self.table = []
    def climbStairs(self, n: int) -> int:
        if self.table == []:
            self.table = [-1] * n
        if n == 1:
            return 1
        if n == 2:
            return 2
        if self.table[n - 2] == -1:
            self.table[n - 2] = self.climbStairs(n - 2)
        if self.table[n - 1] == -1:
            self.table[n - 1] = self.climbStairs(n - 1)
        return self.table[n - 2] + self.table[n - 1]