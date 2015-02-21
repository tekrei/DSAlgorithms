package net.tekrei.ds;

/**
 * Singly linked list node
 * 
 * @author tekrei
 *
 * @param <AnyType>
 *            type of the data stored in it
 * 
 *            For more information @see {@linktourl
 *            https://en.wikipedia.org/wiki/Linked_list}
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
