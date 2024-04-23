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


queue = Queue()
queue.enqueue("15")
queue.enqueue("90")
queue.enqueue("11")
queue.enqueue("5")
print(queue)
queue.dequeue()
queue.dequeue()
print(queue)
