package net.tekrei;

import java.util.List;

import net.tekrei.ds.impl.Queue;

public class QueueTest {

	public static void main(String[] args) {
		Queue<Integer> queue = new Queue<Integer>();
		List<Integer> integerList = SortingTest.generateIntegerList(10);
		for (Integer i : integerList) {
			queue.enqueue(i);
			System.out.println(queue);
		}
		while (!queue.isEmpty()) {
			System.out.println(queue.dequeue());
		}
	}

}
