'''
Created on May 16, 2015

@author: tekrei
Greedy solution to Knapsack problem
Source: Introduction to Computation and Programming Using Python
'''
from Item import buildItems, weightInverse, value, density

def greedy(items, maxWeight, keyFcn):
    assert type(items) == list and maxWeight >= 0
    itemsCopy = sorted(items, key = keyFcn, reverse = True)
    result = []
    totalVal = 0.0
    totalWeight = 0.0
    i = 0
    while totalWeight<maxWeight and i < len(items):
        if (totalWeight + itemsCopy[i].getWeight()) <= maxWeight:
            result.append(itemsCopy[i])
            totalWeight += itemsCopy[i].getWeight()
            totalVal += itemsCopy[i].getValue()
        i+=1
    return (result, totalVal)

def testGreedy(items, constraint, getKey):
    taken, val = greedy(items, constraint, getKey)
    print 'Total value of items taken = ' + str(val)
    for item in taken:
        print '\t', item

def testGreedys(maxWeight=20):
    items = buildItems()
    print 'Use greedy by value for knapsack of size maxWeight'
    testGreedy(items, maxWeight, value)
    print 'Use greedy by weight for knapsack of size maxWeight'
    testGreedy(items, maxWeight, weightInverse)
    print 'Use greedy by density for knapsack of size maxWeight'
    testGreedy(items, maxWeight, density)
    

if __name__ == '__main__':
    testGreedys()
