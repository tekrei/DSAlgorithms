'''
Created on May 16, 2015
'''


class Item(object):
    '''
    Item class for knapsack problem
    '''

    def __init__(self, n, v, w):
        self.name = n
        self.value = float(v)
        self.weight = float(w)

    def getName(self):
        return self.name

    def getValue(self):
        return self.value

    def getWeight(self):
        return self.weight

    def __str__(self):
        return '<' + self.name + ', ' + str(self.value) + ', ' + str(self.weight) + '>'


def value(item):
    return item.getValue()


def weight_inverse(item):
    return 1.0 / item.getWeight()


def density(item):
    return item.getValue() / item.getWeight()


def build_items():
    '''
    build example items for test
    '''
    names = ['clock', 'painting', 'radio', 'vase', 'book', 'computer']
    vals = [175, 90, 20, 50, 10, 200]
    weights = [10, 9, 4, 2, 1, 20]
    items = []
    for i in range(len(vals)):
        items.append(Item(names[i], vals[i], weights[i]))
    return items
