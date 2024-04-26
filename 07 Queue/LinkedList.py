class Node:

  def __init__(self, value=None):
    self.value = value
    self.next = None

class LinkedList:

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
