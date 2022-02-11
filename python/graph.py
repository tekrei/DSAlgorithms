"""
Created on May 16, 2015

Graph implementation and algorithms
Using adjacency list represantation for the graph
Source: Introduction to Computation and Programming Using Python
"""
from collections import defaultdict
from queue import PriorityQueue
import time
from typing import Type


class Node:
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return self.name


class Edge:
    def __init__(
        self, source: Type[Node], destination: Type[Node], weight: float = 1.0
    ):
        self.source = source
        self.destination = destination
        self.weight = weight

    def __str__(self):
        return str(self.source) + "->(" + str(self.weight) + ")" + str(self.destination)


class Digraph:
    def __init__(self):
        self.nodes = []
        self.edges = defaultdict()
        self.weight = defaultdict()

    def addNode(self, node: Type[Node]):
        if node in self.nodes:
            raise ValueError("Duplicate node")
        else:
            self.nodes.append(node)
            self.edges[node] = []

    def addEdge(self, edge: Type[Edge]):
        src = edge.source
        dst = edge.destination
        wgt = edge.weight
        if not (src in self.nodes and dst in self.nodes):
            raise ValueError("Node not in graph")
        self.edges[src].append(dst)
        self.weight[src, dst] = wgt

    def getWeight(self, source: Type[Node], destination: Type[Node]):
        try:
            return self.weight[source, destination]
        except KeyError:
            return float("inf")

    def adjacent(self, node: Type[Node]):
        try:
            return self.edges[node]
        except KeyError:
            return []

    def hasNode(self, node):
        return node in self.nodes

    def vertices(self):
        return self.nodes

    def __str__(self):
        res = ""
        for k in self.edges:
            for d in self.edges[k]:
                res += str(k) + "->" + str(d) + "(" + str(self.getWeight(k, d)) + ")\n"
        return res[:-1]


class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        rev = Edge(edge.destination, edge.source, edge.weight)
        Digraph.addEdge(self, rev)


def DFS(
    graph: Digraph,
    start: Type[Node],
    end: Type[Node],
    path: list = [],
    shortest: list = None,
):
    path = path + [start]
    if start == end:
        return path
    for node in graph.adjacent(start):
        if node not in path:
            if shortest == None or len(path) < len(shortest):
                new_path = DFS(graph, node, end, path, shortest)
                if new_path != None:
                    shortest = new_path
    return shortest


def BFS(graph: Graph, start: Type[Node], end: Type[Node]):
    init_path = [start]
    path_queue = [init_path]
    visited = [start]
    while len(path_queue) != 0:
        tmp_path = path_queue.pop(0)
        last_node = tmp_path[-1]
        if last_node == end:
            return tmp_path
        for next_node in graph.adjacent(last_node):
            if next_node not in visited:
                new_path = tmp_path + [next_node]
                path_queue.append(new_path)
    return None


def print_path(path: list) -> str:
    result = ""
    for i in range(len(path)):
        if i == len(path) - 1:
            result = result + str(path[i])
        else:
            result = result + str(path[i]) + "->"
    return result


def dijkstra(graph: Graph, start: Type[Node]):
    """
    works on non-negative weighted graphs
    """
    queue = PriorityQueue()

    dist = dict()
    parent = dict()

    dist[start] = 0
    parent[start] = None

    for vertex in graph.vertices():
        if start != vertex:
            dist[vertex] = float("inf")
            parent[vertex] = None
        queue.put((dist[vertex], time.time(), vertex))
    while not queue.empty():
        _, _, u = queue.get()
        for v in graph.adjacent(u):
            new_distance = dist[u] + graph.getWeight(u, v)
            # print("src:%s dst:%s new distance:%s"%(str(u), str(v), str(new_distance)))
            if dist[v] > new_distance:
                dist[v] = new_distance
                parent[v] = u
                # update the priority of the node in the queue
                queue.put((new_distance, time.time(), v))
    return dist, parent


def dijsktra_test(start_node: Type[Node]):
    """
    dijkstra test
    """
    D, _ = dijkstra(graph, start_node)
    result = ""
    for n in nodes:
        result += str(start_node) + "->" + str(n) + "=" + str(D[n]) + "\n"
    return result


if __name__ == "__main__":
    graph = Graph()
    nodes = []
    for name in range(10):
        nodes.append(Node(str(name)))

    for n in nodes:
        graph.addNode(n)

    graph.addEdge(Edge(nodes[0], nodes[1]))
    graph.addEdge(Edge(nodes[1], nodes[2]))
    graph.addEdge(Edge(nodes[2], nodes[3]))
    graph.addEdge(Edge(nodes[2], nodes[4]))
    graph.addEdge(Edge(nodes[3], nodes[5]))
    graph.addEdge(Edge(nodes[3], nodes[6]))
    graph.addEdge(Edge(nodes[0], nodes[7]))
    graph.addEdge(Edge(nodes[0], nodes[8]))
    graph.addEdge(Edge(nodes[0], nodes[9]))

    print("BFS:%s" % print_path(BFS(graph, nodes[0], nodes[6])))
    print("DFS:%s" % print_path(DFS(graph, nodes[0], nodes[6])))
    print("Dijkstra result for node %s:\n%s" % (nodes[0], dijsktra_test(nodes[0])))
    print("Dijkstra result for node %s:\n%s" % (nodes[5], dijsktra_test(nodes[5])))
