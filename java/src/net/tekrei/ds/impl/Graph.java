package net.tekrei.ds.impl;

import java.util.PriorityQueue;

import net.tekrei.ds.GraphNode;

/**
 * 
 * @author tekrei
 * 
 *         A simple undirected, unweighted graph implementation which uses
 *         singly linked list to store nodes and nodes storing edges using
 *         singly linked list
 *
 * @param <AnyType>
 *            data type to store in the graph
 * 
 * @see <a
 *      href="http://en.wikipedia.org/wiki/Graph_%28abstract_data_type%29">http://en.wikipedia.org/wiki/Graph_%28abstract_data_type%29</a>
 */
public class Graph<AnyType> {

	private SLinkedList<GraphNode<AnyType>> nodes;
	// store edge count and update it at every edge operation
	private Integer edgeCount = 0;

	/**
	 * 
	 * @param node
	 * @return list of neighbors
	 */
	public SLinkedList<GraphNode<AnyType>> neighbors(GraphNode<AnyType> node) {
		return node.getNeighbors();
	}

	public GraphNode<AnyType> getNode(int i) {
		return nodes.get(i);
	}

	/**
	 * add new edge between the node and neighbor
	 * 
	 * @param node
	 * @param neighbor
	 */
	public void addEdge(GraphNode<AnyType> node, GraphNode<AnyType> neighbor) {
		if (node != neighbor) {
			if (!node.adjacent(neighbor)) {
				node.addNeighbor(neighbor);
				neighbor.addNeighbor(node);
			}
		}
	}

	public GraphNode<AnyType> add(AnyType info) {
		GraphNode<AnyType> node = new GraphNode<AnyType>(info);
		addNode(node);
		return node;
	}

	/**
	 * add a new node to the graph
	 * 
	 * @param node
	 */
	public void addNode(GraphNode<AnyType> node) {
		if (nodes == null)
			nodes = new SLinkedList<GraphNode<AnyType>>();
		nodes.insert(node);
	}

	/**
	 * remove information from graph
	 * 
	 * @param node
	 * @return
	 */
	public AnyType remove(AnyType info) {
		return removeNode(new GraphNode<AnyType>(info));
	}

	private AnyType removeNode(GraphNode<AnyType> node) {
		// first remove edges
		for (int i = 0; i < nodes.size(); i++) {
			nodes.get(i).removeNeighbor(node);
		}
		// now it is safe to remove the node
		return nodes.remove(node).getInfo();
	}

	public boolean removeEdge(GraphNode<AnyType> node,
			GraphNode<AnyType> neighbor) {
		return node.removeNeighbor(neighbor);
	}

	/**
	 * 
	 * @return number of nodes in the graph
	 */
	public Integer size() {
		return nodes.size();
	}

	public Integer edgeCount() {
		return edgeCount;
	}

	private void resetVisits() {
		for (int i = 0; i < size(); i++) {
			nodes.get(i).unvisit();
		}
	}

	/**
	 * Breadth First Search traversal of the graph
	 * 
	 * @param start
	 *            starting point of the traversal
	 * @return string representation of the BFS traversal
	 * @see <a
	 *      href="http://en.wikipedia.org/wiki/Breadth-first_search">http://en.wikipedia.org/wiki/Breadth-first_search</a>
	 */
	public String bfs(GraphNode<AnyType> start) {
		resetVisits();
		String str = "BFS:[";
		GraphNode<AnyType> temp;
		Queue<GraphNode<AnyType>> queue = new Queue<GraphNode<AnyType>>();
		start.visit();
		queue.enqueue(start);
		str += start.getInfo();
		while (!queue.isEmpty()) {
			temp = queue.dequeue();
			for (int i = 0; i < temp.getNeighborCount(); i++) {
				GraphNode<AnyType> neighbor = temp.getNeighbor(i);
				if (!neighbor.isVisited()) {
					neighbor.visit();
					queue.enqueue(neighbor);
					str += " " + neighbor.getInfo();
				}
			}
		}
		return str + "]";
	}

	/**
	 * Depth First Search traversal of the graph
	 * 
	 * @param start
	 *            starting point of the traversal
	 * @return string representation of the DFS traversal
	 * @see <a
	 *      href="http://en.wikipedia.org/wiki/Depth-first_search">http://en.wikipedia.org/wiki/Depth-first_search</a>
	 */
	public String dfs(GraphNode<AnyType> start) {
		resetVisits();
		String str = "DFS:[";
		Stack<GraphNode<AnyType>> stack = new Stack<GraphNode<AnyType>>();
		stack.push(start);
		while (!stack.isEmpty()) {
			GraphNode<AnyType> temp = stack.pop();
			if (!temp.isVisited()) {
				str += " " + temp.getInfo();
				temp.visit();
				for (int i = 0; i < temp.getNeighborCount(); i++) {
					stack.push(temp.getNeighbor(i));
				}
			}
		}
		return str + "]";
	}

	public void computeDistance(GraphNode<AnyType> start) {
		PriorityQueue<GraphNode<AnyType>> queue = new PriorityQueue<GraphNode<AnyType>>();

		// initialization
		for (int i = 0; i < size(); i++) {
			GraphNode<AnyType> node = nodes.get(i);
			node.distance = -1;
			node.previous = null;
		}

		start.distance = 0;
		queue.add(start);

		// finding the paths
		while (!queue.isEmpty()) {
			GraphNode<AnyType> node = queue.poll();
			// visit neighbors
			for (int i = 0; i < node.getNeighborCount(); i++) {
				GraphNode<AnyType> neighbor = node.getNeighbor(i);
				int distance = node.distance + 1;
				if (distance < neighbor.distance || neighbor.distance == -1) {
					queue.remove(neighbor);
					neighbor.distance = distance;
					neighbor.previous = node;
					queue.add(neighbor);
				}
			}
		}
	}

	private String getShortestPathTo(GraphNode<AnyType> end) {
		String path = end.toString();
		while (end.previous != null) {
			path = end.previous + path;
			end = end.previous;
		}
		return path;
	}

	/**
	 * Dijkstra's shortest path algorithm
	 * 
	 * @param start
	 * @return result of the application of Dijkstra
	 * @see <a
	 *      href="http://en.wikipedia.org/wiki/Dijkstra%27s_algorithm">http://en.wikipedia.org/wiki/Dijkstra%27s_algorithm</a> <br/>
	 *      <a href="http://www.algolist.com/code/java/Dijkstra%27s_algorithm">
	 *      http://www.algolist.com/code/java/Dijkstra%27s_algorithm</a>
	 */
	public String dijkstra(GraphNode<AnyType> start) {
		String str = "DIJKSTRA\nStarting Node:" + start + "\n";
		computeDistance(start);
		for (int i = 0; i < size(); i++) {
			GraphNode<AnyType> node = nodes.get(i);
			str += "=>" + node + "|" + getShortestPathTo(node) + "("
					+ node.distance + ")\n";
		}
		return str;
	}

	public String toString() {
		String str = "";
		for (int i = 0; i < nodes.size(); i++) {
			GraphNode<AnyType> node = nodes.get(i);
			str += node.getInfo() + "\t=>{" + node.getNeighbors() + "}\n";
		}
		return str;
	}

}
