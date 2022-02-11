package net.ds;

/**
 * First In First Out (FIFO) data structure
 * 
 * @param <AnyType>
 *                  type of the data stored in it
 * 
 * @see <a
 *      href=
 *      "https://en.wikipedia.org/wiki/Queue_%28abstract_data_type%29">https://en.wikipedia.org/wiki/Queue_%28abstract_data_type%29</a>
 */
public class Queue<AnyType> {

	SLinkedList<AnyType> list = new SLinkedList<AnyType>();

	public AnyType dequeue() {
		if (size() > 0) {
			return list.remove(0);
		}
		return null;
	}

	public void enqueue(AnyType info) {
		list.insert(info);
	}

	public AnyType peek() {
		return list.get(0);
	}

	public boolean isEmpty() {
		return list.size() == 0;
	}

	public int size() {
		return list.size();
	}

	public String toString() {
		return list.toString();
	}

}
