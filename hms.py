# salame

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

from sklearn.metrics import accuracy_score, confusion_matrix
from pandas import read_csv
from numpy import ravel
from sklearn.neural_network import MLPClassifier

import pandas as pd

from constants import *

# import data

def read_data(path:str, headers:list[str], to_drop:list[str], balance:bool):
	
	data = read_csv(
		path,
		low_memory=False,
		names = headers
	)
	# data = data.sample(10_000)
	
	# data preprocessing
	for n in nominals_features:
		tmp, indexes = pd.factorize(data[n])
		data[n] = tmp

	# features selection
	data = pd.DataFrame(data).drop(to_drop,axis='columns')

	if balance:
		g = data.groupby('Label')
		data = g.apply(lambda x: x.sample(g.size().min()).reset_index(drop=True))

	# training
	length = len(data.iloc[1,:]) - 2
	label_index = len(data.iloc[1,:]) - 1

	return data.iloc[:, 0:length], data.iloc[:, label_index]

to_drop = ['ct_flw_http_mthd','is_ftp_login','ct_ftp_cmd'] + flow_features

training_data, training_labels = read_data(
	'UNSW-NB15/UNSW-NB15_1.csv',
	headers=headers,
	to_drop=to_drop,
	balance=True
)

testing_data, testing_labels = read_data(
	'UNSW-NB15/UNSW-NB15_3.csv',
	headers=headers,
	to_drop=to_drop,
	balance=False
)

mlp = MLPClassifier(random_state=0)

model = RandomForestClassifier().fit(
		training_data, 
		ravel(training_labels)
	)

labels = model.predict(testing_data)

score = accuracy_score(ravel(testing_labels), labels)
print(score)





