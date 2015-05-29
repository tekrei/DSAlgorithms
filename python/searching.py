'''
Created on May 15, 2015

@author: tekrei

Various search algorithms
Source: Introduction to Computation and Programming Using Python
'''
import random

def bSearch(L, e, low, high):
    if high == low:
        return L[low] == e
    mid = (low + high)//2
    if L[mid] == e:
        return True
    elif L[mid] > e:
        if low == mid: #nothing left to search
            return False
        else:
            return bSearch(L, e, low, mid - 1)
    else:
        return bSearch(L, e, mid + 1, high)

def binarySearch(L, e):
    """Recursive binary search
    Assumes L is a list, the elements of which are in ascending order.
    Returns True if e is in L and False otherwise"""
    if len(L) == 0:
        return False
    else:
        return bSearch(L, e, 0, len(L) - 1)
    

def linearSearch(L, e):
    """Assumes L is a list.
    Returns True if e is in L and False otherwise"""
    for i in range(len(L)):
        if L[i]==e:
            return True
    return False

def simpleCheck(L, e):
    """
    Simple check using *in* operator of Python
    """
    return e in L

if __name__ == '__main__':
    #generate random 25 NUMBERS as list
    NUMBERS = [random.randint(-10, 10) for x in range(25)]
    print sorted(NUMBERS)
    for x in range(-10,11):
        print x, simpleCheck(NUMBERS, x), linearSearch(NUMBERS, x), binarySearch(sorted(NUMBERS), x)
