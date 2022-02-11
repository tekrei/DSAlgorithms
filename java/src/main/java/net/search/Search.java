package net.search;

import java.util.List;

/**
 * Abstract class for search algorithms
 */
public abstract class Search {

    /**
     * Method to sort collection It must be implemented in all subclasses
     *
     * @param list      - sorted list
     * @param searchKey - target value
     * @return index of the list
     */
    public abstract int search(List<Integer> list, int searchKey);
}
