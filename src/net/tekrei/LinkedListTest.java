package net.tekrei;

import java.util.List;

import net.tekrei.ds.impl.DLinkedList;
import net.tekrei.ds.impl.SLinkedList;

public class LinkedListTest {

	public static void main(String[] args) {
		SLinkedList<Integer> linkedList = new SLinkedList<Integer>();
		List<Integer> integerList = SortingTest.generateIntegerList(10);
		DLinkedList<Integer> dlinkedList = new DLinkedList<Integer>();
		System.out.println(integerList);
		for (Integer i : integerList) {
			linkedList.insert(i);
			dlinkedList.insert(i);
		}
		System.out.println(linkedList);
		System.out.println(dlinkedList);
		linkedList.remove(5);
		dlinkedList.remove(8);
		System.out.println(linkedList);
		System.out.println(dlinkedList);
	}

}
