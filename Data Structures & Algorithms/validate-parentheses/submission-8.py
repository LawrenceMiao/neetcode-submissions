class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in ['(', '{', '[']:
                stack.append(i)
            else:
                if stack and i == ')' and stack[-1] == '(':
                    stack.pop()
                elif stack and i == '}' and stack[-1] == '{':
                    stack.pop()
                elif stack and i == ']' and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
        return stack == []