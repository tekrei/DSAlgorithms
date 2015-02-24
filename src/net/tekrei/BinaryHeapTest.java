package net.tekrei;

import java.util.List;

import net.tekrei.ds.impl.BinaryHeap;

public class BinaryHeapTest {
	public static void main(String[] args) {
		BinaryHeap<Integer> heap = new BinaryHeap<Integer>(15);
		List<Integer> integerList = SortingTest.generateIntegerList(10);
		System.out.println(integerList);
		for (Integer i : integerList) {
			heap.insert(i);
		}

		while (!heap.isEmpty()) {
			System.out.println(heap.remove());
		}
	}

}
