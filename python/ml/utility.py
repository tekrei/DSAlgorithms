import numpy

def euclidean(A, B):
    return numpy.sqrt(numpy.sum((numpy.asarray(A) - numpy.asarray(B))**2))
