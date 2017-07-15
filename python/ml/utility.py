import numpy
import csv
import random

def euclidean(A, B):
    return numpy.sqrt(numpy.sum((numpy.asarray(A) - numpy.asarray(B))**2))

def load_dataset(filename):
    with open(filename, 'rb') as csvfile:
        # all values without quotes are considered numeric
        lines = csv.reader(csvfile,quoting=csv.QUOTE_NONNUMERIC)
        return list(lines)

def load_numbers(filename, delimiter=","):
    return numpy.genfromtxt(filename, delimiter=delimiter)

def split_dataset(dataset, splitFactor):
    trainingSet = []
    testSet = []
    for x in range(len(dataset)-1):
        if random.random() < splitFactor:
            trainingSet.append(dataset[x])
        else:
            testSet.append(dataset[x])
    return trainingSet, testSet
