class Graph:
    def __init__(self, list=None) -> None:
        if list is None:
            list = {}
        self.list = list

    def addVertex(self, vertex):
        if vertex not in self.list:
            self.list[vertex] = []
            return True
        return False

    def addEdge(self, vertexA, vertexB):
        self.list[vertexA].append(vertexB)
        self.list[vertexB].append(vertexA)

    def removeEdge(self, vertexA, vertexB):
        if vertexA in self.list.keys() and vertexB in self.list.keys():
            self.list[vertexA].remove(vertexB)
            self.list[vertexB].remove(vertexA)
            return True
        return False

    def printGraph(self):
        print("\n")
        for vertex in self.list:
            print(vertex, " : ", self.list[vertex])

    def removeVertex(self, vertex):
        if vertex in self.list.keys():
            for other_vertex in self.list[vertex]:
                if vertex in self.list[other_vertex]:
                    self.list[other_vertex].remove(vertex)
            del self.list[vertex]
            return True
        return False


list = {"a": ["b", "c"], "b": ["a"], "c": ["a", "b"]}
graph = Graph(list)
graph.addVertex("d")
graph.addEdge("c", "d")
graph.printGraph()
# graph.removeEdge("a", "c")
# graph.printGraph()
graph.removeVertex("d")
graph.printGraph()
