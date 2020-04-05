package net.tekrei;

import java.util.List;

import net.tekrei.sorting.*;

public class SortingTest {

	private static boolean DEBUG = false;

	public static void main(String[] args) {
		List<Integer> list = Utilities.generateIntegerList(10000);
		insertionSort(Utilities.cloneList(list));
		mergeSort(Utilities.cloneList(list));
		quickSort(Utilities.cloneList(list));
		heapSort(Utilities.cloneList(list));
		bucketSort(Utilities.cloneList(list));
	}

	private static List<Integer> insertionSort(List<Integer> list) {
		System.out.println("INSERTION SORT");
		System.out.println("--------------------------------------");
		if (DEBUG)
			System.out.println("UNSORTED" + list);
		long start = System.nanoTime();
		list = (new InsertionSort()).sort(list);
		long end = System.nanoTime();
		if (DEBUG)
			System.out.println("SORTED" + list);
		System.out.println("TIME:" + (end - start));
		System.out.println("--------------------------------------");
		return list;
	}

	private static List<Integer> mergeSort(List<Integer> list) {
		System.out.println("MERGE SORT");
		System.out.println("--------------------------------------");
		if (DEBUG)
			System.out.println("UNSORTED" + list);
		long start = System.nanoTime();
		list = (new MergeSort()).sort(list);
		long end = System.nanoTime();
		if (DEBUG)
			System.out.println("SORTED" + list);
		System.out.println("TIME:" + (end - start));
		System.out.println("--------------------------------------");
		return list;
	}

	private static List<Integer> quickSort(List<Integer> list) {
		System.out.println("QUICK SORT");
		System.out.println("--------------------------------------");
		if (DEBUG)
			System.out.println("UNSORTED" + list);
		long start = System.nanoTime();
		list = (new QuickSort()).sort(list);
		long end = System.nanoTime();
		if (DEBUG)
			System.out.println("SORTED" + list);
		System.out.println("TIME:" + (end - start));
		System.out.println("--------------------------------------");
		return list;
	}

	private static List<Integer> heapSort(List<Integer> list) {
		System.out.println("HEAP SORT");
		System.out.println("--------------------------------------");
		if (DEBUG)
			System.out.println("UNSORTED" + list);
		long start = System.nanoTime();
		list = (new HeapSort()).sort(list);
		long end = System.nanoTime();
		if (DEBUG)
			System.out.println("SORTED" + list);
		System.out.println("TIME:" + (end - start));
		System.out.println("--------------------------------------");
		return list;
	}

	private static List<Integer> bucketSort(List<Integer> list) {
		System.out.println("BUCKET SORT");
		System.out.println("--------------------------------------");
		if (DEBUG)
			System.out.println("UNSORTED" + list);
		long start = System.nanoTime();
		list = (new BucketSort()).sort(list);
		long end = System.nanoTime();
		if (DEBUG)
			System.out.println("SORTED" + list);
		System.out.println("TIME:" + (end - start));
		System.out.println("--------------------------------------");
		return list;
	}
}
