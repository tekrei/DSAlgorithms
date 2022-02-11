"""
Created on May 16, 2015

Greedy solution to 0/1 Knapsack problem
Source: Introduction to Computation and Programming Using Python
"""
from item import build_items, Item
from list_operations import gen_power_set


def choose_best(
    pset: set, constraint: float, get_value: callable, get_weight: callable
):
    best_value = 0.0
    best_set = None
    for items in pset:
        items_value = 0.0
        items_weight = 0.0
        for item in items:
            items_value += get_value(item)
            items_weight += get_weight(item)
        if items_weight <= constraint and items_value > best_value:
            best_value = items_value
            best_set = items
    return (best_set, best_value)


def test_best(max_constraint: float = 20):
    items = build_items()
    pset = gen_power_set(items)
    taken, val = choose_best(pset, max_constraint, Item.getValue, Item.getWeight)
    print("Total value of items taken = %s " % val)
    for item in taken:
        print("\t%s" % item)


if __name__ == "__main__":
    test_best()
