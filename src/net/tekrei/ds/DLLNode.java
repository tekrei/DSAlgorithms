package net.tekrei.ds;

/**
 * Doubly linked list node
 * 
 * @author tekrei
 *
 * @param <AnyType>
 *            type of the data stored in it
 * 
 *            For more information @see {@linktourl
 *            https://en.wikipedia.org/wiki/Linked_list}
 */
public class DLLNode<AnyType> extends SLLNode<AnyType> {

	private Node<AnyType> previous;

	public DLLNode(AnyType info) {
		super(info);
		this.previous = null;
	}

	public DLLNode<AnyType> getPrevious() {
		return (DLLNode<AnyType>) previous;
	}

	public void setPrevious(DLLNode<AnyType> prev) {
		this.previous = prev;
	}
}
