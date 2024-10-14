class Graph:
    def __init__(self, graph=None):
        if not graph:
            self.adjaceny_list = {}

    def addEdge(self, vertex1, vertex2):
        self.adjaceny_list[vertex1].append(vertex2)
        self.adjaceny_list[vertex2].append(vertex1)

    def removeEdge(self, vertex1, vertex2):
        self.adjaceny_list[vertex1].remove(vertex2)
        self.adjaceny_list[vertex2].remove(vertex1)

    def addVertex(self, vertex):
        self.adjaceny_list[vertex] = []

    def removeVertex(self, vertex):
        if vertex in self.adjaceny_list.keys():
            for elem in self.adjaceny_list[vertex]:
                self.adjaceny_list[elem].remove(vertex)

    def showGraph(self):
        print(self.adjaceny_list)

    def BFS(self, vertex):
        order = []
        visited = set()
        visited.add(vertex)
        order.append(vertex)
        queue = [vertex]

        while queue:
            current = queue.pop(0)
            for elem in self.adjaceny_list[current]:
                if elem not in visited:
                    visited.add(elem)
                    order.append(elem)
                    queue.append(elem)

        print(order)

    def DFS(self, vertex):
        order = []
        visited = set()
        visited.add(vertex)
        order.append(vertex)
        stack = [vertex]

        while stack:
            current = stack.pop()
            if current not in visited:
                visited.add(current)
                order.append(current)

            for elem in self.adjaceny_list[current]:
                if elem not in visited:
                    stack.append(elem)

        print(order)


if __name__ == "__main__":
    graph = Graph()

    graph.addVertex("A")
    graph.addVertex("B")
    graph.addVertex("C")
    graph.addVertex("D")
    graph.addVertex("E")

    graph.addEdge("A", "B")
    graph.addEdge("A", "C")
    graph.addEdge("B", "E")
    graph.addEdge("C", "D")
    graph.addEdge("E", "D")

    graph.showGraph()

    graph.DFS("A")

    print("test")
