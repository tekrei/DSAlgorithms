#ifndef INCLUDES_SEARCH_H_
#define INCLUDES_SEARCH_H_

/**
 * binary search
 */
int b_search(int *L, int e, int low, int high) {
  if (high == low) {
    return L[low] == e;
  }
  int mid = (low + high) / 2;
  if (L[mid] == e) {
    return mid;
  } else if (L[mid] > e) {
    if (low == mid) {
      return -1;
    } else {
      return b_search(L, e, low, mid - 1);
    }
  } else {
    return b_search(L, e, mid + 1, high);
  }
}

/**
 * Recursive binary search
 * Assumes L is a list, the elements of which are in ascending order.
 * Returns index if e is in L and -1 otherwise
 */
int binary_search(int *array, int count, int e) {
  if (count == 0) {
    return -1;
  } else {
    return b_search(array, e, 0, count - 1);
  }
}

/**
 * Assumes L is a list.
 * Returns index if e is in L and -1 otherwise
 */
int linear_search(int *L, int count, int e) {
  for (int i = 0; i < count; i++) {
    if (L[i] == e) {
      return i;
    }
  }
  return -1;
}

#endif  // INCLUDES_SEARCH_H_
