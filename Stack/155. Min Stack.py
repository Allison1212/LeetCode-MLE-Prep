class MinStack:

    def __init__(self):
        self.stack = list()
        
        

    def push(self, value: int) -> None:
        if not self.stack:
            self.stack.append((value,value))
        else:
            cur_min = min(self.stack[-1][-1],value)
            self.stack.append((value,cur_min))
        

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:

        return self.stack[-1][-1]


# 用辅助栈记录每一步的历史最小值