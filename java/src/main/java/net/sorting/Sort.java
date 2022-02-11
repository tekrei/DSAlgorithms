package net.sorting;

import java.util.List;

/**
 * 
 * Abstract class for sort algorithms
 *
 */
public abstract class Sort {

	/**
	 * Method to sort collection It must be implemented in all subclasses
	 * 
	 * @param list
	 * @return sorted list
	 */
	public abstract List<Integer> sort(List<Integer> list);

	/**
	 * Simple swap method
	 * 
	 * @param list
	 * @param i
	 * @param j
	 */
	public void swap(List<Integer> list, Integer i, Integer j) {
		Integer temp = list.get(i);
		list.set(i, list.get(j));
		list.set(j, temp);
	}

}
