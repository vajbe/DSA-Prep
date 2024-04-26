import LinkedList

class Queue:
    def __init__(self) -> None:
        self.list = LinkedList.LinkedList()
        
    def __str__(self):
        node = self.list.head
        s = ''
        while(node):
            s +=  " <- " + str(node.value)
            node = node.next
        return str(s)
    
    def enqueue(self, item):
        newNode = LinkedList.Node(item)
        if self.list.head == None:
            self.list.head = newNode
            self.list.tail = newNode
        else:
            self.list.tail.next = newNode
            self.list.tail = newNode
        
    def dequeue(self):
        if self.isEmpty():
            return "List is empty"    
        else:
            node = self.list.head
            if self.list.head == self.list.tail:
                self.list.head = None
                self.list.tail = None
            else:
                self.list.head = self.list.head.next
            return str(node.value)
    
    def isEmpty(self):
        if self.list.head is None:
            return True
        else:
            return False
    
q = Queue()
q.enqueue(12)
q.enqueue(23)
q.enqueue(33)
q.enqueue(4)
print(q)
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
print(q.dequeue())
print(q)
