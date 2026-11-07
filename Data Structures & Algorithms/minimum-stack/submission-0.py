class MinStack:

    def __init__(self):
        self.array = []
        """ 
        the ith element is the min if we 
        popped the array to that size
        """
        self.min_stack = []

    def push(self, val: int) -> None:
        if len(self.array) == 0:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(self.min_stack[-1], val))
        self.array.append(val)

    def pop(self) -> None:
        self.array.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.array[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
