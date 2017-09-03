from sklearn import tree
from sklearn.naive_bayes import GaussianNB
from sklearn import svm
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score

# [height, weight, shoe_size]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.4, random_state=0)

#Decision Tree Classifier
decesionTreeClassifier = tree.DecisionTreeClassifier()
decesionTreeClassifier = decesionTreeClassifier.fit(X_train,Y_train)
decesionTreeClassifierScore =  decesionTreeClassifier.score(X_test,Y_test)
print("DecisionTreeClassifier score after traning the model is: ", decesionTreeClassifierScore)
decesionTreeClassifierPrediction = decesionTreeClassifier.predict([[181, 80, 43]])
print("Result of Prediction from DecisionTreeClassifier is:",decesionTreeClassifierPrediction)

maximumScore = decesionTreeClassifierScore
betterPredictionValue = decesionTreeClassifierPrediction
goodClassifierAlgoName= "DecisionTreeClassifier"



# Naive bayes 
naiveBayes = GaussianNB()
naiveBayes = naiveBayes.fit(X_train,Y_train)
naiveBayesScore = naiveBayes.score(X_test,Y_test)
print("Naive Bayes score ater traning the model is: ", naiveBayesScore)
naiveBayesPrediction =  naiveBayes.predict([[181, 80, 43]])
print("Result of Prediction from NaiveBayes is:",naiveBayesPrediction)

if(naiveBayesScore > maximumScore):
		maximumScore = naiveBayesScore
		betterPredictionValue = naiveBayesPrediction
		goodClassifierAlgoName= "Naive Bayes"
	


# Support Vector Machine
supportVectorMachine = svm.SVC()
supportVectorMachine = supportVectorMachine.fit(X_train,Y_train)
supportVectorMachineScore = supportVectorMachine.score(X_test,Y_test)
print("Support Vector Machine score after traning the model is: ", supportVectorMachineScore)
supportVectorMachinePrediction = supportVectorMachine.predict([[181, 80, 43]])
print("Result of Prediction from Support Vector Machine  is: ",supportVectorMachinePrediction)

if(supportVectorMachineScore>maximumScore):
		maximumScore = supportVectorMachineScore
		betterPredictionValue = supportVectorMachinePrediction
		goodClassifierAlgoName= "Support Vector Machine-SVM"


# Nu-Support Vector Machine
nuSupportVectorMachine = svm.NuSVC()
nuSupportVectorMachine = nuSupportVectorMachine.fit(X_train,Y_train)
nuSupportVectorMachineScore = nuSupportVectorMachine.score(X_test,Y_test)
print("Nu-Support Vector Machine score after traning the model is: ", nuSupportVectorMachineScore)
nusupportVectorMachinePrediction = nuSupportVectorMachine.predict([[181, 80, 43]])
print("Result of Prediction from Nu-Support Vector Machine  is: ",nusupportVectorMachinePrediction)

if(nuSupportVectorMachineScore>maximumScore):
		maximumScore = nuSupportVectorMachineScore
		betterPredictionValue = nusupportVectorMachinePrediction
		goodClassifierAlgoName= "Support Vector Machine-nu-SVM"



print("Among all one of the good performed Classifier algorithm is: ", goodClassifierAlgoName, "Prediction value is: ", betterPredictionValue , "Maximum score is: ",maximumScore)
