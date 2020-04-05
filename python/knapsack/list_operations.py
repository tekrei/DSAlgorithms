'''
Created on May 16, 2015

@author: tekrei

Chapter 9 codes from Introduction to Computation and Programming Using Python 
'''


def is_subset(L1: list, L2: list):
    for e1 in L1:
        matched = False
        for e2 in L2:
            if e1 == e2:
                matched = True
                break
        if not matched:
            return False
    return True


def intersection(L1: list, L2: list):
    tmp = []
    for e1 in L1:
        for e2 in L2:
            if e1 == e2:
                tmp.append(e1)
    # build without duplicates
    res = []
    for e in tmp:
        if not(e in res):
            res.append(e)
    return res


def get_binary_rep(n, digit_count):
    result = ''
    while n > 0:
        result = str(n % 2) + result
        n = n // 2
    if len(result) > digit_count:
        raise ValueError('not enough digits')
    for _ in range(digit_count - len(result)):
        result = '0' + result
    return result


def gen_power_set(L: list):
    power_set = []
    for i in range(0, 2 ** len(L)):
        binary_str = get_binary_rep(i, len(L))
        subset = []
        for j in range(len(binary_str)):
            if binary_str[j] == '1':
                subset.append(L[j])
        power_set.append(subset)
    return power_set


if __name__ == '__main__':
    pass
