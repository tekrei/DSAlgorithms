/*
 * Searching.cpp
 *
 *  Created on: Jun 1, 2015
 *      Author: tekrei
 */

#include <iostream>
#include <cstdlib>
using namespace std;

/**
 * UTILITY FUNCTIONS
 */
/**
 * Generate random integer numbers as an array
 * count: array size to generate
 */
int* generate(int count) {
	int* result = new int[count];
	for (int i = 0; i < count; i++) {
		//generate integer in the range 0 to 99
		result[i] = rand() % 100;
	}
	return result;
}

/**
 * Swap two elements indexed by i,j of data array
 */
void swap(int* data, int i, int j) {
	int temp = data[i];
	data[i] = data[j];
	data[j] = temp;
}

/**
 * Print array to the screen
 */
void print(int* numbers, int count) {
	for (int i = 0; i < count - 1; i++) {
		cout << numbers[i] << ", ";
	}
	cout << numbers[count - 1] << "\n";
}

//END OF UTILITY FUNCTIONS

/**
 * SEARCHING
 */
int bSearch(int* L, int e, int low, int high) {
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
			return bSearch(L, e, low, mid - 1);
		}
	} else {
		return bSearch(L, e, mid + 1, high);
	}
}

/**
 * Recursive binary search
 * Assumes L is a list, the elements of which are in ascending order.
 * Returns index if e is in L and -1 otherwise
 */
int binarySearch(int* array, int count, int e) {
	if (count == 0) {
		return -1;
	} else {
		return bSearch(array, e, 0, count - 1);
	}
}

/**
 * Assumes L is a list.
 * Returns index if e is in L and -1 otherwise
 */
int linearSearch(int* L, int count, int e) {
	for (int i = 0; i < count; i++) {
		if (L[i] == e) {
			return i;
		}
	}
	return -1;
}
//END OF SEARCHING

/**
 * SORTING
 */

/**
 * Insertion sort: stable, in place O(n^2) sorting algorithm
 */
int* insertion_sort(int* data, int size) {
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
int* selection_sort(int* data, int size) {
	for (int j = 0; j < size - 1; j++) {
		int smallest = j;
		for (int i = j + 1; i < size; i++) {
			if (data[i] < data[smallest]) {
				smallest = i;
			}
		}
		swap(data, j, smallest);
	}
	return data;
}

/**
 * Merge method of merge sort
 * Input: lists to merge
 * Output: merged result
 */
int* merge(int* left, int left_count, int* right, int right_count){
    int left_index = 0;
    int right_index = 0;
	int index = 0;
    int* result = new int[left_count+right_count];
    while(left_index < left_count && right_index < right_count){
        if(left[left_index] < right[right_index]){
            result[index++]=left[left_index];
            left_index++;
        }else{
            result[index++] = right[right_index];
            right_index++;
        }
    }
    while(left_index < left_count){
        result[index++] = left[left_index];
        left_index++;
    }
    while(right_index < right_count){
        result[index++] = right[right_index];
        right_index++;
    }
    return result;
}
/**
 * Merge sort implementation
 * Input: any list which contains comparable elements
 * Output: sorted list
 * O(nlgn)
 */
int* merge_sort(int* data, int start, int end){
	int size = end - start;
    if(size < 2) return data;
    int middle = (start+end) / 2;
    int left_count = middle;
    int right_count = size - middle;
    return merge(merge_sort(data, 0, middle), left_count, merge_sort(data, middle+1, size-1), right_count);
}

//END OF SORTING

int main() {
//generate random integer array
	int numberCount = 25;
	int* numbers = generate(numberCount);
	cout << "Unsorted:";
	print(numbers, numberCount);
	cout << "Insertion sort:";
	print(insertion_sort(numbers, numberCount), numberCount);
	cout << "Selection sort:";
	print(selection_sort(numbers, numberCount), numberCount);
	cout << "Merge sort:";
	print(merge_sort(numbers, 0, numberCount), numberCount);
}

