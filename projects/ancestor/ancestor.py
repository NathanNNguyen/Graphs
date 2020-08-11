class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError('Nonexistent vertex')

    def get_ancestor(self, vertex):
        return self.vertices[vertex]


def earliest_ancestor(ancestors, starting_node):
    graph = Graph()
    for parent, child in ancestors:

        graph.add_vertex(parent)
        graph.add_vertex(child)
        graph.add_edge(child, parent)

    q = Queue()
    q.enqueue([starting_node])
    max_path_length = 1
    aged_one = -1

    while q.size():
        path = q.dequeue()
        vertex = path[-1]

        if (len(path) == max_path_length and vertex < aged_one) or (len(path) > max_path_length):
            aged_one = vertex
            max_path_length = len(path)

        for neighbor in graph.vertices[vertex]:
            path_copy = list(path)
            path_copy.append(neighbor)
            q.enqueue(path_copy)

    return aged_one
