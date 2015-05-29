'''
Created on May 13, 2015

@author: tekrei

Various square root approximations
Source: Introduction to Computation and Programming Using Python book
'''

def newton_raphson(y):
    '''
    Newton-Raphson for square root
    '''
    epsilon = 0.01
    ans = y / 2.0
    numGuesses = 0
    while abs(ans * ans - y) >= epsilon:
        numGuesses += 1
        ans = ans - (((ans ** 2) - y) / (2 * ans))
    return ans, numGuesses

def exhaustive_enumeration(x):
    '''
    Approximating the square root using exhaustive enumeration
    '''
    epsilon = 0.01
    step = epsilon ** 2
    numGuesses = 0
    ans = 0.0
    while abs(ans ** 2 - x) >= epsilon and ans <= x:
        ans += step
        numGuesses += 1
    if abs(ans ** 2 - x) >= epsilon:
        print 'Failed on square root of', x
    else:
        print ans, 'is close to square root of', x
    return ans, numGuesses

def bisection(x):
    '''
    Bisection search to approximate square root
    '''
    epsilon = 0.01
    numGuesses = 0
    low = 0.0
    high = max(1.0, x)
    ans = (high + low) / 2.0
    while abs(ans ** 2 - x) >= epsilon:
        # print 'low =', low, 'high =', high, 'ans =', ans
        numGuesses += 1
        if ans ** 2 < x:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2.0
    return ans, numGuesses

if __name__ == '__main__':
    x = 144
    print exhaustive_enumeration(x)
    print bisection(x)
    print newton_raphson(x)
