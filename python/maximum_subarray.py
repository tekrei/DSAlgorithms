'''
Created on May 13, 2015

@author: tekrei

Algorithm examples from Introduction to Algorithms (3rd) book
'''
import random

def max_subarray(A):
    '''
    Variation of Kadane's algorithm
    Dynamic programming solution
    returns only the sum of the subarray
    '''
    max_ending_here = max_so_far = A[0]
    for x in A[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far
        
def maximum_subarray(data):
    '''
    Dynamic programming solution for maximum subarray problem
    returns start and end index together with sum of the maximum subarray 
    '''
    newsum = []
    newsum.append(data[0])
    currentMax = data[0]
    begin = 0
    end = 0
    
    for i in range(1, len(data)):
        newBegin = begin        
        newEnd = end
        
        if data[i] > (newsum[i - 1] + data[i]):
            newsum.append(data[i])
            newBegin = i
            newEnd = i
        else:
            newsum.append(newsum[i - 1] + data[i])
            newEnd = i
        
        if newsum > currentMax:
            currentMax = newsum[i]
            begin = newBegin
            end = newEnd
            
    return begin, end, currentMax
    

if __name__ == '__main__':
    NUMBERS = [random.randint(-10, 10) for x in range(10)]
    print NUMBERS, maximum_subarray(NUMBERS), max_subarray(NUMBERS)
    n2 = [0, -6, 4, -2, 4, -3, -10, 5, -4, 6]
    print n2, maximum_subarray(n2), max_subarray(n2)
    n3 = [-4, -6, -4, -2, -4, -3, -10, -5, -4, -6]
    print n3, maximum_subarray(n3), max_subarray(n3)
    n4 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    print n4, maximum_subarray(n4), max_subarray(n4)
    
