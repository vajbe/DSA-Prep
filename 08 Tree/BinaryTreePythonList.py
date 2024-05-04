class BinaryTree:
    #TC=O(1) SC=O(N)
    def __init__(self, size):
        self.customList = [None] * size
        self.lastUsedIndex = 0
        self.maxSize = size
    #TC=O(1) SC=O(1)
    def insert(self, value):
        if self.lastUsedIndex + 1 == self.maxSize:
            return "BT is full"
        else:
            self.customList[self.lastUsedIndex + 1] = value
            self.lastUsedIndex += 1
            return "Value has been inserted"

    #TC=O(N) SC=O(1)
    def search(self, nodeValue):
        for i in range(0, len(self.customList)):
            if self.customList[i] == nodeValue:
                return "Value found"
        return "Value not found"

    def preOrder(self, index):
        if index > self.lastUsedIndex:
            return
        print(self.customList[index])
        self.preOrder(index*2) #Left subtree
        self.preOrder(index*2+1) #Right subtree
        
    def postOrder(self, index):
        if index > self.lastUsedIndex:
            return        
        self.postOrder(index*2) #Left subtree
        self.postOrder(index*2+1) #Right subtree
        print(self.customList[index])

    def inOrder(self, index):
        if index > self.lastUsedIndex:
            return
        self.inOrder(index*2) #Left subtree
        print(self.customList[index])        
        self.inOrder(index*2+1) #Right subtree    

    def levelOrderTraverse(self, index):
        for i in range(index, self.lastUsedIndex + 1):
            print(self.customList[i])

    def deleteNode(self, nodeValue):
        if self.lastUsedIndex  == 0:
            return "Tree is empty"        
        index = 0
        for i in range(1, self.lastUsedIndex + 1):
            if self.customList[i] == nodeValue:
                index = i
                break
        if index == 0:
            return "Element Not found"
        self.customList[index] = self.customList[self.lastUsedIndex]
        self.customList[self.lastUsedIndex] = None
        self.lastUsedIndex -= 1
        return "Element has been deleted"


newBT = BinaryTree(8)
print(newBT.insert("Drinks"))
print(newBT.insert("Hot"))
print(newBT.insert("Cold"))
print(newBT.insert("Tea"))
print(newBT.insert("Coffee"))

# print(newBT.search("Cold"))
# newBT.preOrder(1)
# newBT.inOrder(1)
# newBT.postOrder(1)
newBT.levelOrderTraverse(1)
print(newBT.deleteNode("Hot"))
newBT.levelOrderTraverse(1)

