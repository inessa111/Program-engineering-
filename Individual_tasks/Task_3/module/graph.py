class Graph:
    def __init__(self):
        self.edges = []
        self.vertices = set([1])

    def degree(self, v):  # вернуть число - степень вершины с номером v
        cnt = 0
        for i in self.edges:
            if v in i:
                cnt += 1
        return cnt

    def addVertex(self, new_n):
        self.vertices.add(new_n)

    def addEdge(self, new_n, n):
        self.edges.append((new_n, n))

    def generate_vertex(self):
        return len(self.vertices) + 1
