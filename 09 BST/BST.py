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
            
newBST = BSTNode(None)
print(insertNode(newBST, 80))
print(insertNode(newBST, 60))
print(insertNode(newBST, 70))
print(insertNode(newBST, 90))
print(newBST.data)
print(newBST.left.data)
print(newBST.right.data)