package net.tekrei.ds.impl;

import net.tekrei.ds.LinkedList;
import net.tekrei.ds.SLLNode;

/**
 * Singly linked list implementation
 * 
 * @author tekrei
 *
 * @param <AnyType>
 *            type of the data stored in it
 * 
 *            For more information @see {@linktourl
 *            https://en.wikipedia.org/wiki/Linked_list}
 */
public class SLinkedList<AnyType> extends LinkedList<AnyType> {

	SLLNode<AnyType> head;

	public SLinkedList() {
		head = null;
		size = 0;
	}

	@Override
	public AnyType get(int idx) {
		if (idx < 0)
			return null;
		if (idx == 0) {
			return head.getInfo();
		} else {
			SLLNode<AnyType> temp = head;
			int i = 0;
			while (temp.getNext() != null) {
				temp = (SLLNode<AnyType>) temp.getNext();
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
			SLLNode<AnyType> temp = head;
			int i = 0;
			while (temp.getNext() != null) {
				temp = (SLLNode<AnyType>) temp.getNext();
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
	public void insert(AnyType x) {
		SLLNode<AnyType> node = new SLLNode<AnyType>(x);
		if (head == null) {
			head = node;
		} else {
			SLLNode<AnyType> temp = head;
			while (temp.getNext() != null) {
				temp = (SLLNode<AnyType>) temp.getNext();
			}
			temp.setNext(node);
		}
		size++;
	}

	@Override
	public AnyType remove(int idx) {
		AnyType info = null;
		if (idx >= 0) {
			// remove head
			if (idx == 0) {
				info = head.getInfo();
				head = (SLLNode<AnyType>) head.getNext();
				size--;
				// remove another element
			} else {
				SLLNode<AnyType> temp = head;
				SLLNode<AnyType> prev = null;
				int i = 0;
				while (temp.getNext() != null) {
					prev = temp;
					temp = (SLLNode<AnyType>) temp.getNext();
					i++;
					if (i == idx) {
						info = temp.getInfo();
						prev.setNext(temp.getNext());
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
	public String toString() {
		String str = "[";
		SLLNode<AnyType> temp = head;
		// single linked list traversal
		while (temp != null) {
			str += temp.getInfo();
			if (temp.getNext() != null)
				str += ", ";
			temp = (SLLNode<AnyType>) temp.getNext();
		}
		return str + "]";
	}
}