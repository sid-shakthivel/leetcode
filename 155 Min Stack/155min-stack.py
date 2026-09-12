class MinStack:

    def __init__(self):
        self.stack = []
        self.current_min = float('inf')

    def push(self, value: int) -> None:
        self.current_min = min(self.current_min, value)
        self.stack.append((value, self.current_min))
        
    def pop(self) -> None:
        if len(self.stack) > 0:
            self.stack.pop()

            if len(self.stack) == 0:
                self.current_min = float('inf')
            else:
                self.current_min = self.stack[-1][1]

    def top(self) -> int:
        if len(self.stack) == 0:
            return -1

        return self.stack[-1][0]

    def getMin(self) -> int:
        if len(self.stack) == 0:
            return -1
        
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()