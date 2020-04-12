#ifndef INCLUDES_SORT_H_
#define INCLUDES_SORT_H_

#include <utility>

/**
 * Insertion sort: stable, in place O(n^2) sorting algorithm
 */
int *insertion_sort(int *data, int size) {
  for (int j = 1; j < size; j++) {
    int key = data[j];
    int i = j - 1;
    while (i > -1 && data[i] > key) {
      data[i + 1] = data[i];
      i = i - 1;
    }
    data[i + 1] = key;
  }
  return data;
}

/**
 * Selection sort from Introduction to Algorithms (3rd) book
 * Solution of Exercise 2.2-2
 * In place comparison sort, O(n^2) complexity
 * generally performs worse than Insertion Sort. Almost always
 * outperforms bubble sort and gnome sort.
 */
int *selection_sort(int *data, int size) {
  for (int j = 0; j < size - 1; j++) {
    int smallest = j;
    for (int i = j + 1; i < size; i++) {
      if (data[i] < data[smallest]) {
        smallest = i;
      }
    }
    std::swap(data[j], data[smallest]);
  }
  return data;
}

// Merges two subarrays of data[].
// First subarray is data[l..m]
// Second subarray is data[m+1..r]
void merge(int data[], int left, int middle, int right) {
  int i, j, k;
  int n1 = middle - left + 1;
  int n2 = right - middle;

  /* create temp arrays */
  int L[n1], R[n2];

  /* Copy data to temp arrays L[] and R[] */
  for (i = 0; i < n1; i++) L[i] = data[left + i];
  for (j = 0; j < n2; j++) R[j] = data[middle + 1 + j];

  /* Merge the temp arrays back into arr[l..r]*/
  i = 0;     // Initial index of first subarray
  j = 0;     // Initial index of second subarray
  k = left;  // Initial index of merged subarray
  while (i < n1 && j < n2) {
    if (L[i] <= R[j]) {
      data[k] = L[i];
      i++;
    } else {
      data[k] = R[j];
      j++;
    }
    k++;
  }

  /* Copy the remaining elements of L[], if there
 are any */
  while (i < n1) {
    data[k] = L[i];
    i++;
    k++;
  }

  /* Copy the remaining elements of R[], if there
 are any */
  while (j < n2) {
    data[k] = R[j];
    j++;
    k++;
  }
}

// Source: https://www.geeksforgeeks.org/merge-sort/
int *merge_sort(int data[], int start, int end) {
  if (start < end) {
    int middle = start + (end - start) / 2;

    // Sort first and second halves
    merge_sort(data, start, middle);
    merge_sort(data, middle + 1, end);

    merge(data, start, middle, end);
  }
  return data;
}

#endif  // INCLUDES_SORT_H_
