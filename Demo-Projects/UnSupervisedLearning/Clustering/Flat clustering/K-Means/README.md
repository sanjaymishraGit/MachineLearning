# K-Means algorithm - simple example
The idea of K-Means is to attempt to cluster a given dataset into K clusters, The process goes as following:

1. Take entire dataset, and set, randomly, K number of centroids. Centroids are just the "centers" of  clusters. 
2. Calculate distance of each featureset to the centroids, and classify each featureset as the centroid class closest to it. Centroid classes are arbitrary.
3) Once we  have classified all data, now we  take the "mean" of the groups, and set the new centroids as the mean of their associated groups.

Repeat #2 and #3 until we are optimized. Typically, you measure optimization by movement of the centroid. There are many ways to do this, we're just going to use percent change.


