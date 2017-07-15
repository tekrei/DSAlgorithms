#!/usr/bin/python
# coding=utf-8
import sys
import operator
from sklearn.metrics import *
import matplotlib.pyplot as plot
import numpy
import itertools
from sklearn.preprocessing import label_binarize

from utility import *

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
- banknote: nothing changed, converted to CSV (https://archive.ics.uci.edu/ml/datasets/banknote+authentication)

The main source for the code is the following tutorial: Source: http://machinelearningmastery.com/tutorial-to-implement-k-nearest-neighbors-in-python-from-scratch/
'''
def get_neighbors(training, test, k):
    distances = []
    for x in range(len(training)):
        #without target
        dist = euclidean(test[0:-1], training[x][0:-1])
        distances.append((training[x], dist))
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])
    return neighbors

def get_response(neighbors):
    class_votes = {}
    for x in range(len(neighbors)):
        response = neighbors[x][-1]
        if response in class_votes: class_votes[response] += 1
        else: class_votes[response] = 1
    sorted_votes = sorted(class_votes.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sorted_votes[0][0]

def plot_confusion_matrix(cm, classes, normalize=False, title='Confusion matrix', cmap=plot.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    Source: http://scikit-learn.org/stable/auto_examples/model_selection/plot_confusion_matrix.html
    """
    plot.imshow(cm, interpolation='nearest', cmap=cmap)
    plot.title(title)
    plot.colorbar()
    tick_marks = numpy.arange(len(classes))
    plot.xticks(tick_marks, classes, rotation=45)
    plot.yticks(tick_marks, classes)

    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, numpy.newaxis]

    thresh = cm.max() / 2.0
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plot.text(j, i, cm[i, j], horizontalalignment="center", color="white" if cm[i, j] > thresh else "black")

    plot.tight_layout()
    plot.ylabel('True label')
    plot.xlabel('Predicted label')

def main():
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
    # load data
    dataSet = load_dataset(file_name)
    training, test = split_dataset(dataSet, split)
    print 'Train set: ' + repr(len(training))
    print 'Test set: ' + repr(len(test))
    # generate predictions
    predictions=[]
    actual = []
    for x in range(len(test)):
        neighbors = get_neighbors(training, test[x], k)
        result = get_response(neighbors)
        predictions.append(result)
        actual.append(test[x][-1])
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
    print("ROC AUC Score:"+repr(roc_auc_score(label_binarize(actual, class_names), label_binarize(predictions, class_names),average='weighted')))
    # generate confusion matrix
    # plot non-normalized confusion matrix
    plot.figure()
    plot_confusion_matrix(confusion_matrix(actual,predictions), class_names)
    plot.show()
main()
