from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import Perceptron
from sklearn.model_selection import train_test_split

from sklearn.metrics import accuracy_score, confusion_matrix
from pandas import read_csv
from numpy import ravel
from sklearn.naive_bayes import CategoricalNB, GaussianNB
from sklearn.neural_network import MLPClassifier

import pandas as pd

from constants import *

def read_data(path:str, headers:list[str]):
	
	data = read_csv(
		path,
		low_memory=False,
		names = headers
	)
	
	# data preprocessing
	for n in nominals_features:
		tmp, indexes = pd.factorize(data[n])
		data[n] = tmp

	return data
	
def split_with_label(data:any, balance:bool, label:str, skip:list[str]):	
	
	data = pd.DataFrame(data).drop(skip,axis='columns')

	if balance:
		g = data.groupby(label)
		data = g.apply(lambda x: x.sample(g.size().min()).reset_index(drop=True))

	features_length = len(data.iloc[1,:]) - 1
	label_index = len(data.iloc[1,:]) - 1

	return data.iloc[:, 0:features_length-1], data.iloc[:, label_index]

to_drop = ['ct_flw_http_mthd','is_ftp_login','ct_ftp_cmd'] + flow_features

# binary


data = pd.concat([
	read_data('UNSW-NB15/UNSW-NB15_1.csv',headers=headers),
	read_data('UNSW-NB15/UNSW-NB15_2.csv',headers=headers),
	read_data('UNSW-NB15/UNSW-NB15_3.csv',headers=headers),
])

training_data, training_labels = split_with_label(
	data=data,
	balance=True,
	label='Label',
	skip= to_drop + ['attack_cat']
)

data = read_data('UNSW-NB15/UNSW-NB15_4.csv',headers=headers)

testing_data, testing_labels = split_with_label(
	data=data,
	balance=False,
	label='Label',
	skip= to_drop + ['attack_cat']
)


classifiers = {
	"randomforest" : RandomForestClassifier(),
	# "mlp" : MLPClassifier(),
	# "svm" : svm.SVC(),
	# "perceptron" : Perceptron(),
    # "bayes" : GaussianNB(),
}

for k, v in classifiers.items():
	model = v.fit(
		training_data,
		ravel(training_labels)
	)

	labels = model.predict(testing_data)

	score = accuracy_score(ravel(testing_labels), labels)

	print(confusion_matrix(testing_labels, labels))
	print(k, score)


# non-binary


data = pd.concat([
	read_data('UNSW-NB15/UNSW-NB15_1.csv',headers=headers),
	read_data('UNSW-NB15/UNSW-NB15_2.csv',headers=headers),
	read_data('UNSW-NB15/UNSW-NB15_3.csv',headers=headers),
])

data = data[data['Label'] != 0]

training_data, training_labels = split_with_label(
	data=data,
	balance=True,
	label='attack_cat',
	skip= to_drop + ['Label']
)

data = read_data(
	'UNSW-NB15/UNSW-NB15_4.csv',
	headers=headers,
)

data = data[data['Label'] != 0]

testing_data, testing_labels = split_with_label(
	data=data,
	balance=False,
	label='attack_cat',
	skip= to_drop + ['Label']
)


classifiers = {
	"randomforest" : RandomForestClassifier(),
}

for k, v in classifiers.items():
	model = v.fit(
		training_data,
		ravel(training_labels)
	)

	labels = model.predict(testing_data)
	score = accuracy_score(ravel(testing_labels), labels)

	# print(confusion_matrix(testing_labels, labels))
	print(k, score)
