class MinStack:

    def __init__(self):
        self.normal_stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.normal_stack.append(val)
        if self.min_stack:
            self.min_stack.append(min(val, self.min_stack[-1]))
        else:
            self.min_stack.append(val)
        

    def pop(self) -> None:
        if self.normal_stack:
            self.normal_stack.pop()
            self.min_stack.pop()
        else:
            pass

    def top(self) -> int:
        if self.normal_stack:
            return self.normal_stack[-1]
        else:
            pass

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]
        else:
            pass

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

"""
min stack 
[-2 -2]
normal stack 
[-2 0]
output
[-3, 0, -2]
"""
