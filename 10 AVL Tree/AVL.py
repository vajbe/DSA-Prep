import QueueList


class AVLNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None
        self.height = 1


def preOrder(rootNode):
    if rootNode is None:
        return
    print(rootNode.data)
    preOrder(rootNode.left)
    preOrder(rootNode.right)


def inOrder(rootNode):
    if rootNode is None:
        return
    inOrder(rootNode.left)
    print(rootNode.data)
    inOrder(rootNode.right)


def postOrder(rootNode):
    if rootNode is None:
        return
    postOrder(rootNode.left)
    postOrder(rootNode.right)
    print(rootNode.data)


def levelOrder(rootNode):
    if not rootNode:
        return
    customQueue = QueueList.Queue()
    customQueue.enqueue(rootNode)
    while not customQueue.isEmpty():
        root = customQueue.dequeue()
        print("-", root.data)
        if root.left is not None:
            customQueue.enqueue(root.left)
        if root.right is not None:
            customQueue.enqueue(root.right)


def search(rootNode: AVLNode, nodeValue):
    if rootNode is None:
        print("Either tree is empty or value not found")
        return

    if rootNode.data == nodeValue:
        print("Value found")
    elif nodeValue < rootNode.data:
        search(rootNode.left, nodeValue)
    else:
        search(rootNode.right, nodeValue)


root = AVLNode(10)
