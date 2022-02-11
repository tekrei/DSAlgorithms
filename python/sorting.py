'''
Created on May 3, 2015

Note: The sorting algorithm used in most Python
implementations is called timsort

'''
import random
import time
from math import floor


def swap(data: list, i: int, j: int):
    '''
    Simple swap function for lists
    '''
    temp = data[i]
    data[i] = data[j]
    data[j] = temp


def selection_sort(data: list):
    '''
    Selection sort from Introduction to Algorithms (3rd) book
    Solution of Exercise 2.2-2
    In place comparison sort, O(n^2) complexity
    generally performs worse than Insertion Sort. Almost always
    outperforms bubble sort and gnome sort.
    '''
    size = len(data)
    for j in range(0, size - 1):
        smallest = j
        for i in range(j + 1, size):
            if data[i] < data[smallest]:
                smallest = i
        swap(data, j, smallest)
    return data


def insertion_sort(data: list):
    '''
    Insertion sort implementation O(n^2)
    Input: any list which contains comparable elements
    Output: sorted list
    O(n^2) complexity
    Simple algorithm, efficient for small data sets, more
    efficient than selection, bubble, etc.
    Adaptive, stable, in place and online.
    '''
    for j in range(1, len(data)):
        key = data[j]
        i = j - 1
        while i > -1 and data[i] > key:
            data[i + 1] = data[i]
            i = i - 1
        data[i + 1] = key
    return data


def merge(left: list, right: list):
    '''
    Merge method of merge sort
    Input: lists to merge
    Output: merged result
    '''
    left_index = 0
    right_index = 0
    result = []
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    while left_index < len(left):
        result.append(left[left_index])
        left_index += 1
    while right_index < len(right):
        result.append(right[right_index])
        right_index += 1
    return result


def merge_sort(data: list):
    '''
    Merge sort implementation
    Input: any list which contains comparable elements
    Output: sorted list
    O(nlgn)
    '''
    if len(data) < 2:
        return data
    middle = int(len(data) / 2)
    left = data[0:middle]
    right = data[middle:]
    return merge(merge_sort(left), merge_sort(right))


def partition(data: list, left: int, right: int):
    '''
    partition method of quick sort
    '''
    pivot = data[right]
    i = left - 1
    for j in range(left, right):
        if data[j] <= pivot:
            i = i + 1
            swap(data, i, j)
    swap(data, i + 1, right)
    return i + 1


def qsort(data: list, left: int, right: int):
    '''
    Quick sort helper
    '''
    if left < right:
        pivot = partition(data, left, right)
        qsort(data, left, pivot - 1)
        qsort(data, pivot + 1, right)


def quick_sort(data: list):
    '''
    Quick sort implementation
    Input: any list which contains comparable elements
    Output: sorted list
    O(nlgn)
    '''
    qsort(data, 0, len(data) - 1)
    return data


def quick_sort2(data: list):
    '''
    Another quick sort implementation
    Source:
    http://stackoverflow.com/questions/25690175/bucket-sort-faster-than-quicksort
    '''
    if len(data) <= 1:
        return data
    low, pivot, high = partition2(data)
    return quick_sort2(low) + [pivot] + quick_sort2(high)


def partition2(data: list):
    '''
    Partition for second quick sort
    '''
    pivot, data = data[0], data[1:]
    low = [x for x in data if x <= pivot]
    high = [x for x in data if x > pivot]
    return low, pivot, high


def bucket_sort(data: list):
    '''
    Bucket sort implementation
    '''
    maximum = max(data)
    buckets = []
    # using maximum/ buckets
    [buckets.append([]) for i in range(int(maximum / 10) + 1)]

    for number in data:
        buckets[int(number / 10)].append(number)
    for index, bucket in enumerate(buckets):
        buckets[index] = quick_sort2(bucket)
    result = []
    for bucket in buckets:
        for number in bucket:
            result.append(number)
    return result


def heap_sort(data: list):
    '''
    Heap sort implementation
    Input: any list which contains comparable elements
    Output: sorted list
    O(nlgn)
    '''
    size = len(data)
    heapify(data, size)
    end = size - 1
    while end > 0:
        swap(data, end, 0)
        end = end - 1
        sift_down(data, 0, end)
    return data


def heapify(data: list, count: int):
    '''
    Heap creation method for heap sort
    '''
    start = int(floor((count - 2) / 2))
    while start >= 0:
        sift_down(data, start, count - 1)
        start = start - 1


def sift_down(data: list, start: int, end: int):
    '''
    Heap property restoration method for heap sort
    '''
    root = start
    while int(floor(root * 2 + 1)) <= end:
        child = int(floor(root * 2 + 1))
        temp = root
        if data[temp] < data[child]:
            temp = child
        if child + 1 <= end and data[temp] < data[child + 1]:
            temp = child + 1
        if temp == root:
            return
        else:
            swap(data, root, temp)
            root = temp


if __name__ == '__main__':
    '''
    Main method to test sorting implementations
    Merge sort and heapsort achieve O(nlgn) upper bound
    in the worst case; quick_sort2 achieves it on average
    '''
    numbers = [random.randint(0, 25) for x in range(100)]
    print("Unsorted Array:\t%s" % numbers)
    start_time = time.time()
    print("---------------\nINSERTION SORT\n---------------")
    print(insertion_sort(numbers.copy()))
    print("%f" % (time.time() - start_time))
    start_time = time.time()
    print("---------------\nSELECTION SORT\n---------------")
    print(selection_sort(numbers.copy()))
    print("%f" % (time.time() - start_time))
    start_time = time.time()
    print("---------------\nMERGE SORT\n---------------")
    print(merge_sort(numbers.copy()))
    print("%f" % (time.time() - start_time))
    start_time = time.time()
    print("---------------\nQUICK SORT\n---------------")
    print(quick_sort(numbers.copy()))
    print("%f" % (time.time() - start_time))
    start_time = time.time()
    print("---------------\nQUICK SORT 2\n---------------")
    print(quick_sort2(numbers.copy()))
    print("%f" % (time.time() - start_time))
    start_time = time.time()
    print("---------------\nHEAP SORT\n---------------")
    print(heap_sort(numbers.copy()))
    print("%f" % (time.time() - start_time))
    start_time = time.time()
    print("---------------\nBUCKET SORT\n---------------")
    print(bucket_sort(numbers.copy()))
    print("%f" % (time.time() - start_time))
