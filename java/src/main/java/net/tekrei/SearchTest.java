package net.tekrei;

import net.tekrei.search.*;

import java.util.Collections;
import java.util.List;

/**
 * Test all search implementations
 */
public class SearchTest {

    //Variable values, to check the behavior of algorithms in different conditions
    private static int LIST_SIZE = 100;
    private static int EXPECTED_INDEX = 95;

    public static void main(String[] args) {
        List<Integer> integers = Utilities.generateIntegerList(LIST_SIZE);
        Collections.sort(integers);
        linearSearch(integers, integers.get(EXPECTED_INDEX));
        binarySearch(integers, integers.get(EXPECTED_INDEX));
        recursiveBinarySearch(integers, integers.get(EXPECTED_INDEX));
        exponentialSearch(integers, integers.get(EXPECTED_INDEX));
        interpolationSearch(integers, integers.get(EXPECTED_INDEX));
    }

    private static void linearSearch(List<Integer> list, int searchKey) {
        LinearSearch linearSearch = new LinearSearch();
        long start = System.nanoTime();
        int foundIndex = linearSearch.search(list, searchKey);
        long end = System.nanoTime();
        if (foundIndex == EXPECTED_INDEX) {
            System.out.println("Index found: " + foundIndex);
            System.out.println("LINEAR search TIME: " + (end - start));
            System.out.println("------------------------------------------");
        } else {
            System.out.println("The linear search algorithm is not working correctly");
        }
    }

    private static void binarySearch(List<Integer> list, int searchKey) {
        BinarySearch binarySearch = new BinarySearch();
        long start = System.nanoTime();
        int foundIndex = binarySearch.search(list, searchKey);
        long end = System.nanoTime();
        if (foundIndex == EXPECTED_INDEX) {
            System.out.println("Index found: " + foundIndex);
            System.out.println("BINARY search TIME: " + (end - start));
            System.out.println("------------------------------------------");
        } else {
            System.out.println("The binary search algorithm is not working correctly");
        }
    }

    private static void recursiveBinarySearch(List<Integer> list, int searchKey) {
        RecursiveBinarySearch recursiveBinarySearch = new RecursiveBinarySearch();
        long start = System.nanoTime();
        int foundIndex = recursiveBinarySearch.recursiveSearch(list, 0, LIST_SIZE, searchKey);
        long end = System.nanoTime();
        if (foundIndex == EXPECTED_INDEX) {
            System.out.println("Index found: " + foundIndex);
            System.out.println("RECURSIVE BINARY search TIME: " + (end - start));
            System.out.println("------------------------------------------");
        } else {
            System.out.println("The recursive binary search algorithm is not working correctly");
        }
    }

    private static void exponentialSearch(List<Integer> list, int searchKey) {
        ExponentialSearch exponentialSearch = new ExponentialSearch();
        long start = System.nanoTime();
        int foundIndex = exponentialSearch.search(list, searchKey);
        long end = System.nanoTime();
        if (foundIndex == EXPECTED_INDEX) {
            System.out.println("Index found: " + foundIndex);
            System.out.println("EXPONENTIAL search TIME: " + (end - start));
            System.out.println("------------------------------------------");
        } else {
            System.out.println("The exponential search algorithm is not working correctly");
        }
    }

    private static void interpolationSearch(List<Integer> list, int searchKey) {
        InterpolationSearch interpolationSearch = new InterpolationSearch();
        long start = System.nanoTime();
        int foundIndex = interpolationSearch.search(list, searchKey);
        long end = System.nanoTime();
        if (foundIndex == EXPECTED_INDEX) {
            System.out.println("Index found: " + foundIndex);
            System.out.println("INTERPOLATION search TIME: " + (end - start));
        } else {
            System.out.println("The interpolation search algorithm is not working correctly");
        }
    }
}
