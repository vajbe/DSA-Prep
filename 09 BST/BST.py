class BSTNode:
    def __init__(self, data) -> None:
        self.data = data
        self.right = None
        self.left = None

def insertNode(rootNode, nodeValue):
    if rootNode.data is None:
        rootNode.data = nodeValue
    elif nodeValue <= rootNode.data:        
        if rootNode.left is None:            
            node = BSTNode(nodeValue)
            rootNode.left = node
        else:
            insertNode(rootNode.left, nodeValue)
    else:
         if rootNode.right is None:            
            node = BSTNode(nodeValue)
            rootNode.right = node
         else:
            insertNode(rootNode.right, nodeValue)
    return "Node has been inserted"

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

def search(rootNode:BSTNode, nodeValue):
    if rootNode is None:
        print("Either tree is empty or value not found")
        return

    if rootNode.data == nodeValue:
        print("Value found")
    elif nodeValue < rootNode.data:
        search(rootNode.left, nodeValue)
    else:
        search(rootNode.right, nodeValue)

def minValueNode(rootNode):
    current = rootNode
    while current.left is not None:
        current = current.left
    return current

def deleteNode(rootNode: BSTNode, nodeValue:int):
    if rootNode is None:
        return None
    if nodeValue < rootNode.data:
        rootNode.left = deleteNode(rootNode.left, nodeValue)
    elif nodeValue > rootNode.data:  
        rootNode.right= deleteNode(rootNode.right, nodeValue)
    else:
        if rootNode.left is None:
            temp = rootNode.right
            rootNode = None
            return temp
        if rootNode.right is None:
            temp = rootNode.left
            rootNode = None
            return temp        

        temp = minValueNode(rootNode.right)
        rootNode.data = temp.data
        rootNode.right = deleteNode(rootNode.right, temp.data)
    return rootNode
    

newBST = BSTNode(None)
insertNode(newBST, 70)
insertNode(newBST, 50)
insertNode(newBST, 90)
insertNode(newBST, 30)
insertNode(newBST, 60)
insertNode(newBST, 80)
insertNode(newBST, 100)
insertNode(newBST, 20)
insertNode(newBST, 40)
# preOrder(newBST)
# inOrder(newBST)
# 
# search(newBST, 65)
deleteNode(newBST, 100)
postOrder(newBST)