class Node:

  def __init__(self, value=None):
    self.prev = value
    self.next = None
    self.value = value


class DoublyList:

  def __init__(self):
    self.head = None
    self.tail = None

  def __iter__(self):
    node = self.head
    while node:
      yield node
      if node == self.tail:
        break
      node = node.next

  def create(self, value):
    node = Node(value)
    self.head = node
    self.tail = node
    print("List created")

  def insert(self, value, location):
    if self.head is None:
      self.create(value)
    else:
      node = Node(value)
      if location == 0:
        node.next = self.head
        self.head.prev = node
        self.head = node
      elif location == -1:
        node.prev = self.tail
        self.tail.next = node
        self.tail = node
      else:
        index = 0
        currNode = self.head
        while (index < location - 1):
          index += 1
          currNode = currNode.next
        node.next = currNode.next
        node.prev = currNode
        currNode.next.prev = node
        currNode.next = node

  def search(self, value):
    node = self.head
    while (node):
      if node.value == value:
        print("found")
        return
      node = node.next
    print("Not found")


list = DoublyList()
list.create(10)
list.insert(1, -1)
list.insert(2, 0)
list.insert(3, 2)
list.search(3)
print([node.value for node in list])
