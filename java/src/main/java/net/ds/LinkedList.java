package net.ds;

/**
 * Abstract class for linked list implementations
 * 
 * @param <AnyType>
 *                  type of the data stored in it
 * 
 * @see <a
 *      href=
 *      "https://en.wikipedia.org/wiki/Linked_list">https://en.wikipedia.org/wiki/Linked_list</a>
 */
public abstract class LinkedList<AnyType> {

	protected int size = 0;

	public abstract AnyType get(int idx);

	public abstract AnyType set(int idx, AnyType x);

	public abstract void insert(AnyType x);

	public abstract AnyType remove(int idx);

	public int size() {
		return size;
	}

}
