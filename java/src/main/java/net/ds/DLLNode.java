package net.ds;

/**
 * Doubly linked list node
 * 
 * @param <AnyType>
 *                  type of the data stored in it
 * 
 * @see <a
 *      href=
 *      "https://en.wikipedia.org/wiki/Linked_list">https://en.wikipedia.org/wiki/Linked_list</a>
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
