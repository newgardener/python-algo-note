class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int):
        if not self.stack:
            # (value, minValue up to this point)
            self.stack.append((val, val))
        else:
            self.stack.append((val, min(self.stack[-1][1], val)))

    def pop(self):
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
