# https://leetcode.com/problems/min-stack/
class MinStack:

  def __init__(self):
    self.stack = []
    self.minElements = []

  def push(self, val: int) -> None:
    self.stack.append(val)
    if (self.minElements):
      val = min(self.minElements[-1], val)
    print(val)
    self.minElements.append(val)

  def pop(self) -> None:
    val = self.stack.pop()
    self.minElements.pop()

  def top(self) -> int:
    return self.stack[-1]

  def getMin(self) -> int:
    return self.minElements[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
