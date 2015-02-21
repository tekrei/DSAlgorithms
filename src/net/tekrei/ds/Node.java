package net.tekrei.ds;

/**
 * Node class to hold information
 * 
 * @author tekrei
 *
 * @param <AnyType>
 *            type of the data stored in it
 */
public class Node<AnyType> {
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
}
