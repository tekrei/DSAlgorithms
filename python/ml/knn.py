import sys
import csv
import random
import math
import operator
from sklearn.metrics import *
import matplotlib.pyplot as plt
import numpy as np
import itertools
from sklearn.preprocessing import label_binarize
from sklearn.neighbors import NearestNeighbors


'''
k-Nearest Neighbors implementation

It doesn't use any library to perform KNN. 
It use scikit-learn library for calculating various metrics and confusion matrix.

It is possible to provide file name, k value and training-test data split ratio as arguments such as the following:
        python knn.py data/iris.csv 5 0.67

It is tested with the following example data sets:
- iris: string field (result) are enclosed in quotes (https://archive.ics.uci.edu/ml/datasets/Iris)
- forest fires: categorical values (mon, day) are converted to numeric values, all values larger than 0 are converted to 1 in burned area column (https://archive.ics.uci.edu/ml/datasets/Forest+Fires)
- lung cancer: moved target values to the last column, missed values replaced by -1 (https://archive.ics.uci.edu/ml/datasets/Lung+Cancer)
- phishing_websites: nothing changed, converted to CSV without header (https://archive.ics.uci.edu/ml/datasets/Phishing+Websites)
- arrhythmia: missed values replaced by -1 (https://archive.ics.uci.edu/ml/datasets/Arrhythmia)

The main source for the code is the following tutorial: Source: http://machinelearningmastery.com/tutorial-to-implement-k-nearest-neighbors-in-python-from-scratch/
'''
def loadDataset(filename, split, trainingSet=[] , testSet=[]):
    with open(filename, 'rb') as csvfile:
        # all values without quotes are considered numeric
        lines = csv.reader(csvfile,quoting=csv.QUOTE_NONNUMERIC)
        dataset = list(lines)
        for x in range(len(dataset)-1):
            if random.random() < split:
                trainingSet.append(dataset[x])
            else:
                testSet.append(dataset[x])

def euclideanDistance(instance1, instance2, length):
    distance = 0
    for x in range(length):
        distance += pow((instance1[x] - instance2[x]), 2)
    return math.sqrt(distance)

def getNeighbors(trainingSet, testInstance, k):
	distances = []
	length = len(testInstance)-1
	for x in range(len(trainingSet)):
		dist = euclideanDistance(testInstance, trainingSet[x], length)
		distances.append((trainingSet[x], dist))
	distances.sort(key=operator.itemgetter(1))
	neighbors = []
	for x in range(k):
		neighbors.append(distances[x][0])
	return neighbors

def getResponse(neighbors):
    classVotes = {}
    for x in range(len(neighbors)):
        response = neighbors[x][-1]
        if response in classVotes:
            classVotes[response] += 1
        else:
            classVotes[response] = 1
    sortedVotes = sorted(classVotes.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedVotes[0][0]

def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    Source: http://scikit-learn.org/stable/auto_examples/model_selection/plot_confusion_matrix.html
    """
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]

    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, cm[i, j],
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')

def main():
    # prepare data
    trainingSet=[]
    testSet=[]
    argc = len(sys.argv)
    file_name = 'data/iris.csv'
    k = 5
    split = 0.67
    if(argc==1):
        print "Info: You can provide file name and k value as an argument: python knn.py file_name k_value split_value"
    if(argc==2):
        #file is given
        file_name = sys.argv[1]
    if(argc==3):
        #file and k are given
        file_name = sys.argv[1]
        k = int(sys.argv[2])
    if(argc==4):
        #file, k and split are given
        file_name = sys.argv[1]
        k = int(sys.argv[2])
        split = float(sys.argv[3])
    loadDataset(file_name, split, trainingSet, testSet)
    print 'Train set: ' + repr(len(trainingSet))
    print 'Test set: ' + repr(len(testSet))
    # generate predictions
    predictions=[]
    actual = []
    for x in range(len(testSet)):
        neighbors = getNeighbors(trainingSet, testSet[x], k)
        result = getResponse(neighbors)
        predictions.append(result)
        actual.append(testSet[x][-1])
    # calculate and display various scores
    print('Accuracy: ' + repr(accuracy_score(actual, predictions)))
    precision = precision_score(actual, predictions,average='weighted')
    print('Precision: ' + repr(precision))
    recall = recall_score(actual, predictions,average='weighted')
    print('Recall: ' + repr(recall))
    print("F1 score (manual):"+repr(2*((precision*recall)/(precision+recall))))
    print("F1 score (scikit):"+repr(f1_score(actual, predictions, average='weighted')))
    class_names = list(set(actual))
    # use binarized values for AUC score calculation
    print("ROC AUC Score:"+repr(roc_auc_score(label_binarize(actual,class_names), label_binarize(predictions,class_names),average='weighted')))
    # generate confusion matrix
    cnf_matrix = confusion_matrix(actual,predictions)
    # plot non-normalized confusion matrix
    plt.figure()
    plot_confusion_matrix(cnf_matrix,class_names)
    plt.show()
main()
