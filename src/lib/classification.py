from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, ConfusionMatrixDisplay, RocCurveDisplay

import pandas as pd
from numpy import ravel
import matplotlib.pyplot as plt

from principal_component_analysis import PCA_extract

def chooseMostAccurateClassificator(X, labels, classifiers):

	best_model = {}
	best_score = 0

	training_data, testing_data, training_labels, testing_labels = train_test_split(
		X,
		labels,
	)

	isMulticlass = len(pd.value_counts(labels)) > 2 

	#For each classifier, a model is created and tested
	for k, v in classifiers.items():
		
		model = v.fit(
			training_data,
			ravel(training_labels)
		)

		predicted_labels = model.predict(testing_data)

		score = accuracy_score(ravel(testing_labels), predicted_labels)

		print("  ", k, score)

		if score > best_score:
			best_model = model
			best_score = score

		ConfusionMatrixDisplay.from_predictions(ravel(testing_labels), predicted_labels, normalize = "true")
		plt.show()

		if not isMulticlass:
			RocCurveDisplay.from_predictions(ravel(testing_labels), predicted_labels)
			plt.show()

		return best_model, best_score

# Extracting data

data = pd.read_csv('./../assets/UNSW-NB15-preprocessed.csv',low_memory=False)
data.info()

X, labels, classes = data.iloc[:, 1:30], data.iloc[:, 32], data.iloc[:, 31]

classifiers={
	"randomforest" : RandomForestClassifier(),
}

print("Binary classifier")

chooseMostAccurateClassificator(X, labels, classifiers=classifiers)

# removing non attacks
X = X[labels != 0]
classes = classes[labels != 0]

print("Multiclass classifier")
chooseMostAccurateClassificator(X, classes, classifiers=classifiers)

# PCA

X, labels, classes, components = PCA_extract(data, verbose=True)	

print("Binary classifier")
chooseMostAccurateClassificator(X, labels, classifiers=classifiers)

# removing non attacks
X = X[labels != 0]
classes = classes[labels != 0]

print("Multiclass classifier")
chooseMostAccurateClassificator(X, classes, classifiers=classifiers)
