class Heap:
    def __init__(self, size: int) -> None:
        self.customList = (size + 1) * [None]
        self.maxSize = size + 1
        self.heapSize = 0


def peek(rootNode: Heap) -> int:
    if not rootNode:
        return
    return rootNode.customList[1]


def levelOrderTraversal(root: Heap) -> None:
    if not root:
        return
    for i in range(1, root.heapSize + 1):
        print(root.customList[i])


def heapifyInsert(rootNode: Heap, index: int, heapType: str) -> None:
    parentIndex = int(index / 2)
    if index <= 1:
        return

    if heapType == "min":
        if rootNode.customList[parentIndex] > rootNode.customList[index]:
            rootNode.customList[parentIndex], rootNode.customList[index] = (
                rootNode.customList[index],
                rootNode.customList[parentIndex],
            )
        heapifyInsert(rootNode, parentIndex, heapType)
    elif heapType == "max":
        if rootNode.customList[parentIndex] < rootNode.customList[index]:
            rootNode.customList[parentIndex], rootNode.customList[index] = (
                rootNode.customList[index],
                rootNode.customList[parentIndex],
            )
        heapifyInsert(rootNode, parentIndex, heapType)


def insertNode(rootNode: Heap, nodeValue: int, heapType: str):
    if rootNode.heapSize + 1 == rootNode.maxSize:
        return "Tree is full"
    rootNode.customList[rootNode.heapSize + 1] = nodeValue
    rootNode.heapSize += 1
    heapifyInsert(rootNode, rootNode.heapSize, heapType)
    return "The value has been inserted."


def heapifyTreeExtract(rootNode: Heap, index: int, heapTye: str) -> None:
    leftIndex = index * 2
    rightIndex = (index * 2) + 1
    swapChild = 0

    if rootNode.heapSize < leftIndex:
        return
    elif rootNode.heapSize == leftIndex:
        if heapTye == "min":
            if rootNode.customList[index] > rootNode.customList[leftIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = temp
                return
        else:
            if rootNode.customList[index] < rootNode.customList[leftIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = temp
                return
    else:
        if heapTye == "min":
            if rootNode.customList[leftIndex] < rootNode.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex

            if rootNode.customList[index] > rootNode.customList[swapChild]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[swapChild]
                rootNode.customList[swapChild] = temp
        else:
            if rootNode.customList[leftIndex] > rootNode.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex

            if rootNode.customList[index] < rootNode.customList[swapChild]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[swapChild]
                rootNode.customList[swapChild] = temp
        heapifyTreeExtract(rootNode, swapChild, heapTye)


def extractNode(rootNode: Heap, heapType: str):
    if rootNode.heapSize == 0:
        return
    else:
        extractNode = rootNode.customList[1]
        rootNode.customList[1] = rootNode.customList[rootNode.heapSize]
        rootNode.customList[rootNode.heapSize] = None
        rootNode.heapSize -= 1
        heapifyTreeExtract(rootNode, 1, heapType)
        return extractNode
    
def deleteEntireBP(rootNode: Heap):
    rootNode.customList = None


newHeap = Heap(5)
insertNode(newHeap, 4, "max")
insertNode(newHeap, 5, "max")
insertNode(newHeap, 2, "max")
insertNode(newHeap, 1, "max")
print(extractNode(newHeap, "max"))
levelOrderTraversal(newHeap)
