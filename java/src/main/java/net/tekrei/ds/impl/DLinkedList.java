package net.tekrei.ds.impl;

import net.tekrei.ds.DLLNode;
import net.tekrei.ds.LinkedList;

/**
 * Doubly linked list implementation
 * 
 * @author tekrei
 *
 * @param <AnyType>
 *            type of the data stored in it
 * 
 * @see <a
 *      href="https://en.wikipedia.org/wiki/Linked_list">https://en.wikipedia.org/wiki/Linked_list</a>
 */
public class DLinkedList<AnyType> extends LinkedList<AnyType> {
	DLLNode<AnyType> head;

	public DLinkedList() {
		head = null;
		size = 0;
	}

	@Override
	public void insert(AnyType x) {
		DLLNode<AnyType> node = new DLLNode<AnyType>(x);
		if (head == null) {
			head = node;
		} else {
			DLLNode<AnyType> temp = head;
			while (temp.getNext() != null) {
				temp = (DLLNode<AnyType>) temp.getNext();
			}
			node.setPrevious(temp);
			temp.setNext(node);
		}
		size++;
	}

	@Override
	public AnyType remove(int idx) {
		AnyType info = null;
		if (idx >= 0) {
			if (idx == 0) {
				info = head.getInfo();
				((DLLNode<AnyType>) head.getNext()).setPrevious(null);
				head = (DLLNode<AnyType>) head.getNext();
				size--;
				// remove another element
			} else {
				DLLNode<AnyType> temp = head;
				int i = 0;
				while (temp.getNext() != null) {
					temp = (DLLNode<AnyType>) temp.getNext();
					i++;
					if (i == idx) {
						info = temp.getInfo();
						((DLLNode<AnyType>) temp.getNext()).setPrevious(temp
								.getPrevious());
						temp.getPrevious().setNext(temp.getNext());
						temp = null;
						size--;
						break;
					}
				}
			}
		}
		return info;
	}

	@Override
	public AnyType get(int idx) {
		if (idx < 0)
			return null;
		if (idx == 0) {
			return head.getInfo();
		} else {
			DLLNode<AnyType> temp = head;
			int i = 0;
			while (temp.getNext() != null) {
				temp = (DLLNode<AnyType>) temp.getNext();
				i++;
				if (i == idx) {
					return temp.getInfo();
				}
			}
		}
		return null;
	}

	@Override
	public AnyType set(int idx, AnyType x) {
		// update head
		AnyType value = null;
		if (idx < 0)
			return value;
		if (idx == 0) {
			value = head.getInfo();
			head.setInfo(x);
		} else {
			DLLNode<AnyType> temp = head;
			int i = 0;
			while (temp.getNext() != null) {
				temp = (DLLNode<AnyType>) temp.getNext();
				i++;
				if (i == idx) {
					value = temp.getInfo();
					temp.setInfo(x);
					break;
				}
			}
		}
		return value;
	}

	@Override
	public String toString() {
		String str = "[";
		DLLNode<AnyType> temp = head;
		// single linked list traversal
		while (temp != null) {
			str += temp.getInfo();
			if (temp.getNext() != null)
				str += ", ";
			temp = (DLLNode<AnyType>) temp.getNext();
		}
		return str + "]";
	}
}
