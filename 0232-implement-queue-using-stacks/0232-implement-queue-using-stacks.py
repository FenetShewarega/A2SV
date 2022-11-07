class MyQueue:

    def __init__(self):
        self.element=[]

    def push(self, x: int) -> None:
        self.element.append(x)

    def pop(self) -> int:
           return self.element.pop(0)
        

    def peek(self) -> int:
           return self.element[0]
        

    def empty(self) -> bool:
           return len(self.element) == 0
            
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()