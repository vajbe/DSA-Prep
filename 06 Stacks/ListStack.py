class Stack:

  def __init__(self):
    self.stack = []
    self.top = -1

  def push(self, item):
    self.stack.append(item)
    self.top += 1

  def pop(self):
    self.top -= 1
    if self.isEmpty():
      return "List is empty"
    return self.stack.pop()

  def peek(self):
    return self.stack[len(self.stack) - 1]

  def isEmpty(self):
    if self.stack == []:
      return True
    return False


stack = Stack()
stack.push(10)
stack.push(20)
# print(stack.peek())
print(stack.pop())
print(stack.pop())
print(stack.pop())
