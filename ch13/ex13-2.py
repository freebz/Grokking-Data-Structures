# 그래프 구현

# 인접 리스트

class Vertex:
    def __init__(self, key):
        self.id = key
        self._adj_list = SinglyLinkedList()
    def has_edge_to(self, destination_vertex):
        return self._adj_list._search(destination_vertex) is not None
    def add_edge_to(self, destination_vertex):
        if self.has_edge_to(destination_vertex):
            raise ValueError(f'간선이 이미 존재합니다: {self} -> {destination_vertex}')
        self._adj_list.insert_in_front(destination_vertex)


class Graph:
    def __init__(self):
        self._adj = {}
    

    def _get_vertex(self, key):
        if key not in self._adj:
            raise ValueError(f'정점 {key}가 존재하지 않습니다!')
        return self._adj[key]
    

    def insert_vertex(self, key):
        if key in self._adj:
            raise ValueError(f'정점 {key}가 이미 존재합니다!')
        self._adj[key] = Graph.Vertex(key)
    

    def insert_edge(self, key1, key2):
        v1 = self._get_vertex(key1)
        v2 = self._get_vertex(key2)
        v1.add_edge_to(v2)
    

    def delete_vertex(self, key):
        v = self._get_vertex(key)
        for u in self._adj.values():
            if u != v and u.has_edge_to(v):
                u.remove_edge_to(v)
        del self._adj[key]