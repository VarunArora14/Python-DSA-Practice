# https://www.geeksforgeeks.org/must-coding-questions-company-wise/?ref=grb#amazon-interview-coding-questions

class MyStack:
    def __init__(self) -> None:
        self.stack = []
        self.min_stack = []
    
    def push(self, val:int):
        self.stack.append(val)
        if len(self.min_stack)==0 or val<=self.min_stack[-1]:
            self.min_stack.append(val)
    
    def pop(self):
        if self.stack.pop() == self.min_stack[-1]:
            self.min_stack.pop()
    
    def top(self):
        return self.stack[-1]

    def getMinVal(self):
        return self.min_stack[-1]

s = MyStack()
s.push(5)
s.push(4)
s.push(7)
print(s.top())
print(s.getMinVal())