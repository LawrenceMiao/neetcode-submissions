def matches(i, j):
    if i == '[' and j == ']':
        return True
    if i == '(' and j == ')':
        return True
    if i == '{' and j == '}':
        return True
    return False


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in "[({":
                stack.append(i)
            else:
                if len(stack) > 0 and matches( stack[-1], i):
                    stack.pop()
                else:
                    return False


        return stack == []