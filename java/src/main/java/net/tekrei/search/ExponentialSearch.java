package net.tekrei.search;

import net.tekrei.search.Search;

import java.util.Arrays;
import java.util.List;

/**
 * Exponential search implementation
 *
 * There are numerous ways to implement this with the most common being to determine a range
 * that the search key resides in and performing a binary search within that range.
 * This takes O(log i) where i is the position of the search key in the list, if the search key is in the list,
 * or the position where the search key should be, if the search key is not in the list.
 *
 * Complexity: average and worst case O(log i), best case O(1)
 *
 * @see <a href=https://en.wikipedia.org/wiki/Exponential_search />
 *
 */
public class ExponentialSearch extends Search {
    @Override
    public int search(List<Integer> list, int searchKey) {

        if (list.get(0) == searchKey) {
            return 0;
        }
        if (list.get(list.size() - 1) == searchKey) {
            return list.size();
        }

        int range = 1;

        while (range < list.size() && list.get(range) <= searchKey) {
            range = range * 2;
        }

        return Arrays.binarySearch(
                list.stream().mapToInt(i -> i).toArray(),
                range / 2,
                Math.min(range, list.size()),
                searchKey
        );
    }
}
