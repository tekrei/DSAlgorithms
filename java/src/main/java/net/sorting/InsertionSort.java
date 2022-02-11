package net.sorting;

import java.util.List;

/**
 * Insertion Sort Algorithm implementation
 * 
 * Characteristics: Comparison based simple, stable, adaptive, in-place,
 * and online sorting algorithm preferred for low number of collections.
 * 
 * Complexity: Best -> O(n) Average, Worst -> O(n^2)
 *
 * @see <a
 *      href=
 *      "https://en.wikipedia.org/wiki/Insertion_sort">https://en.wikipedia.org/wiki/Insertion_sort</a>
 */

public class InsertionSort extends Sort {

	@Override
	public List<Integer> sort(List<Integer> list) {
		for (int i = 1; i < list.size(); i++) {
			int j = i;
			while (j > 0 && list.get(j - 1) > list.get(j)) {
				swap(list, j, j - 1);
				j = j - 1;
			}
		}
		return list;
	}

}
