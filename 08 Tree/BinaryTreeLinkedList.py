import QueueList
class TreeNode:
    def __init__(self, data) -> None:
        self.data=data
        self.left = None
        self.right = None
    
def preOrder(root:TreeNode):
    if not root:
        return 
    print(root.data)
    preOrder(root.left)
    preOrder(root.right)
    
def inOrder(root:TreeNode):
    if not root:
        return
    inOrder(root.left)
    print(root.data)    
    inOrder(root.right)

def postOrder(root:TreeNode):
    if not root:
        return
    postOrder(root.left)
    postOrder(root.right)
    print(root.data)    
        
#Level order traversal
def traverse(rootNode):
    if not rootNode:
        return
    customQueue = QueueList.Queue()
    customQueue.enqueue(rootNode)
    while not customQueue.isEmpty():
        root = customQueue.dequeue()
        print("-",root.data)
        if(root.left is not None):            
            customQueue.enqueue(root.left)
        if(root.right is not None):            
            customQueue.enqueue(root.right)
        
        
def insert(rootNode, node):
    if not rootNode:
        rootNode = node
    else:
        customQueue = QueueList.Queue()
        customQueue.enqueue(rootNode)
        while not customQueue.isEmpty():
            root = customQueue.dequeue()
            # print(root.data)
            if root.left is not None:
                customQueue.enqueue(root.left)
            else:
                root.left = node
                return
            if root.right is not None:
                customQueue.enqueue(root.right)
            else:
                root.right = node
                return

def getDeepestNode(rootNode:TreeNode) -> TreeNode | None: 
    if not rootNode:
        return None
    else:
        customQueue = QueueList.Queue()
        customQueue.enqueue(rootNode)
        while not customQueue.isEmpty():
            root = customQueue.dequeue()    
            if(root.left is not None):            
                customQueue.enqueue(root.left)
            if(root.right is not None):            
                customQueue.enqueue(root.right)
        deepstNode = root
        return deepstNode

def deleteDeepestNode(rootNode:TreeNode, dNode:TreeNode) -> None:
    if not rootNode:
        return
    else:
        customQueue = QueueList.Queue()
        customQueue.enqueue(rootNode)        
        while not customQueue.isEmpty():
            root = customQueue.dequeue()
            if root is dNode:
                root.data = None
            else:                
                if root.right:
                    if root.right is dNode:
                        root.right = None
                        return
                    else:
                        customQueue.enqueue(root.right)       
                if root.left:
                    if root.left is dNode:
                        root.left = None
                        return
                    else:
                        customQueue.enqueue(root.left)          
    return 

def deleteNode(rootNode:TreeNode, node):
    if not rootNode:
        return "Binary Tree does not exist"
    else:
        customQueue = QueueList.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.data == node:
                dNode = getDeepestNode(rootNode)
                root.data = dNode.data
                deleteDeepestNode(rootNode, dNode)
                return "The node has been deleted"
            if(root.left is not None):            
                customQueue.enqueue(root.left)
            if(root.right is not None):            
                customQueue.enqueue(root.right)
    return "Failed to delete node"    

drink = TreeNode("Drinks")
cold = TreeNode("Cold")
fanta = TreeNode("Fanta")
santa = TreeNode("Santa")
hot = TreeNode("Hot")
insert(drink, cold)
insert(drink, hot)
insert(drink, fanta)
insert(drink, santa)
# traverse(drink)
# print('----------')
# preOrder(drink)
# print('----------')
# postOrder(drink)
# print('----------')
# inOrder(drink)
# print("Deepest Node is ")
# deep = getDeepestNode(drink)
# deleteDeepestNode(drink, deep)
# deep = getDeepestNode(drink)
# deleteDeepestNode(drink, deep)
print(deleteNode(drink, "Cold"))
traverse(drink)