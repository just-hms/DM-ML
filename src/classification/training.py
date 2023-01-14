import pickle

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, ConfusionMatrixDisplay, RocCurveDisplay

import pandas as pd
from numpy import ravel
import matplotlib.pyplot as plt

from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

def chooseMostAccurateModel(X, labels, classifiers, n_rounds=20, plot=False):

	best_model_name = ""
	best_model = {}
	best_score = 0

	training_data, testing_data, training_labels, testing_labels = train_test_split(
		X,
		labels,
	)

	isMulticlass = len(pd.value_counts(labels)) > 2 

	#For each classifier, a model is created and tested
	for k, value in classifiers.items():
		
		model = value.fit(
			training_data,
			ravel(training_labels)
		)

		predicted_labels = model.predict(testing_data)

		score = accuracy_score(ravel(testing_labels), predicted_labels)

		print('  ', k, score)

		if score > best_score:
			best_model_name = k
			best_model = model
			best_score = score

		if plot:
			ConfusionMatrixDisplay.from_predictions(ravel(testing_labels), predicted_labels, normalize = 'true')
			plt.show()

			if not isMulticlass:
				RocCurveDisplay.from_predictions(ravel(testing_labels), predicted_labels)
				plt.show()

	print('chosen model: ', best_model_name)

	for i in range(1, n_rounds):
		
		training_data, testing_data, training_labels, testing_labels = train_test_split(
			X,
			labels,
		)
		
		model = classifiers[best_model_name].fit(
			training_data,
			ravel(training_labels)
		)

		predicted_labels = model.predict(testing_data)

		score = accuracy_score(ravel(testing_labels), predicted_labels)

		print(i, 'score:', score)
		
		if score > best_score:
			best_model = model
			best_score = score

	print('best score: ', best_score)

	return best_model, best_score

# Extracting data

assets_folder = './../../assets/'
models_folder = assets_folder + 'models/'


data = pd.read_csv(assets_folder + 'UNSW-NB15-preprocessed.csv',low_memory=False)
data.info()

X, labels, classes = data.iloc[:, 1:30], data.iloc[:, 32], data.iloc[:, 31]

# return only the  
classes_attacks = classes[labels != 0]

classifiers = {
	'randomforest' : RandomForestClassifier(),
	'logisticregression': LogisticRegression(),
    'kneighbors': KNeighborsClassifier(),
    'mlp': MLPClassifier(),
	
}

print('\nBinary classifier')

model, _ = chooseMostAccurateModel(X, labels, classifiers=classifiers)
pickle.dump(model, open(models_folder + 'binary_model', 'wb'))

print('\nMulticlass classifier')

X_attacks = X[labels != 0]

model, _ = chooseMostAccurateModel(X_attacks, classes_attacks, classifiers=classifiers)
pickle.dump(model, open(models_folder + 'multiclass_model', 'wb'))

