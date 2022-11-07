class MinStack:
    

    def __init__(self):       
        # self.__elements.append(data)
        self._elements = []
    def push(self, val: int) -> None:
        self._elements.append(val)
    def pop(self) -> None:
        if len(self._elements)==0:
            return None
        return self._elements.pop()
    def top(self) -> int:
        return self._elements[-1] 
    def getMin(self) -> int:
        return min(self._elements)
            



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()