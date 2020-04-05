package net.tekrei.search.impl;

import net.tekrei.search.Search;

import java.util.List;

/**
 * Binary search implementation
 *
 * Binary search compares the target value to the middle element of the array.
 * If they are not equal, the half in which the target cannot lie is eliminated
 * and the search continues on the remaining half, again taking the middle element to compare to the target value,
 * and repeating this until the target value is found.
 * If the search ends with the remaining half being empty, the target is not in the array.
 *
 * Complexity: average and worst case O(log n), best case O(1)
 *
 * @see <a href=https://en.wikipedia.org/wiki/Binary_search_algorithm />
 */
public class BinarySearch extends Search {

    @Override
    public int search(List<Integer> list, int searchKey) {
        int lowerBound = 0;
        int upperBound = list.size() - 1;
        int middleBound;

        while(lowerBound <= upperBound) {
            middleBound = (lowerBound + upperBound) / 2;
            if(list.get(middleBound) == searchKey) {
                return middleBound;
            }
            else if(list.get(middleBound) < searchKey) {
                lowerBound = middleBound + 1;
            }
            else if(list.get(middleBound) > searchKey) {
                upperBound = middleBound - 1;
            }
        }

        return -1; //Not found
    }
}
