package net.tekrei.search;

import java.util.List;

/**
 * Recursive binary search implementation
 *
 * @see BinarySearch
 */
public class RecursiveBinarySearch {

    public int recursiveSearch(List<Integer> list, int firstElement, int lastElement, int searchKey) {

        if (lastElement >= firstElement) {
            int middle = firstElement + (lastElement - firstElement) / 2;

            if (list.get(middle) == searchKey) {
                return middle;
            }

            if (list.get(middle) > searchKey) {
                return recursiveSearch(list, firstElement, middle - 1, searchKey);
            }

            return recursiveSearch(list, middle + 1, lastElement, searchKey);
        }

        return -1;
    }
}