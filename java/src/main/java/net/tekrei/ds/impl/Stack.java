package net.tekrei.ds.impl;

/**
 * Last In First Out (LIFO) data structure
 * 
 * @author tekrei
 *
 * @param <AnyType>
 *            type of the data stored in it
 * 
 * @see <a
 *      href="https://en.wikipedia.org/wiki/Stack_%28abstract_data_type%29">https://en.wikipedia.org/wiki/Stack_%28abstract_data_type%29</a>
 */
public class Stack<AnyType> {

	SLinkedList<AnyType> list = new SLinkedList<AnyType>();

	public void push(AnyType info) {
		list.insert(info);
	}

	public AnyType pop() {
		if (list.size() > 0)
			return list.remove(list.size() - 1);
		return null;
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
