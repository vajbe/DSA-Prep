class SNode:

  def __init__(self, value=None):
    self.value = value
    self.next = None


class SLinkedList:

  def __init__(self):
    self.head = None
    self.tail = None

  def __iter__(self):
    node = self.head
    while node:
      yield node
      node = node.next

  def insert(self, value, location):
    node = SNode(value)

    if self.head is None:
      self.head = node
      self.tail = node
    else:
      if location == 0:
        node.next = self.head
        self.head = node
      elif location == -1:
        self.tail.next = node
        self.tail = node
      else:
        index = 0
        tempNode = self.head
        while index < location - 1:
          tempNode = tempNode.next
          index += 1
        nextNode = tempNode.next
        node.next = nextNode
        tempNode.next = node
        if tempNode == self.tail:
          self.tail = tempNode

  def search(self, searchValue):
    if self.head is None:
      print("List is empty")
    else:
      tempNode = self.head
      while (tempNode):
        if tempNode.value == searchValue:
          print("Value is in the list")
          return
        tempNode = tempNode.next
    print('Element is not found')

  def delete(self, location):
    if self.head is None:
      print("List is empty")
    else:
      if location == 0:
        if self.head == self.tail:
          self.head = None
          self.tail = None
        else:
          self.head = self.head.next
      elif location == -1:
        if self.head == self.tail:
          self.head = None
          self.tail = None
        else:
          tempNode = self.head
          while tempNode is not None:
            if tempNode.next == self.tail:
              break
            tempNode = tempNode.next
          tempNode.next = None
          self.tail = tempNode
      else:
        tempNode = self.head
        index = 0
        while index < location - 1:
          tempNode = tempNode.next
          index += 1
        newNode = tempNode.next
        tempNode.next = newNode.next


sList = SLinkedList()
sList.insert(1, -1)
sList.insert(2, -1)
sList.insert(3, -1)
sList.insert(4, -1)

sList.insert(45, 0)
sList.insert(6, 2)
sList.search(6)
sList.search(16)

print([node.value for node in sList])

sList.delete(0)
sList.delete(-1)
sList.delete(2)
print([node.value for node in sList])
