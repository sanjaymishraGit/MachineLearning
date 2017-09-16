# Mean Shift -  Example 

Mean Shift is very similar to the K-Means algorithm, except for one very important factor: you do not need to specify the number of groups prior to training. The Mean Shift algorithm finds clusters on its own.

The way Mean Shift works is to go through each featureset (a datapoint on a graph), and proceed to do a hill climb operation. Hill Climbing is just as it sounds: The idea is to continually increase, or go up, until you cannot anymore. We don't have for sure just one local maximal value. We might have only one, or we might have ten. Our "hill" in this case will be the number of featuresets/datapoints within a given radius. The radius is also called a bandwidth. We do this starting from each data point. Many data points will lead to the same cluster center, which should be expected, but it is also possible that other data points will take you to a completely separate cluster center.

