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


class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)


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
        if vertex in self.vertices:
            return self.vertices[vertex]
        else:
            raise IndexError('Nonexistent vertex')


def build_graph(ancestors):
    graph = Graph()
    for parent, child in ancestors:

        graph.add_ancestor(parent)
        graph.add_ancestor(child)
        graph.add_edge(parent, child)
    return graph


def earliest_ancestor(ancestors, starting_node):
    graph = build_graph(ancestors)
