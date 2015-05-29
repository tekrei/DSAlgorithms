'''
Created on May 16, 2015

@author: tekrei

Chapter 9 codes from Introduction to Computation and Programming Using Python 
'''

def isSubset(L1, L2):
    for e1 in L1:
        matched = False
        for e2 in L2:
            if e1 == e2:
                matched = True
                break
        if not matched:
            return False
    return True

def intersection(L1, L2):
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

def getBinaryRep(n, numDigits):
    result = ''
    while n > 0:
        result = str(n % 2) + result
        n = n // 2
    if len(result) > numDigits:
        raise ValueError('not enough digits')
    for i in range(numDigits - len(result)):
        result = '0' + result
    return result

def genPowerSet(L):
    powerSet = []
    for i in range(0, 2 ** len(L)):
        binStr = getBinaryRep(i, len(L))
        subset = []
        for j in range(len(binStr)):
            if binStr[j] == '1':
                subset.append(L[j])
        powerSet.append(subset)
    return powerSet

if __name__ == '__main__':
    pass
