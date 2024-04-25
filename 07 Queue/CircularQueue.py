# Cirular Queue with capacity


class Queue:

  def __init__(self, maxSize):
    self.items = maxSize * [None]
    self.maxSize = maxSize
    self.start = -1
    self.top = -1

  def __str__(self):
    return '->'.join([str(x) for x in self.items])

  def isFull(self):
    if (self.top + 1 == self.start) or (self.start == 0
                                        and self.top + 1 == self.maxSize):
      return True
    return False

  def isEmpty(self):
    if self.top == -1:
      return True
    return False

  def enqueu(self, item):
    if (self.isFull()):
      print("Can't insert an element")
    else:
      if self.top + 1 == self.maxSize:
        self.top = 0
      else:
        self.top += 1
        if self.start == -1:
          self.start = 0
        self.items[self.top] = item
      print(self.start, self.top)
      print("Inserted an element ", item)

  def dequeue(self):
    if self.isEmpty():
      return "Queue is empty"
    else:
      firstElement = self.items[self.start]
      start = self.start
      if self.start == self.top:
        self.start = -1
        self.top = -1
      elif self.start + 1 == self.maxSize:
        self.start = 0
      else:
        self.start += 1
      self.items[start] = None
      return firstElement


queue = Queue(6)
queue.enqueu(1)
queue.enqueu(2)
queue.enqueu(3)
queue.enqueu(4)
queue.enqueu(5)
queue.enqueu(6)
# queue.enqueu(7)
print(queue)
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.enqueu(3)
queue.enqueu(4)
queue.enqueu(8)
print(queue)
