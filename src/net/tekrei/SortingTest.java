package net.tekrei;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;

import net.tekrei.sorting.impl.BucketSort;
import net.tekrei.sorting.impl.HeapSort;
import net.tekrei.sorting.impl.InsertionSort;
import net.tekrei.sorting.impl.MergeSort;
import net.tekrei.sorting.impl.QuickSort;

public class SortingTest {

	private static Random randomGenerator = new Random();
	private static boolean DEBUG = false;

	public static void main(String[] args) {
		List<Integer> list = generateIntegerList(10000);
		insertionSort(cloneList(list));
		mergeSort(cloneList(list));
		quickSort(cloneList(list));
		heapSort(cloneList(list));
		bucketSort(cloneList(list));
	}

	@SuppressWarnings("unchecked")
	private static List<Integer> cloneList(List<Integer> list) {
		return (List<Integer>) ((ArrayList<Integer>) list).clone();
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

	public static List<Integer> generateIntegerList(int size) {
		List<Integer> list = new ArrayList<Integer>();
		for (int i = 0; i < size; i++) {
			list.add(randomInt(size * size));
		}
		return list;
	}

	public static Integer randomInt(int upper) {
		return randomGenerator.nextInt(upper);
	}
}
