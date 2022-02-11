"""
Created on May 13, 2015

Algorithm examples from Introduction to Algorithms (3rd) book
"""
import random


def max_subarray(A: list):
    """
    Variation of Kadane's algorithm
    Dynamic programming solution
    returns only the sum of the subarray
    """
    max_ending_here = max_so_far = A[0]
    for x in A[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far


def maximum_subarray(data: list):
    """
    Dynamic programming solution for maximum subarray problem
    returns start and end index together with sum of the maximum subarray
    """
    new_sum = []
    new_sum.append(data[0])
    current_max = data[0]
    begin = 0
    end = 0

    for i in range(1, len(data)):
        new_begin = begin
        new_end = end

        if data[i] > (new_sum[i - 1] + data[i]):
            new_sum.append(data[i])
            new_begin = i
            new_end = i
        else:
            new_sum.append(new_sum[i - 1] + data[i])
            new_end = i

        if new_sum[i] > current_max:
            current_max = new_sum[i]
            begin = new_begin
            end = new_end

    return begin, end, current_max


if __name__ == "__main__":
    numbers = [random.randint(-10, 10) for x in range(10)]
    print("%s %s %s" % (numbers, maximum_subarray(numbers), max_subarray(numbers)))
    n2 = [0, -6, 4, -2, 4, -3, -10, 5, -4, 6]
    print("%s %s %s" % (n2, maximum_subarray(n2), max_subarray(n2)))
    n3 = [-4, -6, -4, -2, -4, -3, -10, -5, -4, -6]
    print("%s %s %s" % (n3, maximum_subarray(n3), max_subarray(n3)))
    n4 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    print("%s %s %s" % (n4, maximum_subarray(n4), max_subarray(n4)))
