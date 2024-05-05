import QueueList


class AVLNode:
    def __init__(self, data: int) -> None:
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


def getHeight(rootNode: AVLNode):
    if not rootNode:
        return 0
    return rootNode.height


def rotateRight(rootNode: AVLNode):
    newRoot: AVLNode = rootNode.left
    rootNode.left = rootNode.left.right
    newRoot.right = rootNode
    rootNode.height = 1 + max(getHeight(rootNode.left), getHeight(rootNode.right))
    newRoot.height = 1 + max(getHeight(newRoot.left), getHeight(newRoot.right))
    return newRoot


def rotateLeft(rootNode: AVLNode):
    newRoot: AVLNode = rootNode.right
    rootNode.right = rootNode.right.left
    newRoot.left = rootNode
    rootNode.height = 1 + max(getHeight(rootNode.left), getHeight(rootNode.right))
    newRoot.height = 1 + max(getHeight(newRoot.left), getHeight(newRoot.right))
    return newRoot


def getBalance(rootNode: AVLNode):
    if rootNode is None:
        return 0
    return getHeight(rootNode.left) - getHeight(rootNode.right)


def insertNode(rootNode: AVLNode, nodeValue: int):
    if rootNode is None:
        return AVLNode(nodeValue)

    if nodeValue < rootNode.data:
        rootNode.left = insertNode(root.left, nodeValue)
    else:
        rootNode.right = insertNode(rootNode.right, nodeValue)

    rootNode.height = 1 + max(getHeight(rootNode.left), getHeight(rootNode.right))

    balance = getBalance(rootNode)

    if balance > 1 and nodeValue < rootNode.left.data:
        return rotateRight(rootNode)
    if balance > 1 and nodeValue > rootNode.left.data:
        rootNode.left = rotateLeft(rootNode.left)
        return rotateRight(rootNode)
    if balance < -1 and nodeValue > rootNode.right.data:
        return rotateLeft(rootNode)
    if balance < -1 and nodeValue < rootNode.right.data:
        rootNode.right = rotateRight(rootNode.right)
        return rotateLeft(rootNode)
    return rootNode


root = AVLNode(5)
root = insertNode(root, 10)
root = insertNode(root, 15)
root = insertNode(root, 20)
levelOrder(root)
