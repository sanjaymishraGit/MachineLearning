# Speed dating Classifier  
This classification uses data set from https://www.kaggle.com/annavictoria/speed-dating-experiment and predicts the results of
match.
This is the nice example which covers 3 steps of  data analysis:
1) Cleaning the data
2) Normalization of data: uses StandardScaler
3) Reduction of feature set: uses PCA ( reduced feature set from 101 to 80)

This is also a nice demonstration of the concept of Feature Architecting. in DNN selection of feature is not so important but 
"Feature Architecting is the one which is important"

This uses DNNClassifier using tf.contrib
TF Accuracy:  0.998210023866
