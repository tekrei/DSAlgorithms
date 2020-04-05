"""
Created on May 16, 2015

@author: tekrei
Greedy solution to Knapsack problem
Source: Introduction to Computation and Programming Using Python
"""
from item import build_items, weight_inverse, value, density


def greedy(items: list, max_weight: float, key_func: callable):
    assert type(items) == list and max_weight >= 0
    items_copy = sorted(items, key=key_func, reverse=True)
    result = []
    totalVal = 0.0
    total_weight = 0.0
    i = 0
    while total_weight < max_weight and i < len(items):
        if (total_weight + items_copy[i].getWeight()) <= max_weight:
            result.append(items_copy[i])
            total_weight += items_copy[i].getWeight()
            totalVal += items_copy[i].getValue()
        i += 1
    return (result, totalVal)


def test_greedy(items: list, constraint: float, get_key: callable):
    taken, val = greedy(items, constraint, get_key)
    print("Total value of items taken = %s" % val)
    for item in taken:
        print("\t % s" % item)


def test_greedys(max_constraint: float = 20):
    items = build_items()
    print("Use greedy by value for knapsack of size %s" % max_constraint)
    test_greedy(items, max_constraint, value)
    print("Use greedy by weight for knapsack of size %s" % max_constraint)
    test_greedy(items, max_constraint, weight_inverse)
    print("Use greedy by density for knapsack of size %s" % max_constraint)
    test_greedy(items, max_constraint, density)


if __name__ == "__main__":
    test_greedys()
