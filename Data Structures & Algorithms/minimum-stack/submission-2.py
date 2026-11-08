class MinStack:

    def __init__(self):
        self.stack = []
        self.min_array = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_array == []:
            self.min_array.append(val)
        else:
            self.min_array.append(min(val, self.min_array[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.min_array.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.min_array[-1]
