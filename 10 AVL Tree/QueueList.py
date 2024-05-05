class Queue:

  def __init__(self):
    self.list = []

  def isEmpty(self):
    if self.list == []:
      return True
    return False

  def dequeue(self):
    if self.isEmpty():
      return "Queue is empty"
    else:
      return self.list.pop(0)

  def enqueue(self, value):
    self.list.append(value)

  def __str__(self):
    values = [x for x in self.list]
    return '<-'.join(values)

  def peek(self):
    return self.list[0]