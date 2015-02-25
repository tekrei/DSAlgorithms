package net.tekrei.sorting.impl;

import java.util.List;

import net.tekrei.sorting.Sort;

/**
 * Quick Sort implementation
 * 
 * @author tekrei
 * 
 *         Characteristics: Efficient. With a good implementation beats merge
 *         sort and heap sort. Efficient implementations is not stable. It can
 *         operate in-place. It is a divide-and-conquer algorithm.
 * 
 *         Complexity: average case: O(nlogn) worst case: O(n^2) (but it is
 *         rare)
 * 
 *         For improvement median-of-three partitioning can be used.
 *
 * @see <a
 *      href="https://en.wikipedia.org/wiki/Quick_sort">https://en.wikipedia.org/wiki/Quick_sort</a>
 */

public class QuickSort extends Sort {
	@Override
	public List<Integer> sort(List<Integer> list) {
		if (list.size() <= 1)
			return list;
		Integer pivot = partition(list);
		sort(list.subList(0, pivot));
		sort(list.subList(pivot + 1, list.size()));
		return list;
	}

	private Integer partition(List<Integer> list) {
		Integer pivotIndex = list.size() / 2;
		Integer pivotValue = list.get(pivotIndex);
		swap(list, pivotIndex, list.size() - 1);
		Integer storeIndex = 0;
		for (int i = 0; i < list.size() - 1; i++) {
			if (list.get(i) <= pivotValue) {
				swap(list, i, storeIndex);
				storeIndex++;
			}
		}
		swap(list, storeIndex, list.size() - 1);
		return storeIndex;
	}

}
