class Node:

  def __init__(self, value=None):
    self.value = value
    self.next = None


class LinkedList:

  def __init__(self):
    self.head = None
    self.tail = None

  def append(self, value):
    node = Node(value)
    if self.head is None:
      self.head = node
      self.tail = node
    else:
      node.next = self.head
      self.head = node

  def remove(self):
    if self.head is not None:
      node = self.head
      self.head = self.head.next
      return node.value
    else:
      return "Stack is empty"

  def top(self):
    return self.head.value if self.head is not None else "Stack is empty"


class Stack:

  def __str__(self):
    return str(self.peek())

  def __init__(self):
    self.stack = LinkedList()

  def push(self, item):
    self.stack.append(item)

  def pop(self):
    return self.stack.remove()

  def peek(self):
    return self.stack.top()


stack = Stack()
stack.push(10)
stack.push(30)
# print(stack)
stack.pop()
print(stack.pop())
print(stack)
