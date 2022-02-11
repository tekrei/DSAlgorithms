package net.ds;

/**
 * Node class to hold information
 * 
 * @param <AnyType>
 *                  type of the data stored in it
 */
public class Node<AnyType> {

	public Node() {
	}

	public Node(AnyType info) {
		information = info;
	}

	protected AnyType information;

	public AnyType getInfo() {
		return information;
	}

	public void setInfo(AnyType info) {
		information = info;
	}

	public String toString() {
		return "[" + information + "]";
	}

	public boolean isEquals(Node<AnyType> other) {
		return other.getInfo().equals(getInfo());
	}

}
