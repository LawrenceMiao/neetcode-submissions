class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # end is top
        for i in s:
            if i in ['(','[','{']:
                stack.append(i)
            else:
                if stack == []:
                    return False
                if not ((stack[-1] == '(' and i == ')') or (stack[-1] == '[' and i == ']') or (stack[-1] == '{' and i == '}')):
                    return False
                stack.pop()
        return stack == []
        