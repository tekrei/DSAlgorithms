package net.tekrei.ds;

public class GraphNode<AnyType> extends Node<AnyType> implements Comparable<GraphNode<AnyType>> {

	// using adjacency list to store the
	private SLinkedList<GraphNode<AnyType>> neighbors;

	// is it visited?
	private boolean visited = false;

	// path fields
	public Integer distance;
	public GraphNode<AnyType> previous;

	public GraphNode(AnyType info) {
		super(info);
	}

	public boolean isVisited() {
		return visited;
	}

	public void visit() {
		this.visited = true;
	}

	public void unvisit() {
		this.visited = false;
	}

	public SLinkedList<GraphNode<AnyType>> getNeighbors() {
		return neighbors;
	}

	public void setNeighbors(SLinkedList<GraphNode<AnyType>> neighbors) {
		this.neighbors = neighbors;
	}

	public GraphNode<AnyType> getNeighbor(int idx) {
		return neighbors.get(idx);
	}

	public boolean removeNeighbor(GraphNode<AnyType> node) {
		return neighbors.remove(node) != null;
	}

	public void addNeighbor(GraphNode<AnyType> node) {
		if (neighbors == null)
			neighbors = new SLinkedList<GraphNode<AnyType>>();
		neighbors.insert(node);
	}

	public int getNeighborCount() {
		return (neighbors != null) ? neighbors.size() : 0;
	}

	public boolean adjacent(GraphNode<AnyType> node) {
		return neighbors != null && neighbors.contains(node);
	}

	@Override
	public int compareTo(GraphNode<AnyType> node) {
		return distance.compareTo(node.distance);
	}
}
