package net.tekrei.search.impl;

import net.tekrei.search.Search;

import java.util.List;

/**
 * Interpolation search implementation
 *
 * Resembles Binary search algorithm.
 * By comparison, binary search always chooses the middle of the remaining search space,
 * discarding one half or the other,
 * depending on the comparison between the key found at the estimated position
 * and the key sought — it does not require numerical values for the keys, just a total order on them.
 * The remaining search space is reduced to the part before or after the estimated position.
 * The linear search uses equality only as it compares elements one-by-one from the start, ignoring any sorting.
 *
 * Complexity: worst case O(n), best case O(1), average case O(log(log(n)))
 *
 * @see <a href=https://en.wikipedia.org/wiki/Interpolation_search />
 *
 */
public class InterpolationSearch extends Search {

    @Override
    public int search(List<Integer> list, int searchKey) {
        int lowerBound = 0;
        int upperBound = list.size() - 1;
        int middleBound;

        while ((lowerBound <= upperBound) && (searchKey >= list.get(lowerBound) && (searchKey <= list.get(upperBound)))) {
            middleBound = lowerBound + (((upperBound-lowerBound) /
                    (list.get(upperBound)-list.get(lowerBound))*(searchKey - list.get(lowerBound))));

            if (list.get(middleBound) == searchKey) {
                return middleBound;
            }

            if (list.get(middleBound) < searchKey) {
                lowerBound = middleBound + 1;
            }

            else {
                upperBound = middleBound - 1;
            }
        }

        return -1; //Not found
    }
}
