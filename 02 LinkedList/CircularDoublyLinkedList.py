class Node:

  def __init__(self, value=None):
    self.prev = value
    self.next = None
    self.value = value

  def __str__(self):
    print(self.value)
    return str(self.value)


class DoublyList:

  def __str__(self):
    node = self.head
    s = ""
    while (node):
      s += (str(node.value) + " -> ")
      if self.tail == node:
        break
      node = node.next
    return s

  def __init__(self):
    self.head = None
    self.tail = None

  def create(self, nodeValue):
    node = Node(nodeValue)
    self.head = node
    self.tail = node
    node.next = node
    node.prev = node

  def insert(self, nodeValue, location):
    if self.head is None:
      return "List is empty"
    else:
      node = Node(nodeValue)
      if location == 0:
        node.next = self.head
        node.prev = self.tail
        self.head.prev = node
        self.head = node
        self.tail.next = node
      elif location == -1:
        node.prev = self.tail
        node.next = self.head
        self.head.prev = node
        self.tail.next = node
        self.tail = node
      else:
        tempNode = self.head
        index = 0
        while (index < location - 1):
          index += 1
          tempNode = tempNode.next
        nextNode = tempNode.next
        node.next = nextNode
        node.prev = tempNode
        tempNode.next = node
        nextNode.prev = node

  def delete(self, location):
    if self.head == self.tail:
      self.head = None
      self.tail = None
    else:
      if location == 0:
        self.head = self.head.next
        self.tail.next = self.head
        self.head.prev = self.tail
      elif location == -1:
        self.tail = self.tail.prev
        self.tail.next = self.head
        self.head.prev = self.tail
      else:
        index = 0
        node = self.head
        while (index < location - 1):
          index += 1
          node = node.next
        nextNode = node.next
        node.next = nextNode.next
        nextNode.next.prev = node


list = DoublyList()
list.create(10)
list.insert(11, -1)
list.insert(6, 0)
list.insert(9, -1)
print(list)
list.delete(2)
print(list)
