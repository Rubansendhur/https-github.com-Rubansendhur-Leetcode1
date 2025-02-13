class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        

    def push(self, x: int) -> None:
        self.stack1.append(x)        

    def pop(self) -> int:
        if len(self.stack1) == 0:
            return -1
        while (len(self.stack1) > 0):
            self.stack2.append(self.stack1.pop())

        ans = self.stack2.pop()

        while (len(self.stack2) > 0):
            self.stack1.append(self.stack2.pop())

        return ans       

    def peek(self) -> int:
        if len(self.stack1) == 0:
            return -1

        while (len(self.stack1) > 0):
            self.stack2.append(self.stack1.pop())

        ans = self.stack2[-1]

        while (len(self.stack2) > 0):
            self.stack1.append(self.stack2.pop())

        return ans       

    def empty(self) -> bool:
        if len(self.stack1) == 0:
            return True
        else:
            return False        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()