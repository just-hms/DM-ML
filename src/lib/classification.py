from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import Perceptron
from sklearn.model_selection import train_test_split

from sklearn.metrics import accuracy_score, ConfusionMatrixDisplay, RocCurveDisplay
from pandas import read_csv
from numpy import ravel
import matplotlib.pyplot as plt
from sklearn.naive_bayes import CategoricalNB, GaussianNB
from sklearn.neural_network import MLPClassifier

from src.principal_component_analysis import PCA_extract

from src.constants import *

# Extracting data

data = read_csv('./preprocessing/UNSW-NB15-preprocessed.csv',low_memory=False)

data.info()

X, labels, classes = data.iloc[:, 1:30], data.iloc[:, 32], data.iloc[:, 31]
# X, labels, classes, components = PCA_extract(data, verbose=True)

# Binary classification

#Creation of the training set

training_data, testing_data, training_labels, testing_labels = train_test_split(
	X,
	labels,
)

print("Binary classifier: ")

#Multiple types of classifier are tested
classifiers = {
	"randomforest" : RandomForestClassifier(),
}

#For each classifier, a model is created and tested
for k, v in classifiers.items():
	
	model = v.fit(
		training_data,
		ravel(training_labels)
	)

	predicted_labels = model.predict(testing_data)

	score = accuracy_score(ravel(testing_labels), predicted_labels)

	print(k, score)

	print("Confusion matrix")
	#disp = ConfusionMatrixDisplay(confusion_matrix(ravel(testing_labels), predicted_labels, normalize = "all"))
	ConfusionMatrixDisplay.from_predictions(ravel(testing_labels), predicted_labels, normalize = "true")
	plt.show()

	print("ROC curve")
	RocCurveDisplay.from_predictions(ravel(testing_labels), predicted_labels)
	plt.show()
	
 
# Multiclass classification

print("Multiclass classifier")

# Creation of the training set
X = X[labels != 0]
classes = classes[labels != 0]

training_data, testing_data, training_labels, testing_labels = train_test_split(
	X, 
	classes,
)

#Multiple types of classifier are tested

classifiers = {
	"randomforest" : RandomForestClassifier(),
}

for k, v in classifiers.items():
	model = v.fit(
		training_data,
		ravel(training_labels)
	)

	predicted_labels = model.predict(testing_data)
	score = accuracy_score(ravel(testing_labels), predicted_labels)

	print(k, score)

	print("Confusion matrix:")
	#disp = ConfusionMatrixDisplay(confusion_matrix(ravel(testing_labels), predicted_labels, normalize = "all"), display_labels = ravel(testing_labels))
	ConfusionMatrixDisplay.from_predictions(ravel(testing_labels), predicted_labels, normalize = "true")
	plt.show()












