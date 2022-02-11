package net.sorting;

import java.util.List;

/**
 * Heapsort implementation
 * 
 * Characteristics: another comparison based sorting algorithm. Although
 * somewhat slower in practice on most machines than a well-implemented
 * quicksort, it has the advantage of a more favorable worst-case O(n
 * log n) runtime. Heapsort is an in-place algorithm, but it is not a
 * stable sort.
 * 
 * Complexity: average, best and worst case O(nlogn)
 *
 * @see <a
 *      href=
 *      "https://en.wikipedia.org/wiki/Quick_sort">https://en.wikipedia.org/wiki/Quick_sort</a>
 */

public class HeapSort extends Sort {

	@Override
	public List<Integer> sort(List<Integer> list) {
		heapify(list);

		Integer end = list.size() - 1;
		while (end > 0) {
			swap(list, end, 0);
			end--;
			siftDown(list, 0, end);
		}
		return list;
	}

	private void heapify(List<Integer> list) {
		Integer start = (list.size() - 2) / 2;
		while (start >= 0) {
			siftDown(list, start, list.size() - 1);
			start--;
		}
	}

	private void siftDown(List<Integer> list, Integer start, Integer end) {
		Integer root = start;
		while (root * 2 + 1 <= end) {
			Integer child = root * 2 + 1;
			Integer swap = root;
			if (list.get(swap) < list.get(child)) {
				swap = child;
			}
			if (child + 1 <= end && list.get(swap) < list.get(child + 1)) {
				swap = child + 1;
			}
			if (swap == root) {
				return;
			} else {
				swap(list, root, swap);
				root = swap;
			}
		}
	}
}
