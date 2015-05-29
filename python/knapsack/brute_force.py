'''
Created on May 16, 2015

@author: tekrei
Greedy solution to 0/1 Knapsack problem
Source: Introduction to Computation and Programming Using Python
'''
from Item import buildItems, Item
from list_operations import genPowerSet

def chooseBest(pset,constraint,getVal,getWeight):
    bestVal = 0.0
    bestSet = None
    for items in pset:
        itemsVal = 0.0
        itemsWeight = 0.0
        for item in items:
            itemsVal += getVal(item)
            itemsWeight += getWeight(item)
        if itemsWeight<=constraint and itemsVal> bestVal:
            bestVal = itemsVal
            bestSet = items
    return (bestSet, bestVal)


def testBest(maxWeight=20):
    items = buildItems()
    pset = genPowerSet(items)
    taken, val = chooseBest(pset, maxWeight, Item.getValue, Item.getWeight)
    print 'Total value of items taken = ' + str(val)
    for item in taken:
        print '\t', item    

if __name__ == '__main__':
    testBest()
