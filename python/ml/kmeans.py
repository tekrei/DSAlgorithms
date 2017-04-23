"""
Created on May 24, 2013
Updated on Apr 23, 2017
@author: tekrei

http://stackoverflow.com/questions/1545606/python-k-means-algorithm
"""
from __future__ import division

import numpy
from random import sample
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans as SKLKMeans

class KMeans():

    def euclidean(self, A, B):
        return numpy.sqrt(numpy.sum((A - B)**2))

    def cost(self, data, clusters, memberships):
        squareSum = 0
        for i, datum in enumerate(data):
            squareSum += (self.euclidean(datum, clusters[memberships[i]]) ** 2)

        return (1 / data.shape[0]) * squareSum

    def cluster(self, data, clusterCount, iteration=1000):
        """
        K-Means algorithm
        """
        #select the clusters randomly from data
        dataCount = data.shape[0]
        clusters = numpy.array(sample(data, clusterCount))
        #assign random memberships to the data
        memberships = numpy.zeros(dataCount, dtype=numpy.int8)
        #flags for the stop criteria
        changed = False
        currentIteration = 0
        previousCost = 1e308
        #k-means loop starting
        while True:
            #reset new cluster variables
            newClusters = numpy.zeros((clusterCount, data.shape[1]))
            newClusterSize = numpy.zeros(clusterCount)

            #CLUSTER ASSIGNMENT STEP
            #assign each data to the nearest cluster
            for i, datum in enumerate(data):
                dmin = float('Inf')
                #find the smallest distance cluster center
                for j, cluster in enumerate(clusters):
                    distance = self.euclidean(datum, cluster)
                    if distance < dmin:
                        dmin = distance
                        n = j
                #assign closest cluster to the datum
                if memberships[i] != n:
                    memberships[i] = n
                    changed = True
                #store the sum of the all data belonging to the same cluster
                newClusters[memberships[i]] = newClusters[memberships[i]] + datum
                #store the data count of cluster
                newClusterSize[memberships[i]] += 1

            #UPDATE STEP
            #calculate new cluster centers using data cluster information
            for j in range(clusterCount):
                if newClusterSize[j] > 0:
                    clusters[j] = newClusters[j] / newClusterSize[j]

            #COST CALCULATION
            cost = self.cost(data, clusters, memberships)
            print "Iteration ",currentIteration," Cost:",cost
            if previousCost == cost:
                break
            else:
                previousCost = cost
            currentIteration += 1
            #check for stop criteria
            if currentIteration > iteration or changed is False:
                break
        # data cluster memberships and cluster centers are returned
        self.clusterCenters = clusters
        #calculate inertia
        inertia = 0
        for i, datum in enumerate(data):
            inertia += self.euclidean(datum, clusters[memberships[i]])
        print "inertia:",inertia
        return memberships

if __name__ == "__main__":
    # testing
    ae = KMeans()
    sampleData = numpy.random.rand(100,2)*10
    clusterResult = ae.cluster(sampleData, 2)
    sklKMeans = SKLKMeans(n_clusters=2)
    sklKMeans.fit(sampleData)
    print "scikit-learn inertia:",sklKMeans.inertia_
    #plot results
    f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
    ax1.scatter(sampleData[:,0],sampleData[:,1],c=clusterResult)
    ax1.plot(ae.clusterCenters[:,0],ae.clusterCenters[:,1], 'g^')
    ax1.set_title("K-Means code result")
    ax2.scatter(sampleData[:,0],sampleData[:,1],c=sklKMeans.labels_)
    ax2.plot(sklKMeans.cluster_centers_[:,0],sklKMeans.cluster_centers_[:,1], 'g^')
    ax2.set_title("scikit-learn K-Means result")
    plt.show()