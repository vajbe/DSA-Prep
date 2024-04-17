class Node:

  def __init__(self, value=None):
    self.value = value
    self.next = None


class CircularList:

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
    node.next = node

  def insert(self, value, location):
    node = Node(value)
    if location == 0:
      node.next = self.head
      self.head = node
      self.tail.next = node
    elif location == -1:
      node.next = self.tail.next
      self.tail.next = node
      self.tail = node
    else:
      tempNode = self.head
      index = 0
      while index < location - 1:
        tempNode = tempNode.next
        index += 1
      nextNode = tempNode.next
      node.next = nextNode
      tempNode.next = node

  def search(self, searchValue) -> bool:
    node = self.head
    while (node):
      if (node.value == searchValue):
        print("Element found")
      node = node.next
      if node == self.tail.next:
        break
    return False

  def delete(self, location):
    print("Deleting at ", location)
    if self.head is None:
      print("List is empty")
    elif self.tail == self.head:
      self.head = None
      self.tail = None
    else:
      if location == 0:
        nextNode = self.head.next
        self.tail.next = nextNode
        self.head.next = None
        self.head = nextNode
      elif location == -1:
        node = self.head
        while node.next != self.tail:
          node = node.next
        node.next = self.head
        self.tail = node
      else:
        node = self.head
        index = 0
        while index < location - 1:
          node = node.next
          index += 1
        nextNode = node.next
        node.next = nextNode.next
        nextNode.next = None


cll = CircularList()
cll.create(1)
cll.insert(2, -1)
cll.insert(3, -1)
cll.insert(4, 0)
cll.insert(5, 0)
cll.insert(0, -1)
cll.insert(8, -1)
print([node.value for node in cll])
cll.search(8)
cll.delete(3)
cll.delete(-1)
cll.delete(0)

print([node.value for node in cll])
