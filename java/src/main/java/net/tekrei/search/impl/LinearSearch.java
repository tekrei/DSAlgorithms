package net.tekrei.search.impl;

import net.tekrei.search.Search;

import java.util.List;

/**
 * Linear search implementation
 *
 * It sequentially checks each element of the list until a match is found or the whole list has been searched
 *
 * Complexity: average and worst case O(n), best case O(1)
 *
 * @see <a href=https://en.wikipedia.org/wiki/Linear_search />
 */
public class LinearSearch extends Search {

    @Override
    public int search(List<Integer> list, int searchKey) {
        for (int index = 0; index < list.size(); index++) {
            if (list.get(index) == searchKey)
                return index;
        }

        return -1; //Not found
    }
}
