package net.ds;

/**
 * Singly linked list node
 * 
 * @param <AnyType>
 *                  type of the data stored in it
 * 
 * @see <a
 *      href=
 *      "https://en.wikipedia.org/wiki/Linked_list">https://en.wikipedia.org/wiki/Linked_list</a>
 */
public class SLLNode<AnyType> extends Node<AnyType> {

	private Node<AnyType> next;

	public SLLNode(AnyType info) {
		this.information = info;
		this.next = null;
	}

	public Node<AnyType> getNext() {
		return next;
	}

	public void setNext(Node<AnyType> next) {
		this.next = next;
	}

}
