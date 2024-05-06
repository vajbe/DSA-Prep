class Heap:
    def __init__(self, size: int) -> None:
        self.customList = (size + 1) * [None]
        self.maxSize = size + 1
        self.heapSize = 0


def peek(rootNode: Heap) -> int:
    if not rootNode:
        return
    return rootNode.customList[1]
