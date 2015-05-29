'''
Created on May 13, 2015

@author: tekrei
'''

import random, timeit
import numpy as np
from operator import mul

def square_matrix_multiplication(matrix1, matrix2):
    '''
    Usual matrix multiplication with O(n^3) complexity
    '''
    result = np.zeros(matrix1.shape)
    count = matrix1.shape[1]
    for i in range(count):
        for j in range(count):
            for k in range(count):
                result[i, j] = result[i, j] + (matrix1[i, k] * matrix2[k, j])
    return result

if __name__ == '__main__':
    '''
    main method for matrix operations
    '''
    matrix1 = np.matrix([[random.randint(-10, 10) for x in range(5)] for y in range(5)])
    matrix2 = np.matrix([[random.randint(-10, 10) for x in range(5)] for y in range(5)])
    print matrix1, matrix2
    START_TIME = timeit.default_timer()
    print square_matrix_multiplication(matrix1, matrix2)
    print(timeit.default_timer() - START_TIME)
    START_TIME = timeit.default_timer()
    #using python mul operator
    print mul(matrix1, matrix2)
    print(timeit.default_timer() - START_TIME)
    START_TIME = timeit.default_timer()
    # NumPy uses a highly-optimized, carefully-tuned BLAS method for matrix multiplication
    print np.dot(matrix1, matrix2)
    print(timeit.default_timer() - START_TIME)
