import random
import numpy as np


#################################################

"""Chooses N random elements if you are already given the array a of items"""
def random_element(a, N):
        return a[int(random.random() * N)]

"""The N-th element of the iterator has a 1/N of being kept."""
def random_element_iterator(iterator):
    N = 0
    for item in iterator:
        N += 1
        #Determine if 1/N chance succeeds
        if random.random() * N < 1:
            element = item
    return element

"""Retrieve k random numbers from an array of undetermined size,
also known as reservoir sampling"""
def random_subset(iterator, k):
    result = []
    N = 0
    for item in iterator:
        N += 1
        if len( result ) < k:
            result.append( item )
        else:
            s = int(random.random() * N)
            if s < k:
                result[s] = item

    return result

#######################################################################    

"""Lloyd's algorithm (K-means clustering) in 2 steps. 

1) Using the available K centroids, clusters are updated such that 
they hold the oints closest in distance to each centroid.
2) Given the set of clusters, the centroids are 
recalculated as the mean of all points in a cluster.

At the end, all points within a cluster are closer to
their centroid than they are to any other centroid.

Input: dataset X of N points, we want to specify K clusters. 
Output: set of K centroids mu and a labeling of X that
assigns each of the points in X to a unique cluster.

Note: This may return a local minimum, but we can run
this code a few times and average the result"""


def make_board(N):
    #Initializes a configuration of points    
    X = np.array([(random.uniform(-1, 1), random.uniform(-1, 1)) for i in range(N)])
    return X


def cluster_points(X, mu): #step 1
    clusters  = {}
    for x in X:
        bestmukey = min([(i[0], np.linalg.norm(x-mu[i[0]])) \
                    for i in enumerate(mu)], key=lambda t:t[1])[0]
        #norm gives a positive size to a vector/matrix
        try:
            clusters[bestmukey].append(x)
        except KeyError:
            clusters[bestmukey] = [x]
    return clusters
 
def reevaluate_centers(mu, clusters): #step 2
    newmu = []
    keys = sorted(clusters.keys())
    for key in keys:
        newmu.append(np.mean(clusters[key], axis = 0)) #axis of 0 means we round to 1 significant digit
    return newmu
 
def has_converged(mu, oldmu): #Repeat until the cluster and centroid assignmets do not change
    return (set([tuple(a) for a in mu]) == set([tuple(a) for a in oldmu])
 
def find_centers(X, K): #Main function, uses steps 1 & 2 and the convergence check
    # Initialize to K random centers
    oldmu = random.sample(X, K)
    mu = random.sample(X, K)
    while not has_converged(mu, oldmu):
        oldmu = mu
        # Assign all points in X to clusters
        clusters = cluster_points(X, mu)
        # Reevaluate centers
        mu = reevaluate_centers(oldmu, clusters)
    return(mu, clusters)

