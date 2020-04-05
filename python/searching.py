'''
Created on May 15, 2015

@author: tekrei

Various search algorithms
Source: Introduction to Computation and Programming Using Python
'''
import random


def b_search(L: list, e: any, low: int, high: int):
    if high == low:
        return L[low] == e
    mid = (low + high)//2
    if L[mid] == e:
        return True
    elif L[mid] > e:
        if low == mid:  # nothing left to search
            return False
        else:
            return b_search(L, e, low, mid - 1)
    else:
        return b_search(L, e, mid + 1, high)


def binary_search(elements: list, e: any):
    """Recursive binary search
    Assumes elements is a list, the elements of which are in ascending order.
    Returns True if e is in elements and False otherwise"""
    if len(elements) == 0:
        return False
    else:
        return b_search(elements, e, 0, len(elements) - 1)


def linear_search(elements: list, e: any):
    """Assumes elements is a list.
    Returns True if e is in elements and False otherwise"""
    for i in range(len(elements)):
        if elements[i] == e:
            return True
    return False


def simple_check(elements: list, e: any):
    """
    Simple check using *in* operator of Python
    """
    return e in elements


if __name__ == '__main__':
    # generate random 25 numbers as list
    numbers = [random.randint(-10, 10) for x in range(25)]
    print("%s" % sorted(numbers))
    for x in range(-10, 11):
        print("%s %s %s %s" % (x, simple_check(numbers, x),
                               linear_search(numbers, x), binary_search(sorted(numbers), x)))
