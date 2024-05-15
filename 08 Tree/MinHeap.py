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

newHeap = Heap(5)
insertNode(newHeap, 4, "max")
insertNode(newHeap, 5, "max")
insertNode(newHeap, 2, "max")
insertNode(newHeap, 1, "max")
levelOrderTraversal(newHeap)
