package net.sorting;

import java.util.ArrayList;
import java.util.List;

/**
 * Simple merge sort implementation
 * 
 * Characteristics: Comparison based divide-and-conquer algorithm. It is
 * a stable algorithm and used comparisons are nearly optimal.
 * 
 * It is also practical for external sorting, like tape drives, when the
 * data to be sorted is too large to fit into memory.
 * 
 * Complexity: Average, Worst -> O(nlogn)
 * 
 * @see <a
 *      href=
 *      "https://en.wikipedia.org/wiki/Merge_sort">https://en.wikipedia.org/wiki/Merge_sort</a>
 */

public class MergeSort extends Sort {

	@Override
	public List<Integer> sort(List<Integer> list) {
		return mergeSort(list);
	}

	private List<Integer> mergeSort(List<Integer> list) {
		if (list.size() <= 1)
			return list;
		int center = list.size() / 2;

		List<Integer> list1 = mergeSort(list.subList(0, center));
		List<Integer> list2 = mergeSort(list.subList(center, list.size()));
		return merge(list1, list2);
	}

	private List<Integer> merge(List<Integer> list1, List<Integer> list2) {
		if (list1.size() < 1)
			return list2;
		if (list2.size() < 1)
			return list1;
		List<Integer> list = new ArrayList<Integer>();
		int i = 0, j = 0;
		while (i < list1.size() && j < list2.size()) {
			if (list1.get(i) <= list2.get(j)) {
				list.add(list1.get(i));
				i++;
			} else {
				list.add(list2.get(j));
				j++;
			}
		}
		while (i < list1.size()) {
			list.add(list1.get(i));
			i++;
		}
		while (j < list2.size()) {
			list.add(list2.get(j));
			j++;
		}
		return list;
	}
}
