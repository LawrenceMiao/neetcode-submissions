class Solution:
    def check(self, s, t):
        s = list(s)
        for i in t:
            if i not in s:
                return False
            else:
                del s[s.index(i)]
        return True
    def minWindow(self, s: str, t: str) -> str:

        if not self.check(s, t):
            return ""
        left_valid = self.check(s[1:], t)
        right_valid = self.check(s[:-1], t)

        if not left_valid and not right_valid:
            return s
        if not left_valid and right_valid:
            return self.minWindow(s[:-1], t)

        if left_valid and not right_valid:
            return self.minWindow(s[1:], t)

        
        left = self.minWindow(s[1:], t)
        right = self.minWindow(s[:-1], t)
        if len(left)< len(right):
            return left
        else:
            return right