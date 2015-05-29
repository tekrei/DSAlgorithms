'''
Created on May 16, 2015

@author: tekrei
Graph implementation and algorithms
Using adjacency list represantation for the graph
Source: Introduction to Computation and Programming Using Python
'''
from _collections import defaultdict
from Queue import PriorityQueue



class Node(object):
    def __init__(self, name):
        self.name = name
    def getName(self): return self.name
    def __str__(self): return self.name

class Edge(object):
    def __init__(self, src, dst, wgt=1.0):
        self.source = src
        self.destination = dst
        self.weight = wgt
    def getSource(self): return self.source
    def getDestination(self): return self.destination
    def getWeight(self): return self.weight
    def __str__(self): return str(self.source) + '->(' + str(self.weight) + ')' + str(self.destination) 

class Digraph(object):
    def __init__(self):
        self.nodes = []
        self.edges = defaultdict()
        self.weight = defaultdict()
    def addNode(self, node):
        if node in self.nodes:
            raise ValueError('Duplicate node')
        else:
            self.nodes.append(node)
            self.edges[node] = []
    def addEdge(self, edge):
        src = edge.getSource()
        dst = edge.getDestination()
        wgt = edge.getWeight()
        if not(src in self.nodes and dst in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append(dst)
        self.weight[src, dst] = wgt
    def getWeight(self, src, dst):
        try:
            return self.weight[src, dst]
        except KeyError:
            return float('inf')
    def adjacent(self, node):
        try: 
            return self.edges[node]
        except KeyError:
            return []
    def hasNode(self, node): return node in self.nodes
    def vertices(self): return self.nodes
    def __str__(self):
        res = ''
        for k in self.edges:
            for d in self.edges[k]:
                res += str(k) + '->' + str(d) +'('+str(self.getWeight(k,d))+')\n'
        return res[:-1]

class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource(), edge.getWeight())
        Digraph.addEdge(self, rev)
        
def DFS(graph, start, end, path=[], shortest=None):
    path = path + [start]
    if start == end:
        return path
    for node in graph.adjacent(start):
        if node not in path:
            if shortest == None or len(path) < len(shortest):
                newPath = DFS(graph, node, end, path, shortest)
                if newPath != None:
                    shortest = newPath
    return shortest

def BFS(graph, start, end):
    initPath = [start]
    pathQueue = [initPath]
    visited = [start]
    while len(pathQueue) != 0:
        tmpPath = pathQueue.pop(0)
        lastNode = tmpPath[-1]
        if lastNode == end:
            return tmpPath
        for nextNode in graph.adjacent(lastNode):
            if nextNode not in visited:
                newPath = tmpPath + [nextNode]
                pathQueue.append(newPath)
    return None

def printPath(path):
    result = ''
    for i in range(len(path)):
        if i == len(path) - 1:
            result = result + str(path[i])
        else:
            result = result + str(path[i]) + '->'
    return result

def dijkstra(graph, start):
    '''
    works on non-negative weighted graphs
    '''
    #queue = PQueue()
    queue = PriorityQueue()
    
    dist = dict()
    parent = dict()
    
    dist[start] = 0
    parent[start] = None
    
    for vertex in graph.vertices():
        if start != vertex:
            dist[vertex] = float('inf')
            parent[vertex] = None
        queue.put((dist[vertex],vertex))
    while not queue.empty():
        _, u = queue.get()
        for v in graph.adjacent(u):
            newDistance = dist[u] + graph.getWeight(u, v)
            #print "src:"+str(u)+" dst:"+ str(v)+ " newDistance:"+str(newDistance)
            if dist[v] > newDistance:
                dist[v] = newDistance
                parent[v] = u
                #update the priority of the node in the queue
                #FIX THIS
                queue.put((newDistance, v))
    return dist, parent

def dijsktraTest(startNode):
    '''
    dijkstra test
    '''
    D, _ = dijkstra(graph, startNode)
    result = ''
    for n in nodes:
        result += str(startNode) + "->" + str(n) + "=" + str(D[n]) + "\n"
    return result

if __name__ == '__main__':
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

    print "DFS:", printPath(DFS(graph, nodes[0], nodes[6]))
    print "BFS:", printPath(DFS(graph, nodes[0], nodes[6]))
    print "Dijkstra result:", dijsktraTest(nodes[0])
    print "Dijkstra result:", dijsktraTest(nodes[5])
