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
