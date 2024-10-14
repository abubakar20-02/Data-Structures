class Graph:

    def __init__(self, graph=None):
        if not graph:
            self.adjacent_list = {}

    def addVertex(self, vertex):
        self.adjacent_list[vertex] = []

    def addEdge(self, vertex1, vertex2):
        self.adjacent_list[vertex1].append(vertex2)

    def showGraph(self):
        print(self.adjacent_list)

    def topologicalSortUtil(self, vertex, visited, stack):
        visited.append(vertex)
        for elem in self.adjacent_list[vertex]:
            if elem not in visited:
                self.topologicalSortUtil(elem, visited, stack)
        stack.insert(0, vertex)

    def topologicalSort(self):
        visited = []
        stack = []
        for elem in self.adjacent_list.keys():
            if elem not in visited:
                self.topologicalSortUtil(elem, visited, stack)

        print(stack)


if __name__ == "__main__":
    graph = Graph()
    graph.addVertex("A")
    graph.addVertex("B")
    graph.addVertex("C")
    graph.addVertex("D")
    graph.addVertex("E")
    graph.addVertex("F")
    graph.addVertex("G")
    graph.addVertex("H")

    graph.addEdge("A", "C")
    graph.addEdge("C", "E")
    graph.addEdge("E", "H")
    graph.addEdge("E", "F")
    graph.addEdge("F", "G")
    graph.addEdge("D", "F")
    graph.addEdge("B", "D")
    graph.addEdge("B", "C")

    graph.showGraph()

    graph.topologicalSort()
