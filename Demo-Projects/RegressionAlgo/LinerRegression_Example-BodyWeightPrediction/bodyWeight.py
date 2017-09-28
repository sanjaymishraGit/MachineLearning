import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split

#read data
dataframes = pd.read_csv('challenge_dataset.txt',names=['Brain','Body'])

"""
Brain        Body
3.385        44.500
0.480        15.500
"""
X_train, X_test, y_train, y_test = np.asarray(train_test_split(dataframes['Brain'], dataframes['Body'], test_size=0.1))
   


#train model on Data
body_reg= linear_model.LinearRegression()
body_reg.fit(X_train.values.reshape(-1,1),y_train.values.reshape(-1,1))

print('Score: ', body_reg.score(X_test.values.reshape(-1,1),  y_test.values.reshape(-1,1)))


#visualize results
plt.scatter(X_test,y_test)
plt.plot(X_test,body_reg.predict(X_test.values.reshape(-1,1)))
plt.show()
