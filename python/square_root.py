'''
Created on May 13, 2015

Various square root approximations
Source: Introduction to Computation and Programming Using Python book
'''
import time


def newton_raphson(y):
    '''
    Newton-Raphson for square root
    '''
    epsilon = 0.01
    ans = y / 2.0
    guess_count = 0
    while abs(ans * ans - y) >= epsilon:
        guess_count += 1
        ans = ans - (((ans ** 2) - y) / (2 * ans))
    return ans, guess_count


def exhaustive_enumeration(x):
    '''
    Approximating the square root using exhaustive enumeration
    '''
    epsilon = 0.01
    step = epsilon ** 2
    guess_count = 0
    ans = 0.0
    while abs(ans ** 2 - x) >= epsilon and ans <= x:
        ans += step
        guess_count += 1
    if abs(ans ** 2 - x) >= epsilon:
        print("failed on square root of %s" % x)
    else:
        print("%s is close to square root of %s" % (ans, x))
    return ans, guess_count


def bisection(x):
    '''
    Bisection search to approximate square root
    '''
    epsilon = 0.01
    guess_count = 0
    low = 0.0
    high = max(1.0, x)
    ans = (high + low) / 2.0
    while abs(ans ** 2 - x) >= epsilon:
        # print 'low =', low, 'high =', high, 'ans =', ans
        guess_count += 1
        if ans ** 2 < x:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2.0
    return ans, guess_count


if __name__ == '__main__':
    numbers = [4, 9, 16, 25, 81, 144, 256, 262144]
    for x in numbers:
        print("-------%d------" % x)

        start_time = time.time()
        print("Exhaustive enumeration %s (%fs)" %
              (str(exhaustive_enumeration(x)), time.time() - start_time))

        start_time = time.time()
        print("Bisection %s (%fs)" %
              (str(bisection(x)), time.time() - start_time))

        start_time = time.time()
        print("Newton Raphson %s (%fs)" %
              (str(newton_raphson(x)), time.time() - start_time))
