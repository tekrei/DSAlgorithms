package net.tekrei.ds.impl;

/**
 * First In First Out (FIFO) data structure
 * 
 * @author tekrei
 *
 * @param <AnyType>
 *            type of the data stored in it
 * 
 *            For more information @see {@linktourl
 *            https://en.wikipedia.org/wiki/Queue_%28abstract_data_type%29}
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
