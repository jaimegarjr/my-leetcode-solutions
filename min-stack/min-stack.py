class Node:
    
    def __init__(self, val=0, minVal=0):
        self.val = val
        self.minVal = minVal

class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(Node(val, val))
        else:
            topNode = self.topNode()
            self.stack.append(Node(val, min(topNode.minVal, val)))

    def pop(self) -> None:
        top = self.stack.pop()
        return top.val
    
    def topNode(self) -> Node:
        return self.stack[-1]

    def top(self) -> int:
        return self.stack[-1].val

    def getMin(self) -> int:
        return self.stack[-1].minVal


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()