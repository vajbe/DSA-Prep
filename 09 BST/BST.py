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
preOrder(newBST)